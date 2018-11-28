#include <cstdint>
#include <iostream>
#include <deque>
#include <string>
#include <stdexcept>
#include <algorithm>
#include <tuple>
#include <sstream>

#include "bigint-10-0-src/bigInt.h"

std::string generateCoin(uint32_t n, uint32_t x)
{
  std::stringstream ss;
  ss << "1";
  for (int32_t i = (n - 1); i >= 0; --i)
    ss << ((x >> i) & 1);
  ss << "1";

  return ss.str();
}

void handle(uint32_t n, uint32_t j)
{
  n -= 2;
  uint32_t count(0);
  uint32_t N(1 << n);
  for (int x = 0; x < N; ++x)
  {
    auto coin(generateCoin(n, x));
//    std::cout << "Trying Coin: " << x << " " << coin << std::endl;
    //
    std::vector<uint64_t> divisors;
    for (uint64_t base = 2; base <= 10; ++base)
    {
      //auto based(stoull(coin, nullptr, base));
      BigInt::Rossi based(coin, base);
//      std::cout << "\t" << base << ": " << based << std::endl;
      bool found(false);
      //for (uint64_t div = 3; div < based; ++div) // we know it is always odd
      for (uint64_t div = 3; div < 50; ++div) // we know it is always odd, also restrict
      {
        if (based % BigInt::Rossi(div) == BigInt::Rossi(0))
        {
          divisors.push_back(div);
          found = true;
          break;
        }
      }

      if (!found)
        break;
    }

    if (divisors.size() == 9)
    {
      std::cout << coin;
      for (auto div : divisors)
        std::cout << " " << div;
      std::cout << std::endl;
      ++count;
    }

    if (count == j)
      break;
  }
  if (count != j)
    throw std::runtime_error("Not enough coins found");
}

int main()
{
  std::string s;
  getline(std::cin, s);
  uint32_t t;
  std::stringstream(s) >> t;
  if (t < 1 || t > 100)
  {
    std::cerr << "invalid t: " << t << std::endl;
    exit(1);
  }

  uint32_t i = 1;
  while (std::getline(std::cin, s))
  {
    std::stringstream ss(s);
    uint32_t n(0), j(0);
    if (!(ss >> n) || n < 2)
      throw std::runtime_error("invalid n");
    if (!(ss >> j) || j < 1)
      throw std::runtime_error("invalid j");

    std::cout << "case #" << i << ":" << std::endl;
    handle(n, j);
    ++i;
  }
}

