#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <map>
using namespace std;
double dp[210][210];
double dp2[210][210];
double p[210];
int N, K;
double v[210];
void DP() {
    for(int i = 0; i <= K; i++) {
        for(int j = 0; j <= K; j++) {
            dp[i][j] = 0;
        }
    }
    dp[0][0] = 1;
    for(int i = 1; i <= K; i++) {
        for(int j = 0; j <= i; j++) {
            dp[i][j] = dp[i - 1][j] * (1 - v[i]);
            if(j > 0) {
                dp[i][j] += dp[i - 1][j - 1] * v[i];
            }
        }
    }
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas = 0;
	int T = 0;
	scanf("%d", &T);
	while(T--) {
		printf("Case #%d: ", ++cas);
		scanf("%d%d", &N, &K);
		for(int i = 1; i <= N; i++) {
			scanf("%lf", &p[i]);
		}
		sort(p + 1, p + 1 + N);
		double ans = 0;

		for(int i = 0; i <= K; i++) {
            double tmp = 0;
            int cnt = 0;
            for(int j = 1; j <= i; j++){
                v[++cnt] = p[j];
            }
            for(int j = N; j > N - (K - i); j--){
                v[++cnt] = p[j];
            }
            DP();
            ans = max(ans, dp[K][K/2]);
		}
		printf("%.8f\n", ans);

	}
}
