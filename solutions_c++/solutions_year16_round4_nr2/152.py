#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 220;
int n, k;
int que[N], slc[N];
double p[N], ans, f[N][N];

void init()
{
	scanf("%d%d", &n, &k);
	for (int i = 1; i <= n; ++ i)
		scanf("%lf", &p[i]);
}

int main()
{
	//freopen("2.in", "r", stdin);
	//freopen("2.out", "w", stdout);
	int T, Case = 0;
	scanf("%d", &T);
	while (T --)
	{
		init();
		sort(p + 1, p + 1 + n);
		double ans = 0;
		for (int l = 0; l <= k; ++ l)
		{
			memset(f, 0, sizeof(f));
			f[0][0] = 1;
			for (int i = 1; i <= l; ++ i)
				for (int j = 0; j + j <= k && j <= i; ++ j)
				{
					f[i][j] = f[i - 1][j] * (1 - p[i]);
					if (j) f[i][j] += f[i - 1][j - 1] * p[i];
				}
			for (int i = l + 1, r = n; i <= k; ++ i, -- r)
				for (int j = 0; j + j <= k && j <= i; ++ j)
				{
					f[i][j] = f[i - 1][j] * (1 - p[r]);
					if (j) f[i][j] += f[i - 1][j - 1] * p[r];
				}
			ans = max(ans, f[k][k / 2]);
		}
		printf("Case #%d: %.10f\n", ++ Case, ans);
	}		
}