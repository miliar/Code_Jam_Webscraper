#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

#define EPS 1E-9

using namespace std;

double c, f, x;

bool can_win(double secs) {
  double cookies = 0;
  double cps = 2.0;
  double time = 0.0;

  while (time < secs) {
    if (time + (x - cookies) / cps < secs)
      return true;
    time += (c - cookies) / cps;
    cookies = 0;
    cps += f;
  }

  return false;
}

double bin_search(double lo, double hi) {
  if (abs(hi - lo) < EPS)
    return hi;
  double mid = lo + (hi - lo) / 2.0;
  if (can_win(mid)) {
    return bin_search(lo, mid);
  } else {
    return bin_search(mid, hi);
  }
}

int main() {
  int ncases;

  cin >> ncases;
  for (int caseno = 1; caseno <= ncases; caseno++) {
    cin >> c >> f >> x;
    double ans = bin_search(0.0, x / 2.0);
    printf("Case #%i: %.7lf\n", caseno, ans);
  }
}
