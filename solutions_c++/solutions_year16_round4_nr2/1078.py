#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;
typedef long long LL;
#define For(i,a,b) for (int i = (a); i <= (b); i++)
#define Cor(i,a,b) for (int i = (a); i >= (b); i--)
#define rep(i,a) for (int i = 0; i < a; i++)
#define Fill(a,b) memset(a,b,sizeof(a))
int n, K;
const int maxn = 210;
double f[maxn][maxn][maxn];
double p[maxn];
void init()
{
	scanf("%d%d", &n, &K);
	for (int i = 0; i < n; i++)
		scanf("%lf", &p[i]);
	memset(f, 0, sizeof(f));
}
vector<double> v;
double calc()
{
	int tot = 1 << K;
	double ret = 0;
	for (int mask = 0; mask < tot; mask++)
	{
		if (__builtin_popcount(mask) != K / 2)
			continue;
		double tmp = 1;
		for (int i = 0; i < K; i++)
			if (mask & (1 << i))
				tmp *= v[i];
			else
				tmp *= (1 - v[i]);
		ret += tmp;
	}
	return ret;
}
void solve(int task)
{
	printf("Case #%d: ", task);
	init();
	/*
	f[0][0][0] = 1.0;
	for (int i = 1; i <= n; i++)
		for (int j = 0; j <= i; j++)
			for (int k = 0; k <= min(K / 2, j); k++)
			{
				f[i][j][k] = max(f[i - 1][j][k], f[i][j][k]);
				if (j != 0 && k != 0)
					f[i][j][k] = max(f[i][j][k], f[i - 1][j - 1][k - 1] * p[i] + f[i - 1][j - 1][k] * (1 - p[i]));
			}
	printf("%.8f\n", f[n][K][K / 2]);
	*/
	int tot = 1 << n;
	double ans = 0;
	for (int mask = 0; mask < tot; mask++)
	{
		if (__builtin_popcount(mask) != K)
			continue;
		v.clear();
		for (int i = 0; i < n; i++)
			if (mask & (1 << i))
				v.push_back(p[i]);
		double p = calc();
		ans = max(ans, p);
	}
	printf("%.8f\n", ans);
}
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
		solve(i);
}
