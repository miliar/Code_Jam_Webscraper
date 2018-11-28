#include <stdio.h>
#include <algorithm>

double p[201], choose[201];
double dp[201][201];

double DP(int n, int k){
   int now = 0;
   for(int i=0; i<=k; ++i)
      for(int j=0; j<=k; ++j)
         dp[i][j] = 0.0;
   dp[0][0] = 1.0;
   for(int i=1; i<=k; ++i){
      for(int j=0; j<=k; ++j){
         dp[i][j] += dp[i-1][j] * (1.0 - choose[i-1]);
         if(j > 0)
            dp[i][j] += dp[i-1][j-1] * choose[i-1];
      }
   }
   return dp[k][k/2];
}

int main(){
   int T, N, K;
   double ans;
   scanf("%d", &T);
   for(int t=1; t<=T; ++t){
      printf("Case #%d: ", t);
      scanf("%d%d", &N, &K);
      for(int i=0; i<N; ++i)
         scanf("%lf", &p[i]);
      std::sort(p, p+N);
      ans = 0.0;
      for(int i=0; i<=K; ++i){
         for(int j=0; j<i; ++j){
            choose[j] = p[j];
         }
         for(int j=0; j<K-i; ++j){
            choose[i+j] = p[N-K+i+j];
         }
         double prob = DP(N, K);
         if(prob > ans) ans = prob;
      }
      printf("%.7f\n", ans);
   }
   return 0;
}

