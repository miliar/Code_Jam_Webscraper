#include <iostream>
#include <vector>
#include <string>

int main()
{
  int T;
  std::cin >> T;
  for (int t=1; t <= T; t++)
  {
    int Sm;
    std::cin >> Sm;
    std::string a;
    std::cin >> a;
    
    int req = 0;
    int sum = a[0] - '0';
    for (int i=1; i <= Sm; i++)
    {
      if (sum < i)
      {
        req += (i - sum);
        sum = i;
      }
      sum += a[i] - '0';
    }
      
    std::cout << "Case #" << t << ": " << req << std::endl;
  }
  return 0;
}
