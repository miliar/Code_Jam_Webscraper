#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdint>
#include <vector>
#include <algorithm>

std::string solve(std::string str, int flip);

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        std::string state;
        std::cin >> state;
        int flipper;
        std::cin >>flipper;

        std::cout << "Case #" << t << ": " << solve(state, flipper) << std::endl;
    }
    return 0;
}

char flipped(char ch) {
  return ((ch == '+') ? '-' : '+');
}

std::string solve(std::string str, int flip) {
  int flips = 0;

  for (size_t i = 0; i < str.size(); ++i) {
    if (str[i] == '+') continue;
    
    if (i + flip > str.size()) break;

    ++flips;

    for (size_t j=i; j < i+flip; ++j) {
      str[j] = flipped(str[j]);
    }
  }

  for (int i = str.size() - 1; i >= 0 && i >= int(str.size() - flip); --i) {
    if (str[i] == '-') return "IMPOSSIBLE";
  }

  return std::to_string(flips);
}
 
