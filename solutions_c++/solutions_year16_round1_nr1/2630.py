#include <iostream>
#include <string>

int main() {
  int T;
  std::cin >> T;

  for (int t = 0; t < T; ++ t) {
    std::cout << "Case #" << t + 1 << ": ";

    std::string s;
    std::cin >> s;

    std::string answer;
    for (const char c : s) {
      if (c < answer[0]) {
        answer += c;
      } else {
        answer = c + answer;
      }
    }

    std::cout << answer << "\n";
  }

  return 0;
}
