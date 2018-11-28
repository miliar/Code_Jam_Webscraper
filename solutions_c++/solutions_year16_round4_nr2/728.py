#include <algorithm>
#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <cassert>
#include <set>
#include <cstring>
#include <map>
#include <cmath>

using namespace std;

#define forsn(i, s, n) for (int i = s; i < n; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())
#define all(n) n.begin(), n.end()

#define popcount __builtin_popcount

double solve(const vector <double> &V, int k)
{
	double r = 0;

	for (unsigned long b = 0; b < (1 << V.size()); b++)
	{
		if (popcount(b) != k)
			continue;

		vector <double> e(2 * k + 1, 0);
		e[0 + k] = 1;

		unsigned long h = b;
		for (int i = 0; h > 0; i++, h >>= 1)
		{
			if ((h & 1) == 0)
				continue;

			vector <double> f(2 * k + 1, 0);
			fore(j, e)
			{
				if (j > 0)
					f[j] += e[j - 1] * V[i];

				if (j < e.size() - 1)
					f[j] += e[j + 1] * (1 - V[i]);
			}

			swap(e, f);
		}

		r = max(r, e[0 + k]);
	}

	return r;
}

int main()
{
	int t; cin >> t;

	forsn(z, 1, t + 1)
	{
		int n, k;
		cin >> n >> k;

		vector <double> V(n);
		fore(i, V)
			cin >> V[i];

		printf("Case #%d: %f\n", z, solve(V, k));
	}

	return 0;
}
