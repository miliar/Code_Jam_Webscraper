#include <iostream>
#include <string>

template<typename T, typename V>
T consume(T begin, T end, V val)
{
  while (begin != end && *begin == val) begin++;
  return begin;
}

int flips(const std::string &s)
{
  int f = 0;
  auto b = s.rbegin();
  auto e = s.rend();
  b = consume(b, e, '+');
  char c = '-';
  while (b != e) {
    b = consume(b, e, c);
    c = (c == '+' ? '-' : '+');
    f++;
  }
  return f;
}

int main()
{
  int T;
  std::cin >> T;
  for (int i = 1; i <= T; i++) {
    std::string str;
    std::cin >> str;
    std::cout << "Case #" << i << ": " << flips(str) << std::endl;
  }
  return 0;
}
