#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
char ch[1001][1001];
int n, m;
int calc(int vi, int vj, int si, int sj)
{
	vi += si;
	vj += sj;
	while (vi >= 0 && vi < n && vj >= 0 && vj < m)
	{
		if (ch[vi][vj] != '.') return 0;
		vi += si;
		vj += sj;
	}
	return 1;
}
int main()
{
	int tot, tt;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &tot);
	for (tt = 1; tt <= tot; tt++)
	{
		
		scanf("%d%d\n", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s", ch[i]);
		int ans = 0, flag = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (ch[i][j] != '.')
				{
					int ss[5];
					ss[0] = calc(i, j, -1, 0);
					ss[1] = calc(i, j, 1, 0);
					ss[2] = calc(i, j, 0, -1);
					ss[3] = calc(i, j, 0, 1);
					if (ch[i][j] == '^')
						ans += ss[0];
					if (ch[i][j] == 'v')
						ans += ss[1];
					if (ch[i][j] == '<')
						ans += ss[2];
					if (ch[i][j] == '>')
						ans += ss[3];
					if (ss[0] && ss[1] && ss[2] && ss[3])
						flag = 1;
			}
		if (flag)
			printf("Case #%d: IMPOSSIBLE\n", tt);
		else
			printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
