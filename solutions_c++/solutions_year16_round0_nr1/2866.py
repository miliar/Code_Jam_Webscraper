#include <iostream>

size_t max;

void Count(size_t n, size_t &seen) {
  do {
    seen |= 1 << (n % 10);
    n /= 10;
  } while (n);
}

size_t LastBeforeSleep(const size_t N) {
  const size_t TARGET = (1 << 10) - 1;
  size_t n, seen = 0;
  for (n = N; seen != TARGET; n += N) {
    if (n >= max) max = n;
    Count(n, seen);
  }
  return n - N;
}

int main() {
  size_t T;
  std::cin >> T;
  for (size_t t = 1; t <= T; ++t) {
    size_t N;
    std::cin >> N;
    std::cout << "Case #" << t << ": ";
    if (N) {
      std::cout << LastBeforeSleep(N) << "\n";
    } else {
      std::cout << "INSOMNIA\n";
    }
  }
  return 0;
}
