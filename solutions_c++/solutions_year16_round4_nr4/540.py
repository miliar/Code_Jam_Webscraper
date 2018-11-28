#include <algorithm>
#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <cassert>
#include <set>
#include <cstring>
#include <numeric>
#include <map>
#include <cmath>

using namespace std;

#define forsn(i, s, n) for (int i = s; i < n; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())
#define all(n) n.begin(), n.end()

#define popcount __builtin_popcount

const int big = 1000000;

typedef unsigned long bs;

bool go(const vector <int> &o, bs h, int n, bs k, int z = 0)
{
	if (n == o.size())
		return true;
	
	bool some = false;
	fore(m, o)
	{
		bs b = 1ul << o[n] * o.size() + m;
		bs v = 1ul << m;

		if ((h & b) == 0 || (k & v) != 0)
			continue;

		some = true;
		if (!go(o, h, n + 1, k | v, z + 1))
			return false;
	}

	return some;
}

bool test(int n, bs h)
{
	vector <int> o(n);
	iota(all(o), 0);

	do
	{
		if (!go(o, h, 0, 0ul))
			return false;
	}
	while (next_permutation(all(o)));

	return true;
}

int solve(int n, bs b)
{
	int r = big;
	int k = n * n;
	
	for (bs g = 0; g < (1ul << k); g++)
	{
		if (test(n, b | g))
			r = min(r, popcount(g));
	}

	return r;
}

int main()
{
	int t; cin >> t;

	forsn(z, 1, t + 1)
	{
		int n;
		cin >> n;
	
		string s;
		forn(i, n)
		{
			string k;
			cin >> k;

			s += k;
		}

		unsigned long b = stoull(s, nullptr, 2);
		printf("Case #%d: %d\n", z, solve(n, b));
	}

	return 0;
}
