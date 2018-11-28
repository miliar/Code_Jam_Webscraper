#include <iostream>

int main()
{
  int T = 0;
  std::cin >> T;
  for(int i = 0; i < T; i++)
  {
    std::string dontcare, shys;
    std::cin >> dontcare;
    std::cin >> shys;

    const char *s = shys.c_str();
    int sh = 0;
    int y = 0;
    for(int j = 0; j < shys.size(); j++)
    {
      if((s[j] - '0') && j > sh)
      {
        y += j - sh;
        sh += j - sh;
      }
      sh += s[j] - '0';
    }
    std::cout << "Case #" << (i + 1) << ": " << y << std::endl;
  }
}
