#include <iostream>

int main()
{
  int number_of_tests;
  std::cin >> number_of_tests;
  for (int test_number = 0; test_number < number_of_tests; ++test_number)
  {
    int s_max;
    std::cin >> s_max;
    int current = 0;
    int added = 0;
    for (int i = 0; i <= s_max; ++i)
    {
      char v;
      std::cin >> v;
      v -= '0';
      if (current < i)
      {
        added += i - current;
        current += i - current;
      }
      current += v;
    }
    std::cout << "Case #" << test_number + 1 << ": " << added << std::endl;
  }

  return 0;
}
