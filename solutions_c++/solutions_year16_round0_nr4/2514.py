#include <iostream>
#include <cstdint>

int64_t pow(int64_t k, int64_t c)
{
  if (c == 0) return 1;
  return k * pow(k, c-1);
}

void solve(int64_t k, int64_t c, int64_t s)
{
  int64_t pos = 0;
  int64_t power_val = pow(k, c-1);
  for (int64_t i = 0; i < s; i++) {
    std::cout << " " << pos + 1;
    pos += power_val;
  }
}

int main()
{
  int64_t t;
  std::cin >> t;
  for (int64_t i = 1; i <= t; i++) {
    int64_t a, b, c;
    std::cin >> a >> b >> c;
    std::cout << "Case #" << i << ":";
    solve(a,b,c);
    std::cout << std::endl;
  }
}
