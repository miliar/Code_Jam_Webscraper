#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

std::string solve(uint32_t n) {
  std::vector<bool> seen(10, false);
  uint32_t num, missing = 10;

  if(n == 0)
    return "INSOMNIA";

  for(uint32_t i = 1; missing > 0; ++i) {
    num = i*n;
    std::string str = std::to_string(num);

    for(uint32_t j = 0; j < str.size(); ++j) {
      uint32_t digit = str[j] & 0x0F;

      if(!seen[digit]) {
        seen[digit] = true;
        --missing;
      }
    }
  }

  return std::to_string(num);
}


int main() {
  uint32_t cases, n;

  cin >> cases;

  for(uint32_t i = 0; i < cases; ++i) {
    cin >> n;

    cout << "Case #" << i+1 << ": " << solve(n) << std::endl;
  }

  return 0;
}
