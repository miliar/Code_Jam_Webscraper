#include <stdio.h>
#include <algorithm>

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N, K;
		double a[300] = {0};
		scanf("%d%d", &N, &K);
		for (int i=0; i<N; i++) {
			scanf("%lf", &a[i]);
		}
		std::sort(a, a+N);
		long double m = 0.0;
		for (int pp=0; pp<=K; pp++) {
			long double dp[300][2];
			dp[0][0] = 1.0;
			dp[0][1] = 0.0;
			for (int i=1; i<=K; i++) {
				dp[i][0] = 0.0;
				dp[i][1] = 0.0;
			}
			int l = 0;
			int r = N-1;
			for (int i=0; i<K; i++) {
				int now = i%2;
				int next = 1-now;
				for (int j=0; j<=K; j++) {
					dp[j][next] = 0.0;
				}
				int p = 0;
				if (i < pp) {
					p = r;
					r--;
				} else {
					p = l;
					l++;
				}
				for (int j=0; j<=i; j++) {
					dp[j][next] += dp[j][now] * (1.-(long double)a[p]);
					dp[j+1][next] += dp[j][now] * (long double)a[p];
				}
			}
			if (dp[K/2][0] > m) {
				m = dp[K/2][0];
			}
		}
		printf("Case #%d: %.20llf\n", t, m);

	}
	return 0;
}