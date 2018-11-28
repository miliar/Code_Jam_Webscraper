#include <iostream>
#include <string>

int main() {

  size_t T;
  std::cin >> T;
  for (size_t t = 1; t <= T; ++t) {
    size_t K, C, S;
    std::cin >> K >> C >> S;
    std::cout << "Case #" << t << ":";
    for (size_t i = 1; i <= S; ++i) {
      std::cout << " " << i;
    }
    std::cout << "\n";
  }
  return 0;
}
