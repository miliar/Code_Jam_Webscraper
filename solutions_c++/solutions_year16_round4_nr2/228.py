#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;
double p[205], pc[205], dp[205][205];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int _, cas = 1;
	scanf("%d", &_);
	while (_--) {
		printf("Case #%d: ", cas);
		++cas;

		int n, K;
		scanf("%d%d", &n, &K);
		for (int i = 0; i < n; ++i) {
			cin >> p[i];
		}
		sort(p, p + n);
		double ans = 0;
		for (int l = 0; l <= K; ++l) {
			int r = K - l;
			for (int k = 0; k < l; ++k) {
				pc[k + 1] = p[k];
			}
			for (int k = 0; k < r; ++k) {
				pc[l + k + 1] = p[n - k - 1];
			}
			memset(dp[0], 0, sizeof(dp[0]));
			dp[0][0] = 1;
			for (int i = 1; i <= K; ++i) {
				dp[i][0] = (1 - pc[i]) * dp[i - 1][0];
				for (int j = 1; j <= i; ++j) {
					dp[i][j] = pc[i] * dp[i - 1][j - 1] + (1 - pc[i]) * dp[i - 1][j];
				}
			}
			ans = max(ans, dp[K][K / 2]);
		}
		printf("%.8f\n", ans);
	}
	return 0;
}