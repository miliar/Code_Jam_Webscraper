#include <bits/stdc++.h>

using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back

int dp[200][3];
int N, T;
char str[200];

void openFile() {
	freopen("in.inp", "r", stdin);
	freopen("ou.out", "w", stdout);
}

int main(int argc, char **argv) {
	openFile();
	scanf("%d", &T);
	for (int itest = 0; itest < T; ++itest) {
		memset(dp, 0, sizeof dp);
		scanf("%s", str + 1);
		N = strlen(str + 1);
		dp[1][0] = (str[1] != '-');
		dp[1][1] = (str[1] != '+');
		for (int i = 2; i <= N; ++i)
			if (str[i] == '-') {
				dp[i][0] = dp[i - 1][0];
				dp[i][1] = 1E9;
				for (int j = i; j >= 1 && str[j] == '-'; --j) {
					dp[i][1] = min(dp[j - 1][1] + 3, dp[i][1]);
					dp[i][1] = min(dp[j - 1][0] + 1, dp[i][1]);
				}
			} else {
				dp[i][1] = dp[i - 1][1];
				dp[i][0] = 1E9;
				for (int j = i; j >= 1 && str[j] == '+'; --j) {
					dp[i][0] = min(dp[j - 1][0] + 3, dp[i][0]);
					dp[i][0] = min(dp[j - 1][1] + 1, dp[i][0]);
				}
			}

		printf("Case #%d: %d\n", itest + 1, dp[N][1]);
	}
	return 0;
}
