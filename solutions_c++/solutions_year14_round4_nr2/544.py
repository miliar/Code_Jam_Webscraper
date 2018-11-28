#include <cstdio>

using namespace std;

const int MAXN = 1001;

int dp[MAXN][MAXN];
int l[MAXN], r[MAXN];
int ll[MAXN], rr[MAXN];
int a[MAXN];

void chk(int &x, int y)
{
	if (y < x) x = y;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t ++){
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i ++)
			scanf("%d", &a[i]);
		for (int i = 0; i < n; i ++){
			l[i] = r[i] = 0;
			for (int j = 0; j < i; j ++)
				if (a[j] > a[i])
					l[i] ++;
			for (int j = i+1; j < n; j ++)
				if (a[j] > a[i])
					r[i] ++;
			ll[n-(l[i]+r[i])] = l[i];
			rr[n-(l[i]+r[i])] = r[i];
		}
		dp[0][0] = 0;
		for (int k = 1; k <= n; k ++)
			for (int i = 0; i <= k; i ++){
				int j = k - i;
				//i, j
				dp[i][j] = n * n;
				if (i > 0)
					chk(dp[i][j], dp[i-1][j] + ll[k]);
				if (j > 0)
					chk(dp[i][j], dp[i][j-1] + rr[k]);
			}
		int ans = n * n;
		for (int i = 0; i <= n; i ++)
			if (dp[i][n-i] < ans)
				ans = dp[i][n-i];
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}
