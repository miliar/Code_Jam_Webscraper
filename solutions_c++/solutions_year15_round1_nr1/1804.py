#include <iostream>

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N, m[1000];
    std::cin >> N;
    for (int i = 0; i < N; ++i) std::cin >> m[i];
    int p1 = 0, p2 = 0, r = -1;
    for (int i = 1; i < N; ++i) {
      if (m[i] < m[i-1]) {
        int q = m[i-1] - m[i];
        p1 += q;
        if (r == -1) r = q;
        else r = std::max(r, q);
      }
    }
    if (r == -1) r = 0;
    for (int i = 1; i < N; ++i) {
      p2 += std::min(m[i-1], r);
    }
    std::cout << "Case #" << t << ": " << p1 << " " << p2 << "\n";
  }
  return 0;
}
