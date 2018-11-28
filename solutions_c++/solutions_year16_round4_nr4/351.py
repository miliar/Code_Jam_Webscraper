#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<cmath>
#include<cstdlib>
#include<queue>
using namespace std;

#define pb push_back
#define mp make_pair
#define sc second
#define ft first

#define FOR(i,N) for (int i=1; i<=N; i++)
#define REP(i,l,r) for (int i=l; i<=r; i++)

#define INF ~0U>>1
#define eps 1e-9

int ans;
const int maxn = 10;
int a[maxn][maxn], b[maxn][maxn], p[maxn];
int vis[10];
int n;

bool Try (int x)
{
	int k = p[x]; int bo = 0;
	if (x == n + 1) return true;
	for (int i = 1; i <= n; i ++)
		if (!vis[i])
		{
			if (a[k][i] + b[k][i] == 0) continue;
			bo = 1;
			vis[i] = 1;
			if (!Try (x + 1))
			{
				vis[i] = 0;
				return false;
			}
			vis[i] = 0;
		}
	if (!bo) return false;
	return true;
}

bool solve ()
{
	int k = 1;
	for (int i = 1; i <= n; i ++)
	{
		 k = k * i;
		 p[i] = i;
	}
	for (int i = 1; i <= k; i ++)
	{
		if (!Try(1)) return false;
		next_permutation (p + 1, p + n + 1);
	}
	return true;
}

void dfs (int x, int y, int k)
{
	int dx, dy;
	if (x == n + 1)
	{
		if (k >= ans) return;
		if (solve()) ans = k;
		return;
	}
	if (y == n)
	{
		dx = x + 1;
		dy = 1;
	}
	else
	{
		dx = x;
		dy = y + 1;
	}
	b[x][y] = 0;
	dfs (dx, dy, k);
	if (a[x][y] == 1) return;
	b[x][y] = 1;
	dfs (dx, dy, k + 1);
}

int main ()
{
#ifndef ONLINE_JUDGE
#ifndef MEKTPOY
	freopen (".in", "r", stdin);
	freopen (".out", "w", stdout);
#else
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);
#endif
#endif
	int T;
	cin >> T;
	for (int test = 1; test <= T; test ++)
	{
		printf ("Case #%d: ", test);
		cin >> n;
		for (int i = 1; i <= n; i ++)
		{
			char s[10];
			scanf ("%s", s + 1);
			for (int j = 1; j <= n; j ++)
				a[i][j] = s[j] - '0';
		}
		ans = n * n;
		dfs (1, 1, 0);
		printf ("%d\n", ans);
	}
	return 0;
}

