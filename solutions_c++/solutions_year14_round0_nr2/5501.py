#define NDEBUG
#include <cstdio>
#include <ctime>
#include <iostream>
using namespace std;


long double eval(long double C, long double F, long double X, int nfarms) {
  long double time = 0;
  for (int i=0; i<nfarms; ++i) {
    time += C / (2.0 + i * F);
  }
  time += X / (2.0 + nfarms * F);
  // fprintf(stderr, "eval(nfarms=%d) = %.12Lf\n", nfarms, time);
  return time;
}

long double solve1() {
  long double C, F, X;
  cin >> C >> F >> X;
  int lo = 0, hi = 1;
  while (1) {
    hi *= 2;
    if (eval(C, F, X, hi) > eval(C, F, X, hi/2)) {
      break;
    }
  }
  fprintf(stderr, "hi = %d\n", hi);

  while (lo < hi) {
    int mid = (lo + hi) / 2;
    if (eval(C, F, X, mid) < eval(C, F, X, mid+1)) {
      hi = mid;
    } else {
      lo = mid + 1;
    }
  }
  return eval(C, F, X, lo);
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: %.7Lf\n", tt, solve1());
  }
}
