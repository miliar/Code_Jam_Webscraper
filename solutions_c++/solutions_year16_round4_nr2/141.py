#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 205;

int n, k;

double p[N], q[N];

double dp[N][N];

double calc() {
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for (int i = 0; i < k; ++i) {
		for (int j = 0; j <= i; ++j) {
			dp[i + 1][j] += dp[i][j] * (1 - q[i]);
			dp[i + 1][j + 1] += dp[i][j] * q[i];
		}
	}
	return dp[k][k / 2];
}

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		printf("Case #%d: ", ++id);
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i) {
			scanf("%lf", p + i);
		}
		sort(p, p + n);
		double ans = 0;
		for (int i = 0; i <= k; ++i) {
			int top = 0;
			for (int j = 0; j < i; ++j) {
				q[top++] = p[j];
			}
			for (int j = i; j < k; ++j) {
				q[top++] = p[n - (j - i) - 1];
			}
			ans = max(ans, calc());
		}
		printf("%.12f\n", ans);
	}
	return 0;
}
