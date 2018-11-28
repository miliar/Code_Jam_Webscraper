#include <iostream>
#include <string>

static const int MaxAudience = 1024;

int main(int argc, char **argv)
{
  int testCases;

  std::cin >> testCases;
  
  for (int testCase = 1; testCase <= testCases; testCase++) {
    int audience[MaxAudience];
    std::string saudience;
    int max, needed = 0;

    std::cin >> max;
    std::cin >> saudience;

    int current = saudience[0] - '0';
    for (int i = 1; i <= max; i++) {
      int topping = 0;
      if (current < i)
	topping = i - current;

      needed += topping;
      current += topping + (saudience[i] - '0');
    }

    std::cout << "Case #" << testCase << ": " << needed << std::endl;
  }
}
