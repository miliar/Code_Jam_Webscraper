#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

char a[107][107];

void solve(int t)
{
	printf("Case #%d: ", t);
	int n, m;
	scanf("%d%d ", &n, &m);
	for (int i = 0; i < n; ++i)
		scanf("%s", a[i]);
	int ans = 0;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			if (a[i][j] == '.')
				continue;
//			printf("!!%d %d\n", i, j);
			bool occ[4];
			memset(occ, false, sizeof(occ));
			for (int u = 0; u < i; ++u)
				if (a[u][j] != '.')
					occ[0] = true;
//			printf("    %d\n", occ[0]);
			for (int u = i + 1; u < n; ++u)
				if (a[u][j] != '.')
					occ[1] = true;
			for (int u = 0; u < j; ++u)
				if (a[i][u] != '.')
					occ[2] = true;
			for (int u = j + 1; u < m; ++u)
				if (a[i][u] != '.')
					occ[3] = true;
			if (!((a[i][j] == '^' && occ[0]) || (a[i][j] == 'v' && occ[1]) || (a[i][j] == '<' && occ[2]) || (a[i][j] == '>' && occ[3])))
			{
//				printf("%d %d\n", i, j);
				ans++;
				if (!(occ[0] || occ[1] || occ[2] || occ[3]))
				{
					printf("IMPOSSIBLE\n");
					return;
				}
			}
		}
	}
	printf("%d\n", ans);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		solve(i + 1);
	}
	return 0;
}