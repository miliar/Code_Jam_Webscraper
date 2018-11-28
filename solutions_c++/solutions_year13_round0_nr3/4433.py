#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <math.h>

bool isPalimdrom(std::string nbStr)
{
  for (int i = 0, j = (nbStr.size() - 1); i < (nbStr.size() / 2); ++i, --j)
    {
      if (nbStr[i] != nbStr[j])
	{
	  return false;
	}
    }
  return true;
}

int	main()
{
  int nb_cases;

  std::cin >> nb_cases;
  for (int test_case = 1; test_case <= nb_cases; ++test_case)
    {
      std::cout << "Case #" << test_case << ": ";

      int m, n;
      std::cin >> n;
      std::cin >> m;
      int result = 0;
      while (n <= m)
	{
	  float z = sqrt(n);
	  if (z == (int)z)
	    {
	      std::ostringstream convert;
	      std::string nbStr, sqrtStr;
	      convert << n;
	      nbStr = convert.str(); 
	      convert.str("");
	      convert << (int)z;
	      sqrtStr = convert.str();
	      bool ispal = false;
	      if (isPalimdrom(nbStr))
		ispal = isPalimdrom(sqrtStr);
	      if (ispal)
		{
		  ++result;
		}
	    }
	  ++n;
	}
      std::cout  << result << std::endl;
    }
}
