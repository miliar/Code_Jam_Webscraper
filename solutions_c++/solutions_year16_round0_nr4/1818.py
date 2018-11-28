#include <iostream>

int main(int argc, char **argv) {
  unsigned int T, K, C, S, u, v;

  std::cin >> T;

  for(u = 1; u <= T; ++u) {
    std::cin >> K >> C >> S;

    std::cout << "Case #" << u << ":";
    for(v = 1; v <= K; ++v) {
      std::cout << ' ' << v;
    }
    std::cout << std::endl;
  }

  return 0;
}
