#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

#define mp(a,b) make_pair(a,b)

int arr[105];
int g[105];
int dp[105][1005];

void Solve() {
	int n, p, q;
	cin >> p >> q >> n;
	for (int i = 0; i < n; ++i) {
		cin >> arr[i] >> g[i];
	}
	memset(dp, -1, sizeof dp);
	dp[0][1] = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < 1005; ++j) {
			if (dp[i][j] == -1) {
				continue;
			}
			for (int shots = 0; shots * q < arr[i]; ++shots) {
				if (arr[i] - shots * q <= p * (j + shots)) {
					int to = j + shots - (arr[i] - shots * q + p - 1) / p;
					dp[i + 1][to] = max(dp[i + 1][to], dp[i][j] + g[i]);
				}
			}
			int shots = (arr[i] + q - 1) / q;
			dp[i + 1][j + shots] = max(dp[i + 1][j + shots], dp[i][j]);
		}
	}
	int ret = 0;
	for (int i = 0; i < 1005; ++i) {
		ret = max(ret, dp[n][i]);
	}
	printf("%d\n", ret);
}

int main() {
	freopen("b_large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}