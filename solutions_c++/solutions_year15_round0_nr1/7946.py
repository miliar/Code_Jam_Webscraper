#include <iostream>

int solve(int s_max, int* shynesses)
{
  int count = shynesses[0];
  int friends = 0;
  for (int i = 1; i <= s_max; ++i)
  {
    if (count + friends < i)
      friends += i - (count + friends);
    count += shynesses[i];
  }
  return friends;
}

int main()
{
  int t;
  std::cin >> t;
  for (int i = 0; i < t; ++i)
  {
    int s_max;
    std::cin >> s_max;
    int shynesses[s_max + 1];
    std::string shynesses_str;
    std::cin >> shynesses_str;
    for (int s = 0; s <= s_max; ++s)
      shynesses[s] = shynesses_str[s] - '0';
    std::cout << "Case #" << (i + 1) << ": " <<
      solve(s_max, shynesses) << std::endl;
  }
  return 0;
}
