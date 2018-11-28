#include <iostream>
#include <queue>

unsigned int serialize(std::string S) {
  unsigned int u = 0;
  unsigned char c = '+';

  for(auto it = S.rbegin(); it != S.rend(); ++it) {
    if(*it != c) {
      ++u;
      c = *it;
    }
  }

  return u;
}

int main(int argc, char **argv) {
  unsigned int T, u;
  std::string S;

  std::cin >> T;

  for(u = 1; u <= T; ++u) {
    std::cin >> S;
    std::cout << "Case #" << u << ": ";
    std::cout << serialize(S);
    std::cout << std::endl;
  }

  return 0;
}
