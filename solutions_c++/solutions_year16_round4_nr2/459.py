#include<stdio.h>
#include<algorithm>
#include<memory.h>
double d[205][205];
double pk[205];

double prob[205];

double ansp[205];

int T, K, N;
double solve() {
  memset(d, 0, sizeof(d));
  d[0][0] = 1;
  for(int i = 0; i < K; i++) {
    for(int j = 0; j <= i; j++) {
      d[i+1][j+1] += d[i][j] * pk[i+1];
      d[i+1][j] += d[i][j] * (1 - pk[i+1]);
    }
  }
  return d[K][K>>1];
}


int main()
{
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    scanf("%d %d", &N, &K);
    for(int i = 1; i <= N; i++) {
      scanf("%lf", &prob[i]);
    }

    double ans = 0;

    std::sort(prob+1, prob+N+1);

    for(int i = 0; i <= K; i++) {
      for(int j = 1; j <= i; j++) pk[j] = prob[j];
      for(int j = N, c = i + 1; c <= K; j--, c++) pk[c] = prob[j];
      double t = solve();
      if ( ans < t){
        ans = t;
        memcpy(ansp, pk, sizeof(ansp));
      }
    }

    printf("Case #%d: %.6f\n", t, ans);
//    for(int i = 1; i <= K; i++) printf("%.2lf ", ansp[i]);
//    printf("\n");

  }
}
