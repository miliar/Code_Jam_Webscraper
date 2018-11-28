#include <bits/stdc++.h>
using namespace std;
#define MAXN 205
int T, Cas = 1, N, K;
double P[MAXN];
double dp[MAXN][MAXN][MAXN];
vector<double> vec;

double gao(vector<double> vec) {
	double dp[MAXN][MAXN] = {};
	for (int i = 0; i < vec.size(); i ++) {
		if (i == 0) {
			dp[i][1] = vec[i];
			dp[i][0] = 1.0 - vec[i];
        } else {
        	for (int j = 0; j <= i; j ++) {
        		dp[i][j + 1] += dp[i - 1][j] * vec[i];
        		dp[i][j] += dp[i - 1][j] * (1.0 - vec[i]);
            }
        }
    }
    return dp[vec.size() - 1][K / 2];
}

void small_task() {
	double ans = 0.0;
	for (int i = 0; i < (1 << N); i ++) {
		int cnt = 0;
		for (int j = 0; j < N; j ++) {
			if (i & (1 << j)) {
				cnt ++;
            }
        }
        if (cnt == K) {
        	vec.clear();
        	for (int j = 0; j < N; j ++) {
        		if (i & (1 << j)) {
        			vec.push_back(P[j + 1]);
                }
            }
            double temp = gao(vec);
            ans = max(ans, temp);
        }
    }
    printf("%.12lf\n", ans);
}

void big_task() {
	double ans = 0.0;
    for (int i = 0; i <= K; i ++) {
        vec.clear();
        for (int j = 1; j <= i; j ++) {
        	vec.push_back(P[j]);
        }
        for (int j = 1; j <= K - i; j ++) {
        	vec.push_back(P[N - j + 1]);
        }
        ans = max(ans, gao(vec));
    }
    printf("%.12lf\n", ans);
}

void work() {
	printf("Case #%d: ", Cas ++);
    scanf("%d %d", &N, &K);
    for (int i = 1; i <= N; i ++) {
    	scanf("%lf", &P[i]);
    }
    sort(P + 1, P + 1 + N);
    big_task();
    return ;
    if (N <= 16) {
    	small_task();
    	return ;
    } else {
        return ;
    }
    memset(dp, 0, sizeof(dp));
    dp[1][0][0] = 1.0;
    dp[1][1][1] = P[1];
    dp[1][1][0] = 1.0 - P[1];
    double ans = 0.0;
    for (int i = 2; i <= N; i ++) {
    	for (int j = 0; j <= i; j ++) {
    		if (j == 0) {
    			dp[i][j][0] = 1.0;
            } else {
            	for (int k = 0; k <= j; k ++) {
            		dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k]);
            		if (k > 0) {
            			dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1] * P[i]);
                    } 
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] * (1.0 - P[i]));
                }
            }
            if (j == K) {
            	ans = max(dp[i][j][K / 2], ans);
            }
        }
    }
    cout << ans << endl;
}

int main() {
	scanf("%d", &T);
	while (T --) {
		work();
    }
	return 0;
}
