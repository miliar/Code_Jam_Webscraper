#include <iostream>

unsigned int count(unsigned int N) {
  unsigned int bits = 0;
  unsigned int u = 0;
  unsigned int v;

  do {
    u += N;
    for(v = u; v > 0; v /= 10) {
      bits |= 1 << (v % 10);
    }    
  } while(bits != 0x3FF);

  return u;
}

int main(int argc, char **argv) {
  unsigned int T, N, u;

  std::cin >> T;

  for(u = 1; u <= T; ++u) {
    std::cin >> N;
    std::cout << "Case #" << u << ": ";
    if(N == 0) {
      std::cout << "INSOMNIA";
    } else {
      std::cout << count(N);
    }
    std::cout << std::endl;
  }

  return 0;
}
