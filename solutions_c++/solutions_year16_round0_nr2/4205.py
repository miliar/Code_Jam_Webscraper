#include <bits/stdc++.h>

using namespace std;

int dp[2][111];
char s[111];

void solve() {
	memset(dp, 0, sizeof dp);
	scanf("%s", s);
//	printf("%s\n", s);
	dp[0][0] = (s[0] != '-');
	dp[1][0] = (s[0] != '+');
	int n = strlen(s);
	for(int i = 1; i < n; ++i) 
	if (s[i] == '+'){
		dp[1][i] = min(dp[1][i - 1], dp[0][i - 1] + 1);
		dp[0][i] = min(dp[1][i - 1] + 1, dp[0][i - 1] + 2);
	}
	else {
		dp[1][i] = min(dp[1][i - 1] + 2, dp[0][i - 1] + 1);
		dp[0][i] = min(dp[1][i - 1] + 1, dp[0][i - 1]);
	}
//	for(int i = 0; i < n; ++i)
//		printf("%c %d %d\n", s[i], dp[0][i], dp[1][i]);
	printf("%d\n", dp[1][n - 1]);
}

int main() {
	int ntest;
	scanf("%d\n", &ntest);
	for(int tc = 1; tc <= ntest; ++tc) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}