#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
typedef pair<int,int> pi;
int TC;
int N, K;
double p[300];
double u[300];
double dp[40][40];
int main(){
    scanf("%d", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        scanf("%d %d" , &N, &K); K/=2;
        for(int i = 0; i < N; ++i) scanf("%lf", &p[i]);
        double ans = 0;
        for(int i = 0; i < (1 << N); ++i){
            int c = 0;
            for(int j = 0; j < N; ++j) if(i & (1 << j)) ++c;
            if(c == K*2){
                int c = 0;
                for(int j = 0; j < N; ++j) if(i & (1 << j)){ u[c] = p[j]; ++c; }
                memset(dp, 0, sizeof(dp));
                //for(int i = 0; i < 2*K; ++i) printf("%lf, ", u[i]); printf("\n");
                dp[0][0] = 1;
                for(int i = 1; i <= 2*K; ++i){
                    for(int j = 0; j <= K; ++j){
                        if(j > 0) dp[i][j] = dp[i-1][j-1]*u[i-1] + dp[i-1][j] * (1. - u[i-1]);
                        else dp[i][j] = dp[i-1][j] * (1. - u[i-1]);
                    }
                }
                ans = max(ans, dp[2*K][K]);
            }
        }
        printf("Case #%d: %.6lf\n", tc, ans);
    }
}
        
