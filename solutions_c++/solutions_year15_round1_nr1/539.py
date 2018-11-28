#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

int T, N;
int m[1000];

int main() {
  std::cin >> T;

  int m1, m2, rate, res1;
  for (int n_case = 1; n_case <= T; n_case++) {
    std::cin >> N >> m[0];
    rate = 0;
    res1 = 0;

    for (int i = 1; i < N; i++) {
      std::cin >> m[i];
      if (m[i-1] > m[i]) {
        res1 += m[i-1]-m[i];
        rate = std::max(rate, m[i-1]-m[i]);
      }
    }
    int res2 = 0;
    for (int i = 0; i < N-1; i++) {
      if (m[i] < rate) res2 += m[i];
      else res2 += rate;
    }

    std::printf ("Case #%d: %d %d\n", n_case, res1, res2);
  }

  return 0;
}
