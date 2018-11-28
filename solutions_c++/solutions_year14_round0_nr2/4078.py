#include <iostream>
#include <cmath>

using namespace std;

double C, F, X;

double compute_time(int k) {
  double sum = 0;
  for (int i = 0; i < k; i++) {
    sum += 1.0 / (2.0 + i * F);
  }
  return X / (2.0 + k * F) + C * sum;
}

double search(int lo, int hi) {
  int diff = hi - lo;
  if (diff <= 2) {
    int ret = lo;
    double min_time = compute_time(lo);
    for (int k = lo + 1; k <= hi; k++) {
      double t = compute_time(k);
      if (t < min_time) {
        min_time = t;
        ret = k;
      }
    }
    return ret;
  }

  int m1 = (2 * lo + hi) / 3;
  int m2 = (lo + 2 * hi) / 3;

  if (compute_time(m1) > compute_time(m2)) {
    return search(m1, hi);
  }
  else {
    return search(lo, m2);
  }
}

int main() {

  int T; cin >> T;
  for (int test = 1; test <= T; test++) {
    cin >> C >> F >> X;

    int hi = X / C;
    int k = search(0, hi);
    double min_time = compute_time(k);

    printf("Case #%d: %.7lf\n", test, min_time);
  }
}
