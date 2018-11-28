#include <algorithm>
#include <iostream>
#include <string>

int main() {
  size_t T;
  std::cin >> T;
  for (size_t t = 1; t <= T; ++t) {
    std::string s;
    size_t k;
    std::cin >> s >> k;

    size_t step = 0;

    for (size_t i = 0; s[i + k - 1]; ++i) {
      if (s[i] == '-') {
        ++step;
        for (size_t j = 0; j < k; ++j) {
          s[i + j] = (s[i + j] == '-') ? '+' : '-';
        }
      }
    }

    std::cout << "Case #" << t << ": ";
    
    if (s.find("-") != std::string::npos) {
      std::cout << "IMPOSSIBLE\n";
    } else {
      std::cout << step << "\n";
    }

  }
  return 0;
}
