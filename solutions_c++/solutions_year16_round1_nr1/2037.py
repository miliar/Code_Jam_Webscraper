#include <iostream>
#include <algorithm>
#include <string>
#include <deque>

void solve_case(int case_num)
{
  std::string s;
  std::deque<char> v;
  char max_char = '\0';

  std::cin >> s;
  std::cout << "CASE #" << case_num << ": ";

  for (char& ch : s) {
    if (ch >= max_char) {
      v.push_front(ch);
      max_char = ch;
    } else {
      v.push_back(ch);
    }
  }

  for (char &ch: v) {
    std::cout << (char)ch;
  }
  std::cout << std::endl;
}

int main()
{
  int num_cases;

  std::cin >> num_cases;
  for (int i = 1; i <= num_cases; i++) {
    solve_case(i);
  }
  
  return 0;
}
