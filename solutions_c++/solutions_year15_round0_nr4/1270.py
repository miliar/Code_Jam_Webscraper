#include <iostream>

int main() {
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    int x, r, c;
    std::cin >> x >> r >> c;
    int s = r * c;
    bool win = false;
    if (s % x == 0) {
      switch (x) {
      case 1:
      case 2:
        win = true;
        break;
      case 3:
        win = (s >= 6);
        break;
      case 4:
        win = (s >= 12);
        break;
      }
    }
    std::cout << "Case #" << i + 1 << ": " << (win ? "GABRIEL" : "RICHARD") << std::endl;
  }
}
