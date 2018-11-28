#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int N = 100 + 10;
char s[N];
int dp[N][2];

int doit(int n)
{
	dp[0][0] = dp[0][1] = 0;
	for (int i = 1; i <= n; i++) {
		if (s[i] == '-') {
			dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + 1);
			dp[i][1] = dp[i][0] + 1;
		} else {
			dp[i][1] = min(dp[i - 1][0] + 1, dp[i - 1][1]);
			dp[i][0] = dp[i][1] + 1 ;
		}
	}
	return dp[n][1];
}

int main(int argc, char *argv[])
{

	if (argc == 2) {
		freopen(argv[1], "r", stdin);
	} else if (argc == 3) {
		freopen(argv[1], "r", stdin);
		freopen(argv[2], "w", stdout);
	}

	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++cas);
		scanf("%s", s + 1);
		printf("%d\n", doit(strlen(s + 1)));
	}
	return 0;
}