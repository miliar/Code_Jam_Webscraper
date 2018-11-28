// Author: Chi-Kit (George) LAM
#include <cstdio>
#include <cinttypes>
#include <cstring>
#include <algorithm>
using namespace std;
bool h[2501];
void solve(int T) {
  int N;
  scanf("%d\n", &N);
  for (int k=1; k<=2500; ++k) {
    h[k] = false;
  }
  for(int i=0; i<2*N-1; ++i) {
    for (int j=0; j<N; ++j) {
      int k;
      scanf("%d", &k);
      h[k] = !h[k];
    }
  }
  printf("Case #%d:", T);
  for (int k=1; k<=2500; ++k) {
    if(h[k]) {
      printf(" %d", k);
    }
  }
  printf("\n");
  return;
}
int main(){
  int T;
  scanf("%d\n", &T);
  for (int i=0; i<T; ++i) {
    solve(i+1);
  }
  return 0;
}
