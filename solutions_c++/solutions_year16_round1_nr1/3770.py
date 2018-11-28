#include <deque>
#include <iostream>
#include <string>

int main(int argc, char const *argv[]) {
  unsigned t;

  std::cin >> t;
  for (unsigned t_ = 1; t_ <= t; ++t_) {
    std::string s;
    std::deque<char> last_word;

    std::cin >> s;

    // Build word
    int i = 1;
    last_word.push_back(s[0]);
    while (i < s.length()) {
      if (s[i] < last_word[0])
        last_word.push_back(s[i]);
      else
        last_word.push_front(s[i]);
      i++;
    }

    s = "";
    for (char c : last_word) {
      s += c;
    }

    std::cout << "Case #" << t_ << ": " << s << std::endl;
  }

  return 0;
}
