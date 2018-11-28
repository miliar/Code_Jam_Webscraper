#include <signal.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <ctype.h>
#include <string.h>
#include <stdarg.h>

#include <limits>
#include <ostream>
#include <istream>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <functional>
#include <sstream>
#include <utility>
#include <numeric> 
#include <memory>


bool Palindrom(int n)
{
     std::stringstream ss;
     ss << n;
     std::string s = ss.str();
     std::reverse(s.begin(), s.end());
     return s == ss.str();
}


int Compute(int low, int high)
{
     int LOW = (int) sqrt((double) low);
     int HIGH = (int) sqrt((double) high + 1);

     int cnt = 0;
     for (int i = LOW; i <= HIGH; i++)
     {
	  if (!Palindrom(i)) continue;
	  int ii = i * i;
	  if (Palindrom(ii) && low <= ii && ii <= high)
	  {
	       cnt++;
	  }
     }
     return cnt;
}

int main()
{
     int TCNum;
     std::cin >>  TCNum;
     for (int i = 1; i <= TCNum; i++)
     {
	  int low;
	  int high;
	  std::cin >> low;
	  std::cin >> high;
	  int result = Compute(low, high);
	  std::cout << "Case #" << i << ": " << result << std::endl;
     }
     return 0;
}
