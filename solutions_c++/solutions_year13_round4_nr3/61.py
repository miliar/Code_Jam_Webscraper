#include <iostream>
#include <cstdio>

#define MAX_N 2005

using namespace std;

int tests;
int n, a[MAX_N], b[MAX_N];
int tmp1, tmp2;
int answer[MAX_N];
int dp[MAX_N][MAX_N][2];
bool chk, chk2;

void recur(int r) {
	if (r == n + 1) {
		//printf("XXX");
		chk = true;
		return;
	} else if (!chk) {
		for (int i = 0 ; i < n ; i ++) {
			if (answer[i] == 0) {
				for (int j = 0 ; j < n ; j ++) {
					dp[r][j][0] = dp[r - 1][j][0];
					dp[r][j][1] = dp[r - 1][j][1];
				}
				for (int k = 0 ; k < n ; k ++) {
					if (answer[k] != 0) {
						if (k < i) dp[r][i][0] = max(dp[r][k][0], dp[r][i][0]);
						else dp[r][i][1] = max(dp[r][k][1], dp[r][i][1]);
					}
				}
				dp[r][i][0] ++;
				dp[r][i][1] ++;
				//printf("%d %d : %d %d\n", i, r, dp[r][i][0], dp[r][i][1]);
				if (dp[r][i][0] == a[i] && dp[r][i][1] == b[i]) {
					chk2 = true;
					for (int k = 0 ; k < n ; k ++) {
						if (answer[k] == 0 && k != i) {
							if (k < i && b[k] <= dp[r][i][1]) {
								chk2 = false;
								break;
							} else if (k > i && a[k] <= dp[r][i][0]) {
								chk2 = false;
								break;
							}
						}
					}
					if (chk2) {
						//printf("%d %d\n", i, r);
						answer[i] = r;
						recur(r + 1);
						if (chk) return;
						answer[i] = 0;
					}
				}
			}
		}
	}
}

int main() {
	scanf("%d", &tests);
	for (int test = 0 ; test < tests ; test ++) {
		printf("Case #%d: ", test + 1);
		scanf("%d", &n);
		for (int i = 0 ; i < n ; i ++) {
			scanf("%d", &a[i]);
		}
		for (int i = 0 ; i < n ; i ++) {
			scanf("%d", &b[i]);
		}
		for (int i = 0 ; i < n ; i ++) {
			answer[i] = 0;
			if (a[i] == 1 and b[i] == 1) answer[i] = 1;
		}
		for (int i = 0 ; i < n ; i ++) {
			dp[1][i][0] = 0;
			dp[1][i][1] = 0;
			if (a[i] == 1 and b[i] == 1) {
				dp[1][i][0] = 1;
				dp[1][i][1] = 1;
			}
		}
		chk = false;
		recur(2);
		for (int i = 0 ; i < n ; i ++) {
			if (i != 0) printf(" ");
			printf("%d", answer[i]);
		}
		printf("\n");
	}
	return 0;
}