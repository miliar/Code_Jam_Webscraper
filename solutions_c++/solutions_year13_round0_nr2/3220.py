#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const int maxN = 110;

int res[maxN][maxN], cur[maxN][maxN];
int t, n, m;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		scanf("%d%d", &n, &m);
		printf("Case #%d: ", q + 1);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				scanf("%d", &res[i][j]);
				cur[i][j] = 100;
			}
		}
		for (int i = 0; i < n; i++)
		{
			int rmax = 0;
			for (int j = 0; j < m; j++)
			{
				rmax = max(rmax, res[i][j]);
			}
			for (int j = 0; j < m; j++)
			{
				cur[i][j] = min(rmax, cur[i][j]);
			}
		}
		for (int j = 0; j < m; j++)
		{
			int cmax = 0;
			for (int i = 0; i < n; i++)
			{
				cmax = max(cmax, res[i][j]);
			}
			for (int i = 0; i < n; i++)
			{
				cur[i][j] = min(cmax, cur[i][j]);
			}
		}
		bool yes = true;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (cur[i][j] != res[i][j])
				{
					yes = false;
				}
			}
		}
		if (yes)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}
	return 0;
}