#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
using namespace std;
typedef long long i64;

#define MX(P,Q) ((P) = max(P, Q))

int P, Q, N, H[200], G[200];

int dp[2][110][220][1100]; //[which turn][enemy count (died)][HP of last enemy][Anna's pass count]

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 0; t++ < T; ) {
		scanf("%d%d%d", &P, &Q, &N);
		for(int i = 0; i < N; i++) scanf("%d%d", H+i, G+i);

		for(int i = 0; i <= N; i++) {
			for(int j = 0; j <= 200; j++) {
				for(int k = 0; k <= N * 10; k++) dp[0][i][j][k] = dp[1][i][j][k] = -1000000000;
			}
		}
		H[N] = 0;

		dp[1][0][H[0]][0] = 0;
		for(int i = 0; i < N; i++) {
			for(int j = H[i]; j >= 0; j--) {
				for(int k = 0; k <= N * 10; k++) {
					if(dp[0][i][j][k] >= 0) {
						//printf("0 %d %d %d: %d\n", i, j, k, dp[0][i][j][k]);
						//next: Tower's turn
						if(j <= Q) {
							MX(dp[1][i+1][H[i+1]][k], dp[0][i][j][k]);
						}else{
							MX(dp[1][i][j-Q][k], dp[0][i][j][k]);
						}
					}
						//next: Anna's turn
						
					if(dp[1][i][j][k] >= 0) {
						//use pass
						//printf("1 %d %d %d: %d\n", i, j, k, dp[1][i][j][k]);
						if(k > 0) {
							if(j <= P) {
								MX(dp[1][i+1][H[i+1]][k-1], dp[1][i][j][k] + G[i]);
							} else {
								MX(dp[1][i][j-P][k-1], dp[1][i][j][k]);
							}
						}

						if(j <= P) {
							MX(dp[0][i+1][H[i+1]][k], dp[1][i][j][k] + G[i]);
						} else {
							MX(dp[0][i][j-P][k], dp[1][i][j][k]);
						}

						//make pass
						MX(dp[0][i][j][k+1], dp[1][i][j][k]);

						//just ignore
						MX(dp[0][i][j][k], dp[1][i][j][k]);
					}
				}
			}
		}

		int ret = max(dp[1][N][0][0], dp[0][N][0][0]);

		printf("Case #%d: %d\n", t, ret);
	}

	return 0;
}
