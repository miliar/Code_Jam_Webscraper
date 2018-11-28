#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn = 205;
int t, n, m;
double a[maxn], pre[maxn][maxn], suf[maxn][maxn], ans;
int main()
{
	scanf("%d", &t);
	for(int Case = 1; Case <= t; ++Case)
	{
		ans = -1;
		scanf("%d%d", &n, &m);
		for(int i = 1; i <= n; ++i)
			scanf("%lf", a + i);
		sort(a + 1, a + n + 1);
		memset(pre[0], 0, sizeof(pre[0]));
		pre[0][0] = 1;
		for(int i = 1; i <= n; ++i)
			for(int j = 0; j <= m; ++j)
				pre[i][j] = pre[i - 1][j] * (1 - a[i]) + (j > 0 ? pre[i - 1][j - 1] * a[i] : 0);
		memset(suf[n + 1], 0, sizeof(suf[0]));
		suf[n + 1][0] = 1;
		for(int i = n; i >= 1; --i)
			for(int j = 0; j <= m; ++j)
				suf[i][j] = suf[i + 1][j] * (1 - a[i]) + (j > 0 ? suf[i + 1][j - 1] * a[i] : 0);
		for(int i = 0; i <= m; ++i)
		{
			double *L = pre[i], *R = suf[n - (m - i) + 1], val = 0;
			for(int j = 0; j <= (m >> 1); ++j)
				val += L[j] * R[(m >> 1) - j];
			if(ans < val)
				ans = val;
		}
		printf("Case #%d: %.10f\n", Case, ans);
	}
	return 0;
}
