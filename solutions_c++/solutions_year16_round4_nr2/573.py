#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
typedef pair<int, int> pii;
const double eps = 1e-7;
const int maxn = 200 + 5;
int n, k;
double p[maxn], a[maxn];
double dp[2][maxn << 1];
inline void get(int &x)
{
	char ch = getchar();
	while (ch < '0' || ch > '9') ch = getchar();
	x = ch - '0';
	while (ch = getchar(), ch >= '0' && ch <= '9') x = 10 * x + ch - '0';
}
double run()
{
	get(n); get(k);
	for (int i = 0; i < n; i++) scanf("%lf", p + i);
	sort(p, p + n);
	double res = 0;
	for (int z = 0; z <= k ;z++)
	{
		double *x = dp[0], *y = dp[1];
		memset(dp, 0, sizeof dp);
		y[200] = 1.0;
		for (int i = 0; i < z; i++, swap(x,y))
		{
			memset(x, 0, sizeof dp[0]);
			for (int j = 200 - k; j < 200 + k; j++) if (y[j] > eps) x[j + 1] += y[j] * p[i], x[j - 1] += y[j] * (1 - p[i]);
		}
		for (int i = 0; i < k - z; i++, swap(x,y))
		{
			memset(x, 0, sizeof dp[0]);
			for (int j = 200 - k; j < 200 + k; j++) if (y[j] > eps) x[j + 1] += y[j] * p[n - i - 1], x[j - 1] += y[j] * (1 - p[n - i - 1]);
		}
		res = max(res, y[200]);
	}
	return res;
}
int main()
{
//	freopen("B-small-attempt1.in", "r", stdin);
//	freopen("B-large.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	int T;
	get(T);
	for (int cas = 1; cas <= T; cas++) printf("Case #%d: %.8f\n", cas, run());
	return 0;
}

