#include <iostream>
#include <vector>
#include <string>
#include <array>
#include <deque>

int main() {
  int T;
  std::cin >> T;
  for (auto test = 1; test <= T; ++test) {
    std::string s;
    std::cin >> s;

    std::deque<char> res;
    res.push_back(s[0]);
    for (size_t i = 1; i < s.size(); ++i) {
      auto c = s[i];
      if (res[0] > c) {
        res.push_back(c);
      } else {
        res.push_front(c);
      }
    }

    std::cout << "Case #" << test << ": ";
    std::copy(std::begin(res), std::end(res),
              std::ostream_iterator<char>(std::cout, ""));
    std::cout << std::endl;
  }
}
