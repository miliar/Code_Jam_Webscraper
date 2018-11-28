#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <functional>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

map<vector<string>, bool> dp;

bool f(const vector<string>& v)
{
	if (v.size() == 1)
		return v[0][0] == '1';
	if (dp.count(v)) return dp[v];

	bool ok = 0;
	for (int i = 0; i < v.size(); i++)
	{
		for (int j = 0; j < v.size(); j++)
		{
			if (v[i][j] != '1') continue;
			ok = 1;
			vector<string> g;

			for (int k = 0; k < v.size(); k++)
			{
				if (k == i) continue;
				string cur = "";
				for (int t = 0; t < v.size(); t++)
				{
					if (t == j) continue;
					cur += v[k][t];
				}
				g.push_back(cur);
			}
			if (!f(g))
			{
				return dp[v] = 0;
			}
		}
	}

	return dp[v] = ok;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tests;
	cin >> tests;
	for (int q = 0; q < tests; q++)
	{
		int n;
		cin >> n;

		vector<string> v(n);
		for (int i = 0; i < n; i++) cin >> v[i];

		int ans = 1e9;
		
		for (int i = 0; i < (1 << (n * n)); i++)
		{
			int cur = 0;
			vector<string> t(n);
			for (int j = 0; j < n * n; j++)
			{
				if ((i >> j) & 1) t[j / n] += '1';
				else t[j / n] += '0';
			}

			bool ok = 1;
			for (int j = 0; j < n; j++)
			{
				for (int k = 0; k < n; k++)
				{
					if (v[j][k] == '0' && t[j][k] == '1') cur++;
					if (v[j][k] == '1' && t[j][k] == '0')
					{
						ok = 0;
					}
				}
			}

			if (ok && f(t))
				ans = min(ans, cur);
		}

		printf("Case #%d: ", q + 1);
		printf("%d\n", ans);

	}

	return 0;
}