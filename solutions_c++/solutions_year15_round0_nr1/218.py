#include <iostream>

int main() {
  int T;
  std::cin >> T;
  for (int t = 1; t <= T; ++t) {
    int n;
    std::string s;
    std::cin >> n >> s;
    n = 0;
    for (int i = 0, m = 0; i < s.size(); ++i) {
      if (m < i) {
        n += i - m;
        m = i;
      }
      m += s[i] - '0';
    }
    std::cout << "Case #" << t << ": " << n << "\n";
  }
  return 0;
}
