#include <stdio.h>
#include <stdint.h>
#include <cstring>
#include <iostream>
#include <math.h>

using namespace std;

bool is_palindrome(uint64_t a)
{
  if (a < 10)
    return true;
    
  char str[1024];
  sprintf(str, "%lld", a);
  int len = strlen(str);
  
  for (int i=0; i<=len/2; ++i)
  {
    if (str[i] != str[len-1-i])
      return false;
  }
  return true;
}

uint64_t result(uint64_t a, uint64_t b)
{
  uint64_t count = 0;
  uint64_t limit = b; //std::min(b, a*a)
  uint64_t sa = (uint64_t) ceil(sqrt(a));
  uint64_t sb = (uint64_t) floor(sqrt(b));
  
  for (uint64_t k=sa; k<=sb; ++k)
  {
    uint64_t v = k*k;
    if (v>=a && v<=b && is_palindrome(k) && is_palindrome(v))
      ++count;
  }
  return count;
}

int main(int argc, char **argv)
{
  int ncases = 0;
  cin >> ncases;
  
  for (int c=1; c<=ncases; ++c)
  {
    uint64_t a, b;
    
    cin >> a >> b;
    
    printf("Case #%d: %lld\n", c, result(a,b));
  }
}
