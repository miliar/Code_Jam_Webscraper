#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;

double dp[300];
int cnt = 0;

void update(double x) {
	for (int i = cnt + 1; i >= 1; --i) {
		dp[i] = dp[i - 1] * x + dp[i] * (1 - x);
	}
	dp[0] = dp[0] * (1 - x);
	++cnt;
}

int main() {
	int T;
	cin >> T;
	for (int nc = 1; nc <= T; ++nc) {
		int N, K;
		cin >> N >> K;
		double p[200];
		for (int i = 0; i < N; ++i) {
			cin >> p[i];
		}
		sort(p, p + N);
		double ans = 0;
		for (int L = 0; L <= K; ++L) {
			int R = K - L;

			memset(dp, 0, sizeof dp);
			cnt = 0;
			dp[0] = 1;
			for (int i = 0; i < L; ++i) {
				update(p[i]);
			}
			for (int i = 0; i < R; ++i) {
				update(p[N - 1 - i]);
			}

			ans = max(ans, dp[K / 2]);
		}

		printf("Case #%d: %0.10lf\n", nc, ans);
	}
	return 0;
}
