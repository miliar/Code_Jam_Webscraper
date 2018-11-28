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

int ot[105];
int mt[105], md[105];
int dp[105][2005];
int point[105];
int main() {
	int t, cas = 0;
	int p, q, i, j, n, x;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d%d", &p, &q, &n);
		for (i = 0; i < n; ++i) {
			scanf("%d", &x);
			scanf("%d", &point[i]);
			ot[i] = (x + q - 1) / q;
			mt[i] = ot[i] - 1;
			md[i] = (x - mt[i] * q + p - 1) / p;
		}
		memset(dp, -1, sizeof(dp));
		dp[0][1] = 0;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < 2005; ++j) {
				if (dp[i][j] == -1)
					continue;
				//Ñ¡i
				int jj = j + mt[i] - md[i];
				if (jj >= 2005)
					jj = 2004;
				if (jj >= 0) {
					dp[i + 1][jj] = max(dp[i + 1][jj], dp[i][j] + point[i]);
				}
				//²»Ñ¡i
				jj = j + ot[i];
				if (jj >= 2005)
					jj = 2004;
				if (jj >= 0) {
					dp[i + 1][jj] = max(dp[i + 1][jj], dp[i][j]);
				}
			}
		}
		int ans = 0;
		for (j = 0; j < 2005; ++j)
			ans = max(ans, dp[n][j]);
		printf("Case #%d: %d\n", cas, ans);
	}
}
