#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

const int N = 5;
int adj[N][N], now[N][N];

bool good(int n)
{
	for (int c = 0; c < n; c++)
	{
		vector <int> nbh;
		for (int i = 0; i < n; i++)
			if (now[c][i])
				nbh.push_back(i);

		vector <int> rest;
		for (int i = 0; i < n; i++)
			if (i != c)
				rest.push_back(i);

		int sz = nbh.size();
		if (sz == 0) return false;

		for (int msk = 0; msk < (1 << (n - 1)); msk++)
			if (__builtin_popcountll(msk) == sz)
			{
				vector <int> cur;
				for (int i = 0; i < n - 1; i++)
					if (msk >> i & 1)
						cur.push_back(rest[i]);

				do
				{
					bool can = true;
					for (int i = 0; i < sz; i++)
						if (!now[cur[i]][nbh[i]])
							can = false;
					if (can) return false;
				}
				while (next_permutation(cur.begin(), cur.end()));
			}
	}
	return true;
}

#undef int
int main()
{
#define int long long
	int t; cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cerr << "Executing Case #" << tt << "\n";
		int n; cin >> n;
		for (int i = 0; i < n; i++)
		{
			string s; cin >> s;
			for (int j = 0; j < n; j++)
				adj[i][j] = s[j] - '0';
		}

		vector < pair <int, int> > rem;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				if (!adj[i][j])
					rem.push_back(make_pair(i, j));

		int sz = rem.size();
		for (int msk = 0; msk < 1 << sz; msk++)
		{
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					now[i][j] = adj[i][j];

			for (int i = 0; i < sz; i++)
				if (msk >> i & 1)
					now[rem[i].first][rem[i].second] = true;

			if (good(n))
			{
				cout << "Case #" << tt << ": " << __builtin_popcountll(msk) << "\n";
				break;
			}
		}
	}
	return 0;
}
