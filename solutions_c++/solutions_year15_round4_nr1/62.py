#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std;
int T, n, m, ans;
char a[110][110];

bool go(int x, int y, int dx, int dy)
{
	if (x<1 || y<1 || x>n || y>m) return 0;
	if (a[x][y] != '.') return 1;
	return go(x + dx, y + dy, dx, dy);
}

bool solve()
{
	ans = 0;
	for (int i = 1;i <= n;i++)
	{
		for (int j = 1;j <= m;j++)
		{
			if (a[i][j] == '.') continue;
			if (a[i][j] == '^' && go(i-1, j, -1, 0)) continue;
			if (a[i][j] == 'v' && go(i+1, j, 1, 0)) continue;
			if (a[i][j] == '<' && go(i, j-1, 0, -1)) continue;
			if (a[i][j] == '>' && go(i, j+1, 0, 1)) continue;
			ans++;
			if (!go(i-1, j, -1, 0) && !go(i+1, j, 1, 0) && !go(i, j-1, 0, -1) && !go(i, j+1, 0, 1)) return 0;
		}
	}
	return 1;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for (int t = 1;t <= T;t++)
	{
		cin >> n >> m;
		for (int i = 1;i <= n;i++) scanf("%s", a[i] + 1);
		printf("Case #%d: ", t);
		if (!solve()) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
}