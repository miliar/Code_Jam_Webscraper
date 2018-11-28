#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const double eps = 1e-9;

inline bool lt (double a, double b) { return a + eps < b; }
inline double Min (double a, double b) { return lt(a, b) ? a : b; }

void solve (int tc) {
  double C, F, X;
  scanf("%lf %lf %lf",&C,&F,&X);

  double ret = X / 2.0;
  double I = 2, curr_t = 0, money = 0;

  for (int iter = 0; iter <= 1000000; ++iter) {
    double to_next = C / I;
    curr_t += to_next;
    money += to_next * I;
    I += F;
    money -= C;
    
    if (lt(X, money))
      ret = Min(ret, curr_t);
    else
      ret = Min(ret, curr_t + (X - money) / I);
  }

  printf("Case #%d: %.7lf\n",tc,ret);
}

int main (void) {
  int t;
  scanf("%d",&t);
  for (int c = 1; c <= t; ++c)
    solve(c);
  return 0;
}
