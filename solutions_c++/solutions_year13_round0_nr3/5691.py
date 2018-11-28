#include <iostream>

bool palindrome(int num)
{
  int orig = num;
  int rev = 0;
  while (num > 0)
  {
    int digit = num % 10;
    rev = rev * 10 + digit;
    num = num / 10;
  }
  return orig == rev;
}

int main()
{
  int t;
  std::cin >> t;
  for ( int i = 0; i < t; ++i )
  {
    int a, b;
    std::cin >> a >> b;
    int count = 0;
    for ( int k = 0; k <= b; ++k )
    {
      int sq = k * k;
      if ( sq < a )
        continue;
      if ( sq > b )
        break;
      if ( palindrome(k) && palindrome(sq) )
        ++count;
    }
    std::cout << "Case #" << (i + 1) << ": " << count << std::endl;
  }
}

