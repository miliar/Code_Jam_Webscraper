#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>
#include <numeric>
#include <functional>

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    std::string S;
    int K;
    std::cin >> S >> K;

    size_t n = 0;
    for (size_t i = 0; i <= S.size() - K; ++i) {
      auto c = S[i];
      if (c == '+') {
        continue;
      }
      ++n;
      for (int j = i; j < i + K; ++j) {
        S[j] = S[j] == '+' ? '-' : '+';
      }
    }
    size_t i;
    for (i = S.size() - K + 1; i < S.size(); ++i) {
      auto c = S[i];
      if (c == '+') {
        continue;
      }
      break;
    }
    std::cout << "Case #" << t << ": ";
    if (i == S.size()) {
      std::cout << n;
    } else {
      std::cout << "IMPOSSIBLE";
    }
    std::cout << std::endl;
  }
}
