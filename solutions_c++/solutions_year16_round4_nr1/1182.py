#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

std::string kResult[3][13];

void Init() {
  kResult[0][0] = "P";
  kResult[1][0] = "R";
  kResult[2][0] = "S";
  for (int i = 1; i <= 12; i++) {
    for (int k = 0; k < 3; k++) {
      int k2 = (k + 1) % 3;
      std::string a = kResult[k][i - 1] + kResult[k2][i - 1];
      std::string b = kResult[k2][i - 1] + kResult[k][i - 1];
      kResult[k][i] = std::min(a, b);
    }
  }
}

int main() {
  Init();
  int t;
  std::cin >> t;
  for (int x = 1; x <= t; x++) {
    int n, r, p, s;
    std::cin >> n >> r >> p >> s;
    bool failure = false;
    for (int i = 1; i <= n; i++) {
      int m = 1 << (n - i);
      int x = m - s;
      int y = m - r;
      int z = m - p;
      p = x;
      r = z;
      s = y;
      if (p < 0 || r < 0 || s < 0) {
        failure = true;
        break;
      }
    }
    std::string y;
    if (failure) {
      y = "IMPOSSIBLE";
    } else {
      int k = -1;
      if (p > 0) {
        k = 0;
      } else if (r > 0) {
        k = 1;
      } else {
        k = 2;
      }
      y = kResult[k][n];
    }
    std::cout << "Case #" << x << ": " << y << std::endl;
  }
}
