#include <stdio.h>
#include <string.h>
#define MAXN 104
#define MAX(a,b)    ((a) > (b) ? (a) : (b))
#define MIN(a,b)    ((a) < (b) ? (a) : (b))

int map[MAXN][MAXN];
int hr[MAXN], hc[MAXN];
int n, m;

int msk[4][2] = {
	{1,0}, {-1,0}, {0,1}, {0,-1}
};

bool Solve()
{
	int i, j, dir, r, c;
	int height;
	
	scanf("%d%d", &n, &m);
	memset (hr, 0, sizeof hr);
	memset (hc, 0, sizeof hc);
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
		{
			scanf("%d", &map[i][j]);
			hr[i] = MAX(hr[i], map[i][j]);
			hc[j] = MAX(hc[j], map[i][j]);
		}
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
			if (map[i][j] != MIN(hr[i], hc[j]))
				return false;
	return true;
}

int main()
{
	int cas, t;
	bool ans;
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++)
	{
		ans = Solve();
		printf("Case #%d: %s\n", cas, ans == true ? "YES" : "NO");
	}
	return 0;
}
