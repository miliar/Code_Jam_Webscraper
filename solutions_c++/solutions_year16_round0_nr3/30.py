// Author: Chi-Kit (George) LAM
#include <cstdio>
#include <cinttypes>
#include <cstdlib>
#include <set>
#include <algorithm>
using namespace std;
int T;
int nump = 25;
int p[25] = {2, 3, 5, 7, 11, 13, 17, 19, 23,
  29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
  73, 79, 83, 89, 97};
int factor(int64_t x, int b) {
  for (int i=0; i<nump; ++i) {
    int64_t rem=0;
    for (int64_t y=x; y!=0; y/=2) {
      rem = (rem*b + (y%2)) % p[i];
    }
    if (rem == 0) {
      return p[i];
    }
  }
  return 0;
}
void solve(int T) {
  set<int64_t> S;
  int N, J;
  scanf("%d %d\n", &N, &J);
  printf("Case #%d:\n", T);
  while(S.size() < J) {
    int64_t x = 1;
    for (int i=1; i<=N-2; ++i) {
      x = x*2 + (rand() % 2);
    }
    x = x*2+1;
    if (S.find(x) != S.end()) {
      continue;
    }
    bool flag = true;
    for (int b=2; b<=10; ++b) {
      if (factor(x, b) == 0) {
        flag = false;
      }
    }
    if (flag) {
      S.insert(x);
    }
  }
  for (int64_t x : S) {
    for (int64_t y=x; y!=0; y/=2) {
      printf("%d", y%2);
    }
    for (int b=2; b<=10; ++b) {
      printf(" %d", factor(x,b));
    }
    printf("\n");
  }
  return;
}
int main(){
  srand(0);
  scanf("%d\n", &T);
  for (int i=1; i<=T; ++i) {
    solve(i);
  }
  return 0;
}
