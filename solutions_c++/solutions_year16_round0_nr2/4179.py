#include <iostream>
#include <vector>
#include <string>
#include <array>

int main() {
  int T;
  std::cin >> T;
  for (auto test = 1; test <= T; ++test) {
    std::string s;
    std::cin >> s;
    std::reverse(std::begin(s), std::end(s));
    int ans = 0;
    auto t = '-';
    for (int i = 0; i < s.size();) {
      auto c = s[i];
      if (c != t) {
        ++i;
        continue;
      }
      ++ans;
      for (; i < s.size() && s[i] == t; ++i)
        ;
      if (t == '-') {
        t = '+';
      } else {
        t = '-';
      }
    }
    std::cout << "Case #" << test << ": " << ans << std::endl;
  }
}
