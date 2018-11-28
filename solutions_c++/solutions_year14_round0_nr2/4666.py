#include <iostream>
#include <stdio.h>

void solve() {
  int T, t;
  double C, F, X, res;

  std::cin >> T;
  for (int i = 0; i < T; ++i) {
    std::cin >> C >> F >> X;
    t = int((X / C) - 2 / F - 1) + 1;
    if (t <= 0) {
      t = 0;
    } else {
      while ((t > 0) && (X / (t * F + 2) >= (X - C) / (t * F - F + 2))) {
        --t;
      }
    }
    res = 0;
    for (int j = 0; j < t; ++j) {
      res += C / (j * F + 2);
    }
    res += X / (t * F + 2);
    printf("Case #%d: %.7f\n", i + 1, res);
  }
}

int main(int argc, char *argv[]) {
  solve();
  return 0;
}
