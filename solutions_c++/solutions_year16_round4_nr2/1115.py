#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;
typedef long long int64;
#define rep(x, n) for (int x = 1; x <= n; ++x)
#define zrp(x, n) for (int x = n; x; --x)
#define FOR(x, l, r) for (int x = l; x <= r; ++x)
#define foredge(i, x) for (int i = start[x]; i; i = e[i].l)
struct edge{int a, l;};
double ans = 0, f[2000], p[2000];
int n, k;

double dotry(int x, int t, double now)
{
	if (x > k)
	{
		if (t != 0)
			return 0;
		else
			return now;
	}
	if (t + (k - x + 1) < 0 || t - (k - x + 1) > 0)
		return 0;
	double s = 0;
	s += dotry(x + 1, t + 1, now * f[x]);
	s += dotry(x + 1, t - 1, now * (1 - f[x]));
	return s;
}

void check()
{
	double tmp = dotry(1, 0, 1.0);
	ans = max(ans, tmp);
}

void dfs(int x, int t)
{
	if (t == k)
	{
		check();
		return;
	}
	if (x > n)
	{
		return;
	}
	dfs(x + 1, t);
	f[t + 1] = p[x];
	dfs(x + 1, t + 1);
}

int main()
{
	int T;
	scanf("%d", &T);
	rep(ca, T)
	{

		scanf("%d%d", &n, &k);
		rep(i, n) scanf("%lf", p + i);
		ans = 0;
		dfs(1, 0);

		printf("Case #%d: %.8lf\n", ca, ans);
	}
}
