#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#define REP(i, n) for (int i = 0; i < int(n); ++i)
#define FOR(i, c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALL(c) (c).begin(), (c).end()
using namespace std;
template<typename T> inline void checkMin(T& a, T b) { if (a > b) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (a < b) a = b; }

inline int divideFloor(int a, int b) {
	int ret = a / b;
	if (a % b != 0 && a < 0) {
		ret -= 1;
	}
	return ret;
}

class BigInteger {
private:
	static const int B = (int)1E9;
	vector<int> iv;
	void div2() {
		long long c = 0LL;
		for (int i = (int)iv.size() - 1; i >= 0; --i)
			c = B * c + iv[i], iv[i] = c / 2, c %= 2;
		while (iv.size() > 1U && iv[iv.size() - 1] == 0) iv.pop_back();
	}
public:
	BigInteger(const string& s) {
		for (int i = (int)s.size() - 1, to; i >= 0; i = to) {
			to = max(-1, i - 9);
			int v = 0; for (int j = to + 1; j <= i; ++j) v = 10 * v + (s[j] - '0');
			iv.push_back(v);
		}
	}
	BigInteger(long long v=0LL) {
		if (v == 0) iv.push_back(0);
		else for ( ; v > 0; v /= B) iv.push_back(v % B);
	}
	bool operator<(const BigInteger& rhs) const {
		if (iv.size() != rhs.iv.size()) return iv.size() < rhs.iv.size();
		for (int i = (int)iv.size() - 1; i >= 0; --i)
			if (iv[i] != rhs.iv[i]) return iv[i] < rhs.iv[i];
		return false;
	}
	void add(const BigInteger& rhs) {
		iv.resize(max(iv.size(), rhs.iv.size()), 0);
		int i; for (i = 0; i < (int)rhs.iv.size(); ++i) iv[i] += rhs.iv[i];
		for (i = 0; i < (int)iv.size() - 1; ++i) iv[i + 1] += iv[i] / B, iv[i] %= B;
		for (; iv[i] >= B; ++i) iv.push_back(iv[i] / B), iv[i] %= B;
	}
	void sub(const BigInteger& rhs) { // (*this < rhs) == false
		int i, c; for (i = 0, c = 0; i < (int)rhs.iv.size(); ++i) {
			iv[i] -= c;
			if (iv[i] < rhs.iv[i]) iv[i] = iv[i] + B - rhs.iv[i], c = 1;
			else iv[i] -= rhs.iv[i], c = 0;
		}
		if (c != 0) iv[i] -= c;
		while (iv.size() > 1U && iv[iv.size() - 1] == 0) iv.pop_back();
	}
	void mul(const BigInteger& rhs) {
		vector<int> bv(iv);
		iv.assign(iv.size() + rhs.iv.size(), 0);
		for (int i = 0; i < (int)rhs.iv.size(); ++i)
			for (int j = 0; j < (int)bv.size(); ++j) {
				long long c = (long long)bv[j] * rhs.iv[i] + iv[i + j];
				iv[i + j] = c % B, iv[i + j + 1] += c / B;
			}
		while (iv.size() > 1U && iv[iv.size() - 1] == 0) iv.pop_back();
	}
	void div(const BigInteger& rhs) {
		static BigInteger ONE(1);
		BigInteger l(0), r(0), m1, m2;
		r.iv.assign(iv.size() - rhs.iv.size() + 2, 0); *r.iv.rbegin() = 1;
		while (l < r) {
			m1 = l; m1.add(r); m1.div2(); m2 = m1; m2.add(ONE);
			BigInteger temp(m2); temp.mul(rhs);
			if (*this < temp) r = m1; else l = m2;
		}
		*this = l;
	}
	void mod(const BigInteger& rhs) {
		BigInteger d = *this;
		d.div(rhs); d.mul(rhs);
		this->sub(d);
	}
	string to_s() {
		char str[10]; string ret;
		vector<int>::reverse_iterator rit = iv.rbegin();
		sprintf(str, "%d", *rit); ret += str;
		for (++rit; rit != iv.rend(); ++rit)
			sprintf(str, "%09d", *rit), ret += str;
		return ret;
	}
};

inline bool isPar(string s) {
	for (int i = 0, j = (int)s.size() - 1; i < j; ++i, --j) {
		if (s[i] != s[j]) {
			return false;
		}
	}
	return true;
}

vector<BigInteger> g[105];

vector<BigInteger> lv;
int gao(const BigInteger& N) {
	return upper_bound(ALL(lv), N) - lv.begin();
}

int main() {
	g[1].push_back(BigInteger(1));
	g[1].push_back(BigInteger(2));
	g[1].push_back(BigInteger(3));
	for (int w = 3; w <= 55; w += 2) {
		FOR (iter, g[w - 2]) {
			string s = iter->to_s();
			string t = s.substr((int)s.size() / 2);
			string tt = t;
			reverse(ALL(tt));
			BigInteger temp(tt + t);
			BigInteger temp2 = temp;
			temp2.mul(temp);
			if (isPar(temp2.to_s())) {
				g[w - 1].push_back(temp);
				REP (o, 3) {
					temp = BigInteger(tt + (char)('0' + o) + t);
					temp2 = temp;
					temp2.mul(temp);
					if (isPar(temp2.to_s())) {
						g[w].push_back(temp);
					}
				}
			}
		}
	}
	for (int w = 1; w <= 54; ++w) {
		FOR (iter, g[w]) {
			lv.push_back(*iter);
		}
	}
	sort(ALL(lv));

	FOR (iter, lv) {
		BigInteger temp(*iter);
		iter->mul(temp);
//		printf("%s => %s\n", temp.to_s().c_str(), iter->to_s().c_str());
	}
//	return 0;

	int n_case;
	scanf("%d", &n_case);
	for (int index = 1; index <= n_case; ++index) {
		static char s1[105], s2[105];
		scanf("%s%s", s1, s2);
		BigInteger A(s1), B(s2);
		A.sub(BigInteger(1));
		printf("Case #%d: %d\n", index, gao(B) - gao(A));
	}
	return 0;
}
