#include <iostream>

int f(int* p, int i) {
  if (i < 4) {
    if (p[3]) return 3;
    if (p[2]) return 2;
    return 1;
  }
  if (!p[i]) return f(p, i-1);
  int z = p[i];
  p[i] = 0;
  int x = i / 2;
  p[x] += z;
  p[i - x] += z;
  int n = std::min(z + f(p, i-1), i);
  p[x] -= z;
  p[i - x] -= z;
  if (i > 6) {
    x = i / 3;
    p[x] += 2 * z;
    p[i - 2 * x] += z;
    n = std::min(2 * z + f(p, i-1), n);
    p[x] -= 2 * z;
    p[i - 2 * x] -= z;
  }
  p[i] = z;
  return n;
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int D;
    std::cin >> D;
    int p[1001] = {0};
    for (int d = 0, n; d < D; ++d) {
      std::cin >> n;
      ++p[n];
    }
    std::cout << "Case #" << t << ": " << f(p, 1000) << "\n";
  }
  return 0;
}
