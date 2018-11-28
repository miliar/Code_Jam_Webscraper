#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

double p[210];
vector<double> ps;

double dp[210][210]; // total, yes

double res(){
  int N = (int)ps.size();

  dp[0][0] = 1.0;

  for(int i = 1; i <= N; i++){
    for(int j = 0; j <= i; j++){
      dp[i][j] = 0.0;
      if(j > 0) dp[i][j] += dp[i - 1][j - 1] * ps[i - 1];
      dp[i][j] += dp[i - 1][j] * (1.0 - ps[i - 1]);
    }
  }

  return dp[N][N / 2];
}

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    int N, K; scanf("%d%d", &N, &K);
    for(int i = 0; i < N; i++) scanf("%lf", &p[i]);

    sort(p, p + N);

    double ans = 0.0;

    for(int es = 0; es < N; es++){
      int ee = es + (N - K) - 1;
      if(ee == N) break;

      ps.clear();
      for(int i = 0; i < N; i++) if(i < es || i > ee) ps.push_back(p[i]);

      // for(double x : ps) printf("%.2lf ", x);

      double r = res();

      // printf("%.5lf\n", r);

      if(r > ans) ans = r;
    }

    printf("Case #%d: %.10lf\n", tt, ans);
  }
  return 0;
}
