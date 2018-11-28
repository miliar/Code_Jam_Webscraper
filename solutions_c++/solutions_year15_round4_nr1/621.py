#include <cstdio>
#include <cstring>
const int maxn = 110;
int t, n, m, er[maxn][maxn], ec[maxn][maxn], posr[maxn][maxn], posc[maxn][maxn], ans;
char s[maxn][maxn];
bool vis[maxn][maxn];
void dfs(int x, int y)
{
	if(vis[x][y] == 1)
		return;
	vis[x][y] = 1;
	if(s[x][y] == '<')
	{
		if(posr[x][y] > 1)
			dfs(x, er[x][posr[x][y] - 1]);
		else
			++ans;
	}
	else if(s[x][y] == '>')
	{
		if(posr[x][y] < er[x][0])
			dfs(x, er[x][posr[x][y] + 1]);
		else
			++ans;
	}
	else if(s[x][y] == '^')
	{
		if(posc[x][y] > 1)
			dfs(ec[y][posc[x][y] - 1], y);
		else
			++ans;
	}
	else if(s[x][y] == 'v')
	{
		if(posc[x][y] < ec[y][0])
			dfs(ec[y][posc[x][y] + 1], y);
		else
			++ans;
	}
}
int main()
{
	scanf("%d", &t);
	for(int Case = 1; Case <= t; ++Case)
	{
		ans = 0;
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; ++i)
			scanf("%s", s[i]);
		for(int i = 0; i < n; ++i)
		{
			er[i][0] = 0;
			for(int j = 0; j < m; ++j)
				if(s[i][j] != '.')
				{
					er[i][++er[i][0]] = j;
					posr[i][j] = er[i][0];
				}
		}
		for(int i = 0; i < m; ++i)
		{
			ec[i][0] = 0;
			for(int j = 0; j < n; ++j)
				if(s[j][i] != '.')
				{
					ec[i][++ec[i][0]] = j;
					posc[j][i] = ec[i][0];
				}
		}
		bool flag = 0;
		for(int i = 0; i < n && !flag; ++i)
			for(int j = 0; j < m && !flag; ++j)
				if(s[i][j] != '.' && er[i][0] == 1 && ec[j][0] == 1)
					flag = 1;
		if(flag)
		{
			printf("Case #%d: IMPOSSIBLE\n", Case);
			continue;
		}
		memset(vis, 0, sizeof vis);
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				if(s[i][j] != '.' && !vis[i][j])
					dfs(i, j);
		printf("Case #%d: %d\n", Case, ans);
	}
	return 0;
}
