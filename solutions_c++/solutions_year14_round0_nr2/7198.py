#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

const double EPS = 1e-9;
double C, F, X;

void input() {
  cin >> C >> F >> X;
}

bool equal( double a, double b ) {
  return fabs(a - b) < EPS;
}

bool less_than_equal( double a, double b ) {
  return equal(a, b) || a < b;
}

double solve() {
  double res = X / 2.0;
  double t = 0.0;
  double sum = 0.0;
  double v = 2;
  while ( less_than_equal(t, res) ) {
    // cout << "v = " << v << ", t = " << t <<  ", time = " << C / v << ", res = " << ( t + X / v ) << endl;
    res = min(res, t + X / v);
    t += C / v;
    //X += C;
    v += F;
  }
  return res;
}

int main() {
  int tests;
  cin >> tests;
  for ( int i = 0; i < tests; ++ i ) {
    input();
    printf("Case #%d: %.12f\n", i + 1, solve());
  }
  return 0;
}

