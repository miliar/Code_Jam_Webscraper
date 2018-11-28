#include"stdio.h"
#include"stdlib.h"
#include"math.h"
#include"algorithm"
using namespace std;

int T, t, i, j, k, n, dp[2][1001], ans;
double naomi[1001], ken[1001];
int main() {
	freopen("2.in", "r", stdin);
	freopen("2.txt", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		for (i = 0; i < 1001; i++) dp[0][i] = dp[1][i] = 0;
		ans = 0;
		scanf("%d", &n);
		for (i = 0; i < n; i++) scanf("%lf", &naomi[i]);
		for (i = 0; i < n; i++) scanf("%lf", &ken[i]);
		sort(naomi, naomi + n);
		sort(ken, ken + n);
		for (i = 0; i < n; i++) {
			k = i % 2;
			dp[k][0] = (naomi[0] > ken[i]);
			for (j = 1; j < n; j++)
				if (naomi[j] > ken[i]) dp[k][j] = dp[!k][j - 1] + 1;
				else dp[k][j] = max(dp[!k][j], dp[k][j - 1]);
		}
		for (i = j = n - 1; i >= 0; i--)
			if (naomi[i] > ken[j]) ans++;
			else j--;
		printf("Case #%d: %d %d\n", t, dp[k][n - 1], ans); /////////
	}
}
/*
5
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458
10
0.00 0.03 0.06 0.09 0.11 0.12 0.15 0.19 0.20 0.25
0.01 0.02 0.05 0.10 0.13 0.14 0.17 0.18 0.22 0.23
*/
