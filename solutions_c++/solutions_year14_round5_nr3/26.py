#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
#include <map>
using namespace std;

int dp[35][1 << 15];
char buf[1005][5];
int id[1005];
int cost[1 << 15];

void Solve() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> buf[i] >> id[i];
	}
	for (int i = 1; i < (1 << n); ++i) {
		char buf[15] = {};
		int q = 0, rid = -1, cost = 0;
		for (int j = 0; j < n; ++j) {
			if (i & (1 << j)) {
				if (rid != -1 && id[j] != 0 && rid != id[j]) {
					cost = -1;
				} else {
					rid = id[j] ? id[j] : rid;
					buf[q++] = ::buf[j][0];
				}
			}
		}
		if (rid != -1) {
			for (int j = 0; j < n; ++j) {
				if (id[j] == rid && !((1 << j) & i)) {
					cost = -1;
				}
			}
		}
		char c = 0;
		for (int j = 0; j < q; ++j) {
			if (buf[j] == c) {
				cost = -1;
			}
			c = buf[j];
		}
		if (cost != -1 && c == 'E') {
			cost = 1;
		}
		::cost[i] = cost;
	}
	memset(dp, 0x7f, sizeof dp);
	dp[0][(1 << n) - 1] = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < (1 << n); ++j) {
			for (int k = j; k > 0; k = (k - 1) & j) {
				if (cost[k] == -1) {
					continue;
				}
				dp[i + 1][j ^ k] = min(dp[i + 1][j ^ k], dp[i][j] + cost[k]);
			}
		}
		dp[i + 1][0] = min(dp[i + 1][0], dp[i][0]);
	}
	if (dp[n][0] != 0x7f7f7f7f) {
		printf("%d\n", dp[n][0]);
	} else {
		puts("CRIME TIME");
	}
}


int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}