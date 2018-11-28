#include <iostream>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <math.h>

using namespace std;

#define get std::cin
void i64toa (uint64_t value, char *string, int radix = 10)
{
  char *i, *s, t, d;

  i = string;

  s = i;

  do
  {   d = value % radix;
    value /= radix;

    if (d > 9)
      *i++ = d + 'A' - 10;
    else
      *i++ = d + '0';
  } while (value > 0);

  *i-- = '\0';

  do
  {   t = *i;
    *i = *s;
    *s = t;

    --i;
    ++s;
  } while (s < i);
}

bool ispolindrome(uint64_t number)
{
  bool poly= true;
  char str[1024];
  i64toa(number, str);
  int len = strlen(str);
  for(int i = 0; i<(len/2); ++i)
  {
    poly &= str[i]==str[len-i-1];
  }
  return poly;
}

int main()
{
  //uint128_t counter;
  std::ifstream inFile;
  inFile.open("/home/dez/src/jam-0/Lawnmower/Lawnmower/C-small-attempt0.in", std::ios::in);
  int testCases(0);
  inFile >> testCases;
  for(int j = 1; j<= testCases; ++j)
  {
    int polucount = 0;
    uint64_t left, right;
    inFile >> left;
    inFile >> right;
    for(uint64_t val = left; val <= right; ++val)
    {
      if(ispolindrome(val))
      {
        uint64_t val2 = sqrt(val);
        if(val2*val2 == val)
        {
          if(ispolindrome(val2))
          {
            ++ polucount;
          }
        }
      }
    }
    std::cout << "Case #" << j <<": " << polucount << "\n";
  }
  return 0;
}

