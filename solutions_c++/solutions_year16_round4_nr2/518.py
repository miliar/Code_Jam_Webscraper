#include<stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;
double a[205];
double b[205];
double dp[205][500];
double gao(int n) {
	int i, j, k;
	for (i = 0; i <= n; ++i) {
		for (j = 0; j < 500; ++j) {
			dp[i][j] = 0;
		}
	}
	dp[0][0] = 1;
	for (i = 0; i < n; ++i) {
		for (j = -i; j <= i; ++j) {
			dp[i + 1][j + 1] += dp[i][j] * b[i];
			dp[i + 1][j - 1] += dp[i][j] * (1 - b[i]);
		}
	}
	return dp[n][0];
}
int main() {
	int t, cas = 0;
	int n, k;
	int i, j;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d", &n, &k);
		for (i = 0; i < n; ++i) {
			scanf("%lf", &a[i]);
		}
		sort(a, a + n);
		double ans = 0;
		for (i = 0; i <= k; ++i) {
			for (j = 0; j < i; ++j) {
				b[j] = a[j];
			}
			for (j = i; j < k; ++j) {
				b[j] = a[n - (k - j)];
			}
			double tmp = gao(k);
			if (ans < tmp)
				ans = tmp;
		}
		printf("Case #%d: %.12lf\n", cas, ans);
	}
}
