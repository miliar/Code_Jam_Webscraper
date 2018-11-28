#include <iostream>

int calc_worst(int x, int n) {
  int ret = 0;
  int left = x;

  for (int i = 0; i < n; ++i) {
    if (left > 0) {
      ret = (ret << 1) + 1;
      left = (left - 1) / 2;
    } else {
      ret <<= 1;
    }
  }

  return ret;
}


int calc_best(int x, int n) {
  int ret = 0;
  int left = (1 << n) - x - 1;

  for (int i = 0; i < n; ++i) {
    if (left > 0) {
      ret <<= 1;
      left = (left - 1) / 2;
    } else {
      ret = (ret << 1) + 1;
    }
  }

  return ret;
}

int main() {
  int T;
  std::cin >> T;

for (int tt = 1; tt <= T; ++tt) {
  int n, p;
  std::cin >> n >> p;

  int tot = 1 << n;
  std::cout << "Case #" << tt << ": ";
  for (int i = tot - 1; i >= 0; --i) {
    if (calc_worst(i, n) < p) {
      std::cout << i << " ";
      break;
    }
  }

  for (int i = tot - 1; i >= 0; --i) {
    if (calc_best(i, n) < p) {
      std::cout << i << std::endl;
      break;
    }
  }
}
}
