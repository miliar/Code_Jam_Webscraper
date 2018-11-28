#include <map>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#define MAXN (1 << 10)
using namespace std;

int n;
int a[MAXN];
int dp[MAXN][MAXN];
map<int, int> bigger;
map<int, int> pos;

inline void solve() {
	pos.clear();
	bigger.clear();
	memset(dp, -1, sizeof dp);
	for (int i=0; i < n; ++i) pos[a[i]] = i;
	for (int i=0; i < n; ++i) {
		for (int j=0; j < i; ++j)
			if (a[i] < a[j])
				bigger[ a[i] ] ++;
	}

	sort(a, a+n);
	dp[0][n-1] = 0;

	for (int dif=n-1; dif >= 0; --dif) {
		for (int l=0; l+dif < n; ++l) {
			int r = l+dif;

			// move to left
			int &Left = dp[l+1][r];
			int costleft = bigger[ a[n-1-dif] ];
			if (Left == -1 || Left > dp[l][r] + costleft) {
				Left = dp[l][r] + costleft;
			}
			// move to right
			int &Right = dp[l][r-1];
			int costright = dif-costleft;
			if (Right == -1 || Right > dp[l][r] + costright) {
				Right = dp[l][r] + costright;
			}
		}
	}

/*	for (int i=0; i < n; ++i)
		for (int j=0; j < n; ++j)
			printf("%d%c", dp[i][j], (j+1 == n)? '\n' : ' ');*/

	int ans = dp[0][0];
	for (int i=0; i < n; ++i)
		ans = min(ans, dp[i][i]);
	printf("%d\n", ans);
}

inline void read() {
	scanf("%d", &n);

	for (int i=0; i < n; ++i)
		scanf("%d", &a[i]);
}

int main() {
	int brt;
	scanf("%d", &brt);

	for (int test=0; test < brt; ++test) {
		printf("Case #%d: ", test+1);
		read();
		solve();
	}
	return 0;
}