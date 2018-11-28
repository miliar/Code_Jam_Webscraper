#include <iostream>
#include <algorithm>

int main(int argc, char* argv[])
{
  int T, j;
  for (std::cin >> T, j = 0; j < T; ++j) {
    std::cout << "Case #" << j + 1 << ": ";
    std::string word;
    std::cin >> word;
    int moves = 0;

    while (std::any_of(word.begin(), word.end(), [](char w) { return w == '-'; })) {
      ++moves;

      auto n = std::find(word.begin(), word.end(), '-');
      if (n != word.end()) {
        for (; n + 1 != word.end() && *(n + 1) != '+'; ++n)
          ;
        std::transform(word.begin(), n + 1, word.begin(), [](const char& i) -> char {
            if (i == '-') { 
              return '+';
            } else {
              return '-';
            }
        });
      }
    }
    std::cout << moves << '\n';
  }

  return 0;
}
