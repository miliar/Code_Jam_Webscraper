#include <bits/stdc++.h>

using namespace std;

int T, N, K;
double P[210];
double p[210], dp[210][210];

double DP() {
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for(int i = 1; i <= K; i ++) {
		//cout << p[i] << endl;
		for(int j = 0; j <= i; j ++) {
			dp[i][j] = dp[i-1][j-1] * p[i] + dp[i-1][j] * (1-p[i]);
		}
	}
	return dp[K][K/2];
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas ++) {
		scanf("%d%d", &N, &K);
		for(int i = 0; i < N; i ++) {
			scanf("%lf", &P[i]);
		}
		sort(P, P+N);
		double res = 0;
		for(int mask = 0; mask < N; mask ++) {
			int k = 0;
			for(int i = 0; i < K; i ++) {
				p[++ k] = P[(mask + i) % N];
			}
			res = max(res, DP());
		}
		printf("Case #%d: %.8f\n", cas, res);
	}
	return 0;
}

