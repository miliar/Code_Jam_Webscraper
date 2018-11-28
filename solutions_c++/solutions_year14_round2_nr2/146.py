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

using namespace std;

__int64 dp[32][2][2][2];
int main() {
	int i, j, k;
	int a, b, r, c;
	int jj, rr, kk;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d%d", &a, &b, &c);
		memset(dp, 0, sizeof(dp));
		dp[30][1][1][1] = 1;
		for (i = 29; i >= 0; --i) {
			for (j = 0; j < 2; ++j) {
				for (k = 0; k < 2; ++k)
					for (r = 0; r < 2; ++r) {
						///////00
						jj = j;
						kk = k;
						rr = r;
						if (a & (1 << i)) {
							jj = 0;
						}
						if (b & (1 << i)) {
							kk = 0;
						}
						if (c & (1 << i))
							rr = 0;
						dp[i][jj][kk][rr] += dp[i + 1][j][k][r];
						///////////////10
						jj = j;
						kk = k;
						rr = r;
						if ((a & (1 << i)) || jj == 0) {
							if (b & (1 << i)) {
								kk = 0;
							}
							if (c & (1 << i))
								rr = 0;
							dp[i][jj][kk][rr] += dp[i + 1][j][k][r];
						}
						/////////////01
						jj = j;
						kk = k;
						rr = r;
						if ((b & (1 << i)) || kk == 0) {
							if (a & (1 << i)) {
								jj = 0;
							}
							if (c & (1 << i))
								rr = 0;
							dp[i][jj][kk][rr] += dp[i + 1][j][k][r];
						}
						/////////////11
						jj = j;
						kk = k;
						rr = r;
						if ((a & (1 << i)) || j == 0) {
							if ((b & (1 << i)) || k == 0) {
								if ((c & (1 << i)) || rr == 0)
									dp[i][jj][kk][rr] += dp[i + 1][j][k][r];
							}
						}
					}
			}
		}
		printf("Case #%d: %I64d\n", cas, dp[0][0][0][0]);
	}
}
