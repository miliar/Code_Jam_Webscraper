#include <bits/stdc++.h>
#define REP(i, n) for(int i = 0;i < n;++i)
using namespace std;
const int INF = 1e9;
const int MAX = 200;
int a[MAX];
int dp[2][MAX];
char in[MAX];
int n;

int solve () {
	dp[0][0] = a[0];
	dp[1][0] = !a[0];
	for(int i = 1;i < n;++i) {
		if(a[i]) {
			dp[1][i] = min(dp[1][i - 1], dp[0][i - 1] + 1);
			dp[0][i] = min(dp[1][i - 1] + 1, dp[0][i - 1] + 3);
		}
		else {
			dp[0][i] = min(dp[0][i - 1], dp[1][i - 1] + 1);
			dp[1][i] = min(dp[0][i - 1] + 1, dp[1][i - 1] + 3);
		}
	}
	return dp[1][n - 1];
}

int main () {
	int t;
	scanf("%d", &t);
	REP(i, t) {
		scanf("%s", in);
		n = strlen(in);
		printf("Case #%d: ", i + 1);
		REP(j, n) a[j] = in[j] == '+' ? 1 : 0;
		printf("%d\n", solve());
	}
}
