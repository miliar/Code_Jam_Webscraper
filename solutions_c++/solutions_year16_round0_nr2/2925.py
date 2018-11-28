#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

const int inf = 1000000000+10;

const int maxn = 105;
int dp[maxn][maxn][2];
char str[maxn];
int n;

void solve(int tst) {
	char ch[2] = {'-', '+'};
	scanf("%s", str);
	n = strlen(str);
	for (int i = 0; i < n; i ++)
		for (int j = 0; j < n; j ++) 
			for (int k = 0; k < 2; k ++) {
				dp[i][j][k] = inf;
			}
	for (int i = 0; i < n; i ++) {
		dp[i][i][0] = str[i] != ch[0];
		dp[i][i][1] = str[i] != ch[1];
	}
	for (int len = 1; len < n; len ++)
		for (int i = 0; i + len < n; i ++) {
			int j = len + i;
			for (int k = 0; k < 2; k ++) {
				if (i <= j) {
					if (str[j] == ch[k]) {
						dp[i][j][k] = dp[i][j - 1][k];
						continue;
					}	

					bool ok = true;
					for (int m = i; m <= j; m ++) 
						if (str[m] == ch[k]) {
							ok = false;
							break;
						}
					if (ok) {
						dp[i][j][k] = 1;
						continue;
					}

					for (int m = i; m < j; m ++) {
						int now = dp[i][m][!k];
						now += 1;  // flip (i, j)
						now += dp[j][m + 1][!k];
						dp[i][j][k] = min(dp[i][j][k], now);
					}
				} else {
					if (str[j] == ch[k]) {
						dp[i][j][k] = dp[i][j + 1][k];
						continue;
					}

					bool ok = true;
					for (int m = j; m <= i; m ++) {
						if (str[m] == ch[k]) {
							ok = false;
							break;
						}
					}
					if (ok) {
						dp[i][j][k] = 1;
						continue;
					}

					for (int m = j + 1; m <= i; m ++) {
						int now = dp[i][m][!k];
						now += 1;
						now += dp[j][m - 1][!k];
						dp[i][j][k] = min(dp[i][j][k], now);
					}
				}
			}
		}
	printf("Case #%d: %d\n", tst, dp[0][n - 1][1]);
}

int main() {
	int tst;
	scanf("%d", &tst);
	for (int t = 1; t <= tst; t ++) {
		solve(t);
	}
	return 0;
}