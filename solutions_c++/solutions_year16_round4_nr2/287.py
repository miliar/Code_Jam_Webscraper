#include <bits/stdc++.h>
using namespace std;

int TC, N, K;
double yp[205];
double dp[205][205];

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N; i++) scanf("%lf", &yp[i]);
		double ans = 0;
		for (int i = 0; i < (1 << N); i++) {
			if (__builtin_popcount(i) != K) continue;
			vector<double> v;
			for (int j = 0; j < N; j++) if (i & (1 << j)) v.push_back(yp[j]);
			for (int j = 0; j <= v.size(); j++) for (int k = 0; k <= K/2; k++) dp[j][k] = 0;
			dp[0][0] = 1;
			for (int j = 1; j <= v.size(); j++) {
				for (int k = 0; k <= K/2; k++) {
					dp[j][k] += dp[j - 1][k] * (1.00 - v[j - 1]);
					if (k > 0) dp[j][k] += dp[j - 1][k - 1] * v[j - 1];
				}
			}
			ans = max(ans, dp[v.size()][K/2]);
		}
		printf("Case #%d: %lf\n", tc, ans);
	}
}
