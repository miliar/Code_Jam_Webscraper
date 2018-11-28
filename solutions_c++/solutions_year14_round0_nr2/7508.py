#include<vector>
#include<cstdio>
#include<iostream>

using namespace std;

int T;
long double C,F,X;

int main() {
  scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    scanf("%LF", &C);
    scanf("%LF", &F);
    scanf("%LF", &X);
    long double best = X;
    long double r = 0;
    for(int f=0; f < 500000; ++f) {
      best = min(best, X / (f * F + 2) + r);
      r += C / (f * F + 2);
    }
    printf("Case #%d: %.10LF\n", t, best);
  }
  return 0;
}
