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

double ans, tmp;
const int maxn = 210;
//int vis[maxn];
double a[maxn];
double f[maxn][maxn], g[maxn][maxn];
int N, K;
/*
vector <double> A;

void Dfs (int x, int num, double P)
{
	if (x == K + 1)
	{
		if (num == K / 2)
		{
			tmp += P;
		}
		return;
	}
	Dfs (x + 1, num + 1, P * A[x]);
	Dfs (x + 1, num, P * (1.0 - A[x]));
}

void solve ()
{
	A.clear();
	tmp = 0;
	for (int i = 1; i <= N; i ++)
		if (vis[i])
			A.pb (a[i]);
	Dfs (0, 0, 1.0);
	if (tmp > ans) ans = tmp;
}

void dfs (int x, int num)
{
	if (x == N + 1)
	{
		if (num == K)
		{
			solve ();
		}
		return;
	}
	vis[x] = 1;
	dfs (x + 1, num + 1);
	vis[x] = 0;
	dfs (x + 1, num);
}

*/
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
		cin >> N >> K;
		for (int i = 1; i <= N; i ++)
			scanf ("%lf", &a[i]);
		ans = 0.0;
		sort (a + 1, a + N + 1);
		memset (f, 0, sizeof(f));
		f[0][0] = 1.0;
		for (int i = 1; i <= N; i ++)
			for (int j = 0; j <= N; j ++)
			{
				if (j) f[i][j] += f[i - 1][j - 1] * a[i];
				f[i][j] += f[i - 1][j] * (1.0 - a[i]);
			}
		memset (g, 0, sizeof(g));
		g[N + 1][0] = 1.0;
		for (int i = N; i >= 1; i --)
			for (int j = 0; j <= N; j ++)
			{
				if (j) g[i][j] += g[i + 1][j - 1] * a[i];
				g[i][j] += g[i + 1][j] * (1.0 - a[i]);
			}
		for (int i = 0; i <= K; i ++)
		{
			double tmp = 0;
			for (int j = 0; j <= i; j ++)
			{
				if (j > K / 2) continue;
				tmp += f[i][j] * g[N - (K - i) + 1][K / 2 - j];
			}
			if (tmp > ans) ans = tmp;
		}
		printf ("%.10f\n", ans);
	}
	return 0;
}

