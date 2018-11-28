#include <iostream>
#include <string>

int countFlips(const std::string& pancakes)
{
  int flips = 0;
  
  for (int i = 0; i < pancakes.size() - 1; ++i) {
    if (pancakes[i] != pancakes[i + 1]) {
      ++flips;
    }
  }

  if (pancakes[pancakes.size() - 1] == '-') {
    ++flips;
  }

  return flips;
}

int main()
{
  int cases = 0;
  std::cin >> cases;

  for (int i = 1; i <= cases; ++i) {
    std::string pancakes;
    std::cin >> pancakes;

    std::cout << "Case #" << i << ": " << countFlips(pancakes) << std::endl;
  }
  
  return 0;
}
