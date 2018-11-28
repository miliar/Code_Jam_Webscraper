#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
using namespace std;
struct st
{
	int x1;
	int x2;
	int y1;
	int y2;
}p[10001] = {0};
int q[1000001] = {0};
int vis[50001] = {0};
int f[2001][2001] = {0};
int dp[2001] = {0};
int N;
int spfa(int vs, int vt)
{
	int close = 0, open = 1;
	memset(vis, 0, sizeof(vis));
	for (int i = 1; i <= N; i++)
		dp[i] = 1000000000;
	vis[vs] = 1;
	q[close] = vs;
	dp[vs] = 0;
	while (close < open)
	{
		int v = q[close];
		for (int i = 1; i <= N; i++)
		{
			int k = i;
			if (dp[k] > f[v][k] + dp[v])
			{
				dp[k] = f[v][k] + dp[v];
				if (vis[k] == 0)
				{
					vis[k] = 1;
					q[open++] = k;
				}
			}
		}
		vis[v] = 0;
		close++;
	}
	return dp[vt];
}
int cal(int s1, int t1, int s2, int t2)
{
	int ret = 0;
	if (s1 > s2)
	{
		swap(s1, s2);
		swap(t1, t2);
	}
	if (s2 >= t1) return s2 - t1;
	else return 0;
} 
int calc(st x, st y)
{
	int px = cal(x.x1, x.x2, y.x1, y.x2);
	int py = cal(x.y1, x.y2, y.y1, y.y2);
	return max(px, py);
}
int main()
{
	int tot;
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &tot);
	for (int tt = 1; tt <= tot; tt++)
	{
		printf("Case #%d: ", tt);
		int n, w, h;
		scanf("%d%d%d", &w, &h, &n);
		for (int i = 1; i <= n; i++)
		{
			scanf("%d%d%d%d", &p[i].x1, &p[i].y1, &p[i].x2, &p[i].y2);
			if (p[i].x1 > p[i].x2) swap(p[i].x1, p[i].x2);
			if (p[i].y1 > p[i].y2) swap(p[i].y1, p[i].y2);
			p[i].x2++, p[i].y2++;
		}
		p[n+1].x1 = -10000, p[n+1].y1 = -10000;
		p[n+1].x2 = 0, p[n+1].y2 = h;
		p[n+2].x1 = w, p[n+2].y1 = -10000;
		p[n+2].x2 = w+1000, p[n+2].y2 = h;
		n+=2;
		N = n;
		memset(f, 0, sizeof(f));
		for (int i = 1; i <= n; i++)
		{
			for (int j = i+1; j <= n; j++)
			{
				f[i][j] = f[j][i] = calc(p[i], p[j]);
			}
		}
		int ans = spfa(n-1, n);
		printf("%d\n", ans);
	}
	return 0;
}
