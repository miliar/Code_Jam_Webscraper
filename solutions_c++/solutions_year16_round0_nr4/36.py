// Author: Chi-Kit (George) LAM
#include <cstdio>
#include <cinttypes>
#include <algorithm>
using namespace std;
int T;
int64_t X[101];
void solve(int T) {
  int K, C, S;
  scanf("%d %d %d\n", &K, &C, &S);
  printf("Case #%d:", T);
  if (K > S * C) {
    printf(" IMPOSSIBLE");
  } else {
    int64_t max = 0;
    for (int i=0; i<S; ++i) {
      int64_t x = min(i*C+1,K);
      for (int j=i*C+2; j<=i*C+C; ++j) {
        x = (x-1)*K + min(j, K);
      }
      if (x > max) {
        printf(" %" PRId64, x);
        max = x;
      }
    }
  }
  printf("\n");
  return;
}
int main(){
  scanf("%d\n", &T);
  for (int i=1; i<=T; ++i) {
    solve(i);
  }
  return 0;
}
