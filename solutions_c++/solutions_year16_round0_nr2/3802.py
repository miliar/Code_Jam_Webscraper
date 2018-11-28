#include <iostream>
#include <string>

int solve(std::string &s) {
  int counter = 0;
  int i = 0;
  int sz = s.size();
  while (i < sz && s[i] == '-') {
    ++i;
  }
  if (i != 0) {
    ++counter;
  }

  while (i < sz) {
    bool change = false;
    while (i < sz && s[i] == '+') {
      ++i;
    }
    while (i < sz && s[i] == '-') {
      change = true;
      ++i;
    }
    if (change) {
      counter += 2;
    }
  }
  return counter;
}

int main() {
  int sz;
  std::cin >> sz;
  std::string line;
  std::getline(std::cin, line);
  for (int i = 1; i <= sz; ++i) {
    std::string s;
    std::getline(std::cin, line);
    std::cout << "Case #" << i << ": ";
    std::cout << solve(line) << std::endl;
  }
  return 0;
}