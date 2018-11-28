#include <iostream>
#include <cmath>
#include <vector>
#include <cstdint>
#include <bitset>

uint64_t ConvertToBase(std::vector<int> &coin, int base)
{
  uint64_t v = 1;
  for (int i = coin.size()-1; i >= 0; i--) {
    v *= base;
    v += coin[i];
  }
  return v * base + 1;
}

uint64_t SmallestDivisor(uint64_t val)
{
  if (!(val % 2)) return 2;
  if (!(val % 3)) return 3;
  for (uint64_t sm = 5; sm * sm <= val; sm += 6) {
    if (!(val % sm)) return sm;
    if (!(val % (sm+2))) return sm+2;
  }
  return val;
}

std::vector<uint64_t> IsJamcoin(std::vector<int> &coin)
{
  std::vector<uint64_t> res;
  for (int i = 2; i <= 10; i++) {
    uint64_t val = ConvertToBase(coin, i);
    uint64_t small = SmallestDivisor(val);
    if (small == val) return {};
    res.push_back(small);
  }
  return res;
}

int main()
{
  int t, n, c;
  std::cin >> t >> n >> c;
  std::cout << "Case #1:" << std::endl;
  int coins = 0;
  std::vector<int> coin(n-2);
  for (int i = 0; i < 1<<coin.size(); i++) {
    for (int j = 0; j < coin.size(); j++) {
      coin[j] = (i&(1<<j))?1:0;
    }
    auto v = IsJamcoin(coin);
    if (!v.size()) continue;
    coins++;
    std::cout << "1" << std::bitset<14>(i) << "1";
    for (auto it : v) {
      std::cout << " " << it;
    }
    std::cout << std::endl;
    if (coins == c) return 0;
  }
}
