#include <bits/stdc++.h>

using namespace std;

using ull  = unsigned long long;
using val  = ull;
using bign = vector<val>;

void trim(bign & a)
{
	while (a.size() > 1 && a.back() == 0)
		a.pop_back();
}

void add(bign & a, const bign & b, val t)
{
	a.resize(max(a.size(), b.size()) + 1);
	for (size_t i = 0; i < b.size(); ++i)
		a[i] += b[i];
	for (size_t i = 0; i + 1 < b.size(); ++i)
		if (a[i] >= t) {
			a[i] -= t;
			++a[i + 1];
		}
	trim(a);
}

void mul(bign & a, val x, val b)
{
	a.resize(a.size() + 2);
	val c = 0;
	for (size_t i = 0; i < a.size(); ++i) {
		a[i] = a[i] * x + c;
		c = a[i] / b;
		a[i] %= b;
	}
	trim(a);
}

val div(bign & a, val x, val b)
{
	val r = 0;
	for (ssize_t i = ssize_t(a.size()) - 1; i >= 0; --i)
		r = ((r * b) + a[i]) % x;
	return r;
}

val try_base(const vector<bool> & v, val b)
{
	assert(b >= 2 && b <= 10);
	bign r(1, 1), x(1, 0);
	for (size_t i = 0; i < v.size(); ++i) {
		if (v[i])
			add(x, r, b);
		mul(r, b, b);
	} 
	for (val d = 3; d < 9; d += 2) {
		bign t(x);
		if (!div(t, d, b))
			return d;
	}
	return 0;
}

void mine(size_t n, size_t m)
{
	static mt19937 rnd;
	static set<vector<bool>> f;
	assert(n >= 2);
	for (size_t t = 0; t < m; ) {
		vector<bool> v(n);
		v[0] = v[n - 1] = true;
		for (size_t i = 1; i + 1 < n; ++i)
			v[i] = rnd() & 1;
		if (f.find(v) != f.end())
			continue;
		f.insert(v);
		val r[11] = {}; bool f = true;
		for (size_t i = 2; i <= 10; ++i)
			if (!(r[i] = try_base(v, val(i)))) {
				f = false;
				break;
			}
		if (f) {
			reverse(v.begin(), v.end());
			for (auto x : v)
				cout << x;
			for (size_t i = 2; i <= 10; ++i)
				cout << " " << r[i];
			cout << endl;
			++t;
		}
	}
}

int main(int argc, char ** argv)
{
    if (argc != 3) {
		cout << "program n m" << endl;
		return 1;
	}
	mine(atoll(argv[1]), atoll(argv[2]));
	return 0;
}
