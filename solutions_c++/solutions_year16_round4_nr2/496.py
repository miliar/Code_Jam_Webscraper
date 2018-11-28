#include <bits/stdc++.h>
using namespace std;


const double eps = 1e-8;

double P[222];
double Q[222];
double dp[222][222];

int main(void) {

	int cases; scanf("%d", &cases);

	int cas = 0;
	while (cases--) {
		printf("Case #%d: ", ++cas);

		int N, K; scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i) scanf("%lf", &P[i]);
		sort(P, P + N);


		double ans = 0;
		for (int x = 0; x <= K; ++x) {
			int cnt = 0;
			for (int i = 0; i < x; ++i) Q[cnt++] = P[i];
			for (int i = N-1, t = 0; t < K-x; --i, ++t) Q[cnt++] = P[i];

			memset(dp, 0, sizeof dp);
			dp[0][0] = 1.0;

			for (int i = 0; i < K; ++i)
				for (int j = 0; j <= i; ++j) if (dp[i][j] > eps) {
					dp[i+1][j] += dp[i][j] * (1-Q[i]);
					dp[i+1][j+1] += dp[i][j] * Q[i];
				}
			ans = max(ans, dp[K][K/2]);
		}
		printf("%.10f\n", ans);
	}


	return 0;
}