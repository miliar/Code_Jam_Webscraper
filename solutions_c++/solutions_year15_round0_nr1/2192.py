#include <iostream>
#include <string>

int main() {
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    int s;
    std::string S;
    std::cin >> s >> S;
    int y = 0;
    int c = 0;
    for (int k = 0; k < S.length(); k++) {
      int a = S[k] - '0';
      if (c < k) {
        y += k - c;
        c = k;
      }
      c += a;
    }
    std::cout << "Case #" << i + 1 << ": " << y << std::endl;
  }
}
