//By Lin
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <bitset>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>

#define X first
#define Y second
#define mp make_pair
#define sqr(x) ((x) * (x))
#define Rep(i, n) for(int i = 0; i<(n); i++)
#define foreach(it, n) for(__typeof(n.begin()) it = n.begin(); it != n.end(); it++)

using namespace std;
typedef long long LL;
typedef pair<int, int> pii;

#define esp 1e-8
#define N 1010

int dp[N][20][2100];
int h[110], g[110], P, Q, n;

void check(int &x, int y) {
	if (x == -1 || x < y) x = y;
}
int main() {
	int cas, tt = 0;
	scanf("%d", &cas);
	while (cas --) {
		scanf("%d%d%d", &P, &Q, &n);
		Rep(i, n) scanf("%d%d", &h[i], &g[i]);
		memset(dp, -1, sizeof dp);
		dp[0][0][1] = 0;
		int ans = 0;
		for (int i = 0; i<n; i++) {
			for (int a = 0; a * Q < h[i]; a++)
				for (int b = 0; b < 1200; b++) {
					if (dp[i][a][b] == -1) continue;
					if ((a + 1) * Q < h[i]) 
						check(dp[i][a + 1][b + 1], dp[i][a][b]);
					else
						check(dp[i + 1][0][b + 1], dp[i][a][b]);

					if (b * P + a * Q >= h[i]) {
						int hp = h[i] - a * Q, t;
						if (hp % P == 0) t = hp / P;
						else t = hp / P + 1;
						check(dp[i + 1][0][b - t], dp[i][a][b] + g[i]);
						check(ans, dp[i][a][b] + g[i]);
					}
				}
		}
		printf("Case #%d: %d\n", ++tt, ans);
	}
	return 0;
}
