#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 30;
int n, ans;
int a[N][N], p[N], que[N], slc[N];

void init()
{
	scanf("%d", &n);
	for (int i = 1; i <= n; ++ i)
		for (int j = 1; j <= n; ++ j)
		{
			char x;
			scanf(" %c", &x);
			a[i][j] = x - '0';
		}
}

bool Check(int dep)
{
	if (dep > n)
		return 1;
	int flag = 0;
	for (int i = 1; i <= n; ++ i) if (a[que[dep]][i] && !slc[i])
	{
		slc[i] = 1;
		if (!Check(dep + 1)) return 0;
		slc[i] = 0;
		flag = 1;
	}
	return flag;
}

bool check(int dep)
{
	if (dep > n)
	{
		memset(slc, 0, sizeof(slc));
		return Check(1);
	}
	for (int i = 1; i <= n; ++ i) if (!p[i])
	{
		que[dep] = i;
		p[i] = 1;
		if (!check(dep + 1)) return 0;
		p[i] = 0;
	}
	return 1;
}

void dfs(int u, int v, int cur)
{
	if (cur >= ans) return;
	if (u > n)
	{
		memset(p, 0, sizeof(p));
		if (check(1)) 
			ans = cur;
		return;
	}
	if (v > n)
	{
		dfs(u + 1, 1, cur);
		return;
	}
	if (a[u][v])
	{
		dfs(u, v + 1, cur);
		return;
	}
	a[u][v] = 1;
	dfs(u, v + 1, cur + 1);
	a[u][v] = 0;
	dfs(u, v + 1, cur);
}

int main()
{
	//freopen("4.in", "r", stdin);
	//freopen("4.out", "w", stdout);
	int T, Case = 0;
	scanf("%d", &T);
	while (T --)
	{	
		init();
		printf("Case #%d: ", ++ Case);
		ans = n * n;
		dfs(1, 1, 0);
		printf("%d\n", ans);
	}
}