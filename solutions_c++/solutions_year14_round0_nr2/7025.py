#include <iostream>
#include <string>
#include <vector>
#include <iomanip> 
using namespace std;


int main()
{
  int n;
  double c, f, x, res, prev;
  
  std::cin >> n;
  std::cin.ignore();
  
  for(int i = 0; i < n; i++)
    {
      c = f = x = res = 0;
      prev = res + 1;
  
      std::cin >> c;
      std::cin.ignore();
      std::cin >> f;
      std::cin.ignore();
      std::cin >> x;
      std::cin.ignore();

      res = x/2; 	  //0 ferme
      prev = res + 1;
      int j = 1;
      bool inf = true;
      while(prev > res)
	{
	  prev = res;
	  res = x/(j*f + 2);
	  for(int i = 0; i < j; i++)
	    res += c/(2+i*f);
	  
	  j++;
	  //	  std::cout << res << std::endl;
	}
      
      std::cout << "Case #" << i+1 << ": " << std::setprecision(16) << prev << std::endl;
    }

  return 0;

}
