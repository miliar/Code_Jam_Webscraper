#include <bits/stdc++.h>

using namespace std;
const int N = 1100;
int n, k;
double p[N], pp[N];
double f[N][N];
int cnt(int x){
  int res = 0;
  while (x){
    x = x & (x - 1);
    res++;
  }
  //printf("%d\n", res);
  return res;
}
int main(){
  freopen("out", "w", stdout);
  int t; scanf("%d", &t);
  while(t--){
    static int ca = 0;
    printf("Case #%d: ", ++ ca);
    scanf("%d %d", &n, &k);
    double ans = 0;
    for (int i = 0; i < n; ++ i) scanf("%lf", &pp[i]);
    sort(pp, pp + n);
    for (int m = 0; m <= k; ++ m){
      int tot = 0;
      for (int i = 1; i <= m; ++ i) p[++tot] = pp[i - 1];
      for (int i = 1; i <= k - m; ++ i) p[++tot] = pp[n - i];
      f[0][0] = 1;
      for (int i = 1; i <= k; ++ i){
          for (int j = 0; j <= k; ++ j){
            f[i][j] = f[i - 1][j] * (1. - p[i]);
            if (j > 0) f[i][j] += f[i - 1][j - 1] * p[i];
        }
      }
      //printf("%f\n", f[n][k/2]);
      ans = max(ans, f[k][k/2]);
    }
    printf("%.10f\n", ans);
  }
}
