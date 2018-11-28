#include <cstdint>
#include <iostream>
#include <set>
#include <string>

std::set<char> getDigits(uint64_t n)
{
  std::set<char> set;

  auto s(std::to_string(n));
  set.insert(s.begin(), s.end());

  return set;
}

void printset(std::set<char> const &set)
{
  for (auto c : set)
    std::cout << c << " ";
  std::cout << std::endl;
}

void handle(std::set<char> const &reference, uint32_t n)
{
  std::set<char> total;
  for (int i = 1; i < 100; ++i)
  {
    auto x(i * n);
    auto set(getDigits(x));
    total.insert(set.begin(), set.end());
    //std::cout << "Adding " << x << std::endl;
    //std:: cout << "Set: ";
    //printset(set);
    //std:: cout << "Total: ";
    //printset(total);
    if (total == reference)
    {
      std::cout << x << std::endl;
      return;
    }
  }

  std::cout << "INSOMNIA" << std::endl;
}

int main()
{
  std::set<char> reference(getDigits(9876543210));

  uint32_t t;
  std::cin >> t;
  if (t < 1 || t > 100)
  {
    std::cerr << "invalid t: " << t << std::endl;
    exit(1);
  }

  uint32_t i = 1;
  uint64_t n;
  while (std::cin >> n)
  {
    std::cout << "case #" << i << ": ";
    handle(reference, n);
    ++i;
  }
}

