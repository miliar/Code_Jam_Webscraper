#include <iostream>
#include <string>
#include <math.h>

using namespace std;

bool is_palindrome(unsigned long n);
unsigned long is_square(unsigned long n);

int main()
{ 
  const short length = 100;
  int i, j;
  unsigned long count = 0;
  unsigned long root;
  
  unsigned long numbers[length][2] = {{512, 552}, {115, 519}, {1, 6}, {121, 742}, {121, 485}, {85, 958}, {483, 485}, {1, 302}, {100, 1000}, {368, 518}, {65, 302}, {8, 302}, {65, 742}, {1, 221}, {397, 650}, {515, 858}, {484, 485}, {483, 484}, {1, 2}, {3, 122}, {150, 552}, {62, 662}, {393, 975}, {8, 485}, {399, 435}, {1, 101}, {21, 221}, {60, 451}, {484, 484}, {120, 742}, {120, 122}, {141, 551}, {252, 541}, {3, 221}, {1, 122}, {37, 60}, {3, 65}, {228, 702}, {65, 484}, {69, 269}, {3, 9}, {219, 525}, {384, 742}, {354, 763}, {108, 699}, {4, 122}, {51, 164}, {324, 926}, {65, 485}, {1, 9}, {751, 772}, {302, 705}, {455, 470}, {271, 592}, {121, 584}, {49, 947}, {8, 122}, {121, 302}, {1, 104}, {21, 302}, {120, 584}, {122, 1000}, {3, 485}, {122, 483}, {526, 540}, {168, 322}, {3, 5}, {190, 423}, {9, 121}, {4, 4}, {808, 862}, {1, 742}, {10, 120}, {399, 406}, {602, 916}, {121, 122}, {8, 10}, {1, 1000}, {1, 484}, {21, 484}, {65, 122}, {8, 121}, {7, 742}, {121, 484}, {8, 109}, {3, 302}, {4, 711}, {225, 603}, {249, 300}, {501, 673}, {484, 584}, {592, 681}, {9, 302}, {4, 65}, {1, 121}, {3, 10}, {9, 484}, {1, 4}, {4, 10}, {1, 5}};
  
  for(i = 0; i < length; i++)
  {
    count = 0;
    
    for(j = numbers[i][0]; j <= numbers[i][1]; j++)
    {
      root = is_square(j);
      
      if(root != -1 && is_palindrome(j) && is_palindrome(root))
      {
        count++;
      }
    }
    
    
    cout << "Case #" << i + 1 << ": " << count << "\n";
  }
  
  return 0;
}

bool is_palindrome(unsigned long n)
{
    if(n < 10 && n > -1)
      return true;
  
    int i;
    unsigned long reversed = 0;
    
    
    for (i = n; i > 0; i /= 10)
    {
      reversed = reversed * 10 + i % 10;
    }
    
    return n == reversed;
}

unsigned long is_square(unsigned long n)
{
  
  unsigned int root = (unsigned int) sqrt(n);
  bool result = root * root == n;
  
  if(result)
    return root;
  else
    return -1;
}
