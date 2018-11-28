#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>

using namespace std;

int nr, nc;
char a[128][128];
char mark[128][128];

int dfs(int sr, int sc)
{
	int r = sr, c = sc;
	int dir = a[r][c];
	int lr = sr, lc = sc;
	while (r >= 0 && r < nr && c >= 0 && c < nc)
	{
		if (a[r][c] >= 0)
		{
			lr = r;
			lc = c;
			dir = a[r][c];
		}
		if (mark[r][c] >> dir & 1)
			return 0;
		mark[r][c] |= 1 << dir;
		int d = dir & 2? -1: 1;
		if (dir & 1)
			r += d;
		else
			c += d;
	}
	for (dir = 0; dir < 4; ++dir)
	{
		for (r = lr, c = lc; ; )
		{
			int d = dir & 2? -1: 1;
			if (dir & 1)
				r += d;
			else
				c += d;
			if (r < 0 || r >= nr || c < 0 || c >= nc)
				break;
			if (a[r][c] >= 0)
			{
				a[lr][lc] = dir;
				return 1;
			}
		}
	}
	return -1;
}

int solve()
{
	memset(mark, 0, sizeof(mark));
	int res = 0;
	for (int i = 0; i < nr; ++i)
		for (int j = 0; j < nc; ++j)
			if (a[i][j] >= 0 && !mark[i][j])
			{
				int t = dfs(i, j);
				if (t < 0)
					return -1;
				res += t;
			}
	return res;
}

int main()
{
	int itest, ntest;
	scanf("%d", &ntest);
	for (itest = 0; ++itest <= ntest; )
	{
		scanf("%d%d", &nr, &nc);
		for (int i = 0; i < nr; ++i)
		{
			scanf(" %s", a[i]);
			for (int j = 0; j < nc; ++j)
			{
				if (a[i][j] == '>')
					a[i][j] = 0;
				else if (a[i][j] == 'v')
					a[i][j] = 1;
				else if (a[i][j] == '<')
					a[i][j] = 2;
				else if (a[i][j] == '^')
					a[i][j] = 3;
				else
					a[i][j] = -1;
			}
		}
		int res = solve();
		printf("Case #%d: ", itest);
		if (res < 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}
	return 0;
}
