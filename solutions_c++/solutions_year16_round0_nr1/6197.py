#include <iostream>
#include <cstdint>
using namespace std;
uint32_t mask;

void SetMask(uint64_t tmp) {
  while (tmp) {
    mask |= (0x1 << (tmp%10));
    tmp = tmp/10;
  }
}

int main() {
  uint64_t T, N;
  cin >> T;
  for (uint64_t i = 1; i <= T; i++) {
    cin >> N;
    mask = 0x0;
    cout << "Case #" << i  << ": ";
    if (N) {
      uint32_t c = 1;
      uint64_t tmp = 0;
      while(true) {
        tmp = c*N;
        SetMask(tmp);
        if (mask == 0x3FF)
          break;
        c++;
      }
      cout << tmp;
    } else {
      cout << "INSOMNIA";
    }
    cout << "\n";
  }

  return 0;
}



