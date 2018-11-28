#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

bool equal(double a, double b) {
  return fabs(a - b) <= 1E-9;
}

int main() {
  freopen("A-small-attempt1.in", "r", stdin);
  freopen("A-small-attempt1.out", "w", stdout);
  int T, cas = 1;
  double r, t;

  cin >> T;
  while (T--) {
    printf("Case #%d: ", cas++);
    cin >> r >> t;
    double delta = (2 * r - 1) * (2 * r - 1) + 8 * t;
    if (delta >= 0) {
      double ans = ((1 - 2 * r) + sqrt(delta)) / 4;
      long long n = ans;
      double sum = 2 * n * n + (2 * r - 1) * n - t;
      if (!(sum <= 0)) {
        --n;
      }
      cout << n << endl;
    } else {
      fprintf(stderr, "cas = %d\n", cas);
      printf("0\n");
    }
  }
  return 0;
}
