#include <iostream>
#include <string>

bool CheckCakes(const std::string &Cakes) {
  return cakes.find('-') == std::string::npos;
}

size_t FlipCount(const std::string &Cakes) {
  std::string cakes = Cakes;
  size_t flip_count = 0;
  while (!CheckCakes(cakes)) {
    char first_cake = cakes[0];
    for (size_t i = 0; cakes[i] && (cakes[i] == first_cake); ++i) {
      cakes[i] = (cakes[i] == '+') ? '-' : '+';
    }
    ++flip_count;
  }
  return flip_count;
}

int main() {
  size_t T;
  std::cin >> T;
  for (size_t t = 1; t <= T; ++t) {
    std::string cakes;
    std::cin >> cakes;
    std::cout << "Case #" << t << ": " << FlipCount(cakes) << "\n";
  }
  return 0;
}
