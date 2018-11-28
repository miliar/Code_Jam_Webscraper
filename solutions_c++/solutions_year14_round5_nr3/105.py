#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
using namespace std;
struct node {
	int op, x;
} a[1005];
int dp[20][1 << 15];
int main() {
	int t, cas = 0;
	int n, i, j, k;
	char op[5];
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		for (i = 0; i < n; ++i) {
			scanf("%s", op);
			if (op[0] == 'E')
				a[i].op = 0;
			else
				a[i].op = 1;
			scanf("%d", &a[i].x);
		}
		int inf = 100004;
		for (i = 0; i <= n; ++i) {
			for (j = 0; j < (1 << n); ++j) {
				dp[i][j] = inf;
			}
		}
		dp[0][0] = 0;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < (1 << n); ++j) {
				if (dp[i][j] == inf)
					continue;
				if (a[i].x == 0) {
					if (a[i].op == 0) {
						dp[i + 1][j | (1 << i)] = min(dp[i + 1][j | (1 << i)],
								dp[i][j] + 1);
					} else if (a[i].op == 1) {
						for (k = i - 1; k >= 0; --k) {
							if (j & (1 << k)) {
								if (a[k].op == 0)
									dp[i + 1][j ^ (1 << k)] = min(dp[i + 1][j
											^ (1 << k)], dp[i][j] - 1);
							}
						}
						if (k < 0)
							dp[i + 1][j | (1 << i)] = min(dp[i + 1][j
									| (1 << i)], dp[i][j]);
					}
				} else {
					if (a[i].op == 0) {
						for (k = i - 1; k >= 0; --k) {
							if (j & (1 << k)) {
								if (a[k].op == 0 && a[k].x == a[i].x)
									break;
							}
						}
						if (k < 0)
							dp[i + 1][j | (1 << i)] = min(dp[i + 1][j
									| (1 << i)], dp[i][j] + 1);
					} else if (a[i].op == 1) {
						for (k = i - 1; k >= 0; --k) {
							if (j & (1 << k)) {
								if (a[k].op == 0 && (a[k].x == a[i].x || a[k].x
										== 0))
									dp[i + 1][j ^ (1 << k)] = min(dp[i + 1][j
											^ (1 << k)], dp[i][j] - 1);
							}
							if (a[k].op == 1 && a[k].x == a[i].x)
								break;
						}
						if (k < 0)
							dp[i + 1][j | (1 << i)] = min(dp[i + 1][j
									| (1 << i)], dp[i][j]);
					}
				}
			}
		}
		int ans = inf;
		for (j = 0; j < (1 << n); ++j) {
			ans = min(ans, dp[n][j]);
		}
		if (ans == inf)
			printf("Case #%d: CRIME TIME\n", cas);
		else
			printf("Case #%d: %d\n", cas, ans);
	}
}
