#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;

#define INF 1000000
#define MaxN 110

int T;
char s[MaxN];
int n;
int dp[MaxN][MaxN][2][2];

int main()
{
	scanf("%d",&T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ",t);

		scanf("%s",s);
		n = strlen(s);

		for (int i = 0; i < n; ++i) {
			dp[i][i][0][0] = s[i] == '+';
			dp[i][i][0][1] = s[i] == '-';
			dp[i][i][1][0] = s[i] == '-';
			dp[i][i][1][1] = s[i] == '+';
		}

		for (int len = 1; len < n; ++len) {
			for (int i = 0; i + len < n; ++i) {
				int j = i + len;

				// flip == 0 && sign == 0
				if (s[j] == '-') dp[i][j][0][0] = dp[i][j-1][0][0];
				else {
					dp[i][j][0][0] = INF;
					for (int k = i; k < j; ++k) {
						dp[i][j][0][0] = min(dp[i][j][0][0], dp[i][k][0][1] + 1 + dp[k+1][j][1][0]);
					}
				}

				// flip == 0 && sign == 1
				if (s[j] == '+') dp[i][j][0][1] = dp[i][j-1][0][1];
				else {
					dp[i][j][0][1] = INF;
					for (int k = i; k < j; ++k) {
						dp[i][j][0][1] = min(dp[i][j][0][1], dp[i][k][0][0] + 1 + dp[k+1][j][1][1]);
					}
				}

				// flip == 1 && sign == 0
				if (s[i] == '+') dp[i][j][1][0] = dp[i+1][j][1][0];
				else {
					dp[i][j][1][0] = INF;
					for (int k = j; k > i; --k) {
						dp[i][j][1][0] = min(dp[i][j][1][0], dp[k][j][1][1] + 1 + dp[i][k-1][0][0]);
					}
				}

				// flip == 1 && sign == 1
				if (s[i] == '-') dp[i][j][1][1] = dp[i+1][j][1][1];
				else {
					dp[i][j][1][1] = INF;
					for (int k = j; k > i; --k) {
						dp[i][j][1][1] = min(dp[i][j][1][1], dp[k][j][1][0] + 1 + dp[i][k-1][0][1]);
					}
				}

				// all flip
				dp[i][j][0][0] = min(dp[i][j][0][0], dp[i][j][0][1] + 1);
				dp[i][j][0][1] = min(dp[i][j][0][1], dp[i][j][0][0] + 1);
				dp[i][j][1][0] = min(dp[i][j][1][0], dp[i][j][1][1] + 1);
				dp[i][j][1][1] = min(dp[i][j][1][1], dp[i][j][1][0] + 1);

				// printf("****** %d => %d *******\n",i+1,j+1);
				// printf("no-flipped - => %d\n",dp[i][j][0][0]);
				// printf("no-flipped + => %d\n",dp[i][j][0][1]);
				// printf("flipped - => %d\n",dp[i][j][1][0]);
				// printf("flipped + => %d\n",dp[i][j][1][1]);
				// printf("\n");
			}
		}

		printf("%d\n",dp[0][n-1][0][1]);
	}

	return 0;
}