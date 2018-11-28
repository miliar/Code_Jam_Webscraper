#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

double seconds(double c, double f, double x) {
  if (x < c) {
    return x/2;
  }

  double inc = 2, sum = 0;
  double res = 0;


  while (sum < x) {
    if (sum < c) {
      res += c / inc;
      sum = c;
    }

    if ((x-c) / inc > x / (inc+f)) {
      sum = 0;
      inc += f;
    } else {
      res += (x-c) / inc;
      break;
    }
  }

  return res;
}

int main() {
  int T;
  double C, F, X;
  cin >> T;

  for (int i = 1; i <= T; ++i) {
    cin >> C >> F >> X;
    printf("Case #%d: %.7lf\n", i, seconds(C, F, X));
  }
  return 0;
}
