#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int n;
int st[30][30], p[30], d[30];

int dfs(int dep) 
{
	if (dep == n) return true;
	bool ok = true, found = false;
	int cur = p[dep];
	for (int i = 0; i < n; ++i) if (st[cur][i] && !d[i]) {
		found = true;
		d[i] = 1;
		ok &= dfs(dep + 1);
		d[i] = 0;
	}
	ok &= found;
	return ok;
}

bool check() 
{
	for (int i = 0; i < n; ++i) p[i] = i;
	bool f = true;
	do {
		f &= dfs(0);
	} while (next_permutation(p, p + n));
	return f;
}

int main()
{
	
	int ncase,i,j,tt=0;
	scanf("%d", &ncase);
	
		freopen("D-small-attempt0.in", "r", stdin);
		freopen("D-small-attempt0.out", "w", stdout);
	while (ncase--) 
	{
		scanf("%d", &n);
		memset(st, 0, sizeof(st));
		
		for (i = 0; i<n; i++)
		for (j = 0; j<n; j++)
			scanf("%1d", &st[i][j]);

		int ans = 25 * 25;
		int t = n * n;
		for (int msk = 0; msk < (1 << t); ++msk) 
		{
			int cnt = 0;
			for (int i = 0; i < t; ++i) if (msk >> i & 1) 
			{
				++cnt;
				++st[i / n][i % n];
			}
			if (check())
			{
				ans = min(ans, cnt);
			}
			for (int i = 0; i < t; ++i) if (msk >> i & 1) 
			{
				--st[i / n][i % n];
			}
		}
		printf("Case #%d: %d\n", ++tt, ans);
	}
	return 0;
}
