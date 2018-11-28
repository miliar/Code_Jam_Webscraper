#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>

using namespace std;

struct TestCase {
	
	long long repeats;
	string quat;
};

std::vector<TestCase> load(const std::string& s) {
	std::ifstream fs(s);
	if (!fs.is_open())
		std::cout << "Not found" << std::endl;

	int n;
	std::vector<TestCase> res;
	fs >> n;
	for (int i = 0; i < n; i++) {
		TestCase tc;
		int l;
		fs >> l;
		fs >> tc.repeats;
		fs >> tc.quat;
		res.push_back(tc);
	}
	fs.close();
	return res;
}

struct quat {
	int r, i, j, k;

	quat() {
		r = 1;
		i = j = k = 0;
	}

	quat(const quat& q) {
		r = q.r;
		i = q.i;
		j = q.j;
		k = q.k;
	}

	explicit quat(char c) {
		r = i = j = k = 0;
		switch (c) {
		case 'i': i = 1; break;
		case 'j': j = 1; break;
		case 'k': k = 1; break;
		default: assert(false);
		}
	}

	quat(int _r, int _i, int _j, int _k) : r(_r), i(_i), j(_j), k(_k) {}

	quat mul(const quat& q) {
		return quat(this->r * q.r - this->i * q.i - this->j * q.j - this->k
			* q.k, this->r * q.i + this->i * q.r + this->j * q.k - this->k
			* q.j, this->r * q.j - this->i * q.k + this->j * q.r + this->k
			* q.i, this->r * q.k + this->i * q.j - this->j * q.i + this->k
			* q.r);
	}

	int powHelper(int x, long long count) {
		if (x == -1)
			return count % 2 == 0 ? 1 : -1;
		else if (x == 1)
			return 1;
		else if (x == 0)
			return 0;
		assert(false);
		return x;
	}

	quat pow(long long n) {
		if (n == 0)
			return quat();
		quat half = pow(n / 2);
		return n % 2 == 0 ? half.mul(half) : mul(half.mul(half));
		//return quat(powHelper(r, n), powHelper(i, n), powHelper(j, n), powHelper(k, n));
	}

	bool isR() { return r == 1 && i == 0 && j == 0 && k == 0; }
	bool isI() { return r == 0 && i == 1 && j == 0 && k == 0; }
	bool isJ() { return r == 0 && i == 0 && j == 1 && k == 0; }
	bool isK() { return r == 0 && i == 0 && j == 0 && k == 1; }
	bool is(char c) {
		if (c == 'i') return isI();
		if (c == 'j') return isJ();
		if (c == 'k') return isK();
		assert(false);
		return false;
	}
};

static const char depths[] = { 'i', 'j', 'k' };
typedef std::vector<quat> quatcache;

bool find(const char *s, int modulo, long long offset, long long slen, int depth, quatcache& cache) {
	if (depth == 2) {
		quat muls = cache[0];
		/*for (int i = 0; i < modulo; i++)
			muls = muls.mul(quat(s[i]));*/

		quat current = (offset % modulo == 0) ? quat() : cache[offset % modulo];
		/*for (long long i = offset; i < slen && (i % modulo) != 0; i++) {
			current = current.mul(quat(s[i % modulo]));
		}*/

		long long count = (slen - offset) / modulo;
		quat res = current.mul(muls.pow(count));

		return res.is(depths[depth]);
	}

	quat current;
	long long i = offset;
	for (; i < slen; i++) {
		current = current.mul(quat(s[i % modulo]));
		if (current.is(depths[depth])) {
			if (find(s, modulo, (i + 1), slen, depth + 1, cache))
				return true;
		}
	}

	return false;
}

quatcache computeCache(const char *s, int len) {
	quatcache res;
	res.resize(len);
	quat current;
	for (int i = len - 1; i >= 0; i--) {
		current = quat(s[i]).mul(current);
		res[i] = current;
	}
	return res;
}

std::string solve(TestCase& tc) {
	auto cache = computeCache(tc.quat.c_str(), tc.quat.size());
	return find(tc.quat.c_str(), tc.quat.size(), 0, (long long)tc.quat.size() * tc.repeats, 0, cache) ? "YES" : "NO";
}



int main(int argc, const char *argv[]) {
	std::ofstream fs("C-small-attempt1.out");
	int i = 1;
	for (auto tc : load("C-small-attempt1.in")) {
		std::cout << "Case " << i  << endl;
		fs << "Case #" << i << ": " << solve(tc) << std::endl;
		i++;
	}
	fs.close();
	return 0;
}
