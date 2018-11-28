#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>
#include <numeric>

using namespace std;

const int MAXN = 201;

double dp[MAXN][MAXN], a[MAXN];

int main() {
	int task;
	scanf("%d", &task);
	for (int index = 1; index <= task; ++ index) {
		int n, m;
		scanf("%d %d", &n, &m);
		m /= 2;
		for (int i = 0; i < n; ++ i) {
			scanf("%lf", a + i);
		}
		sort(a, a + n);
		double ans = 0.0;
		for (int k = 0; k <= m + m; ++ k) {
			dp[0][0] = 1.0;
			for (int i = 1; i <= m + m; ++ i) {
				double p = i <= k ? a[i - 1] : a[n - i + k];
				for (int j = 0; j <= min(m, i); ++ j) {
					double py = j == 0 ? 0.0 : dp[i - 1][j - 1] * p;
					double pn = dp[i - 1][j] * (1.0 - p);
					dp[i][j] = py + pn;
				}
			}
			ans = max(ans, dp[m + m][m]);
		}
		printf("Case #%d: %.8f\n", index, ans);
	}
	return 0;
}

