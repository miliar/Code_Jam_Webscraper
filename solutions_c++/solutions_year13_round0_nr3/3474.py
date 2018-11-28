/* CodeJam solution fairSquare in C++ by domob.  */

/* Should work for small and large1, but fail for large2.  Doesn't matter
   for this contest, though.  */

//#define NDEBUG

#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdint.h>
#include <sstream>

typedef long long unsigned int largeT;

/* Test if a number is a palindrome.  */
bool
isPalindrome (largeT num)
{
  std::ostringstream out;
  out << num;

  std::string str = out.str ();
  for (size_t i = 0; 2 * i < str.size (); ++i)
    if (str[i] != str[str.size () - 1 - i])
      return false;

  return true;
}

/* Iteratively construct palindromes.  */
largeT
constructPalindrome (largeT a, largeT b, char* resOrig, char* res, int d)
{
  if (d <= 0)
    {
      largeT num;
      sscanf (resOrig, "%llu", &num);
      assert (isPalindrome (num));
      largeT sq = num * num;
      if (sq >= a && sq <= b && isPalindrome (sq))
        return 1;
      return 0;
    }

  largeT cnt = 0;
  char min;
  if (res == resOrig)
    min = '1';
  else  
    min = '0';
  for (char cur = min; cur <= '9'; ++cur)
    {
      res[0] = cur;
      res[d - 1] = cur;
      cnt += constructPalindrome (a, b, resOrig, res + 1, d - 2);
    }

  return cnt;
}

/* Construct palindromes with given number of digits and check their squares.  */
largeT
findWithDigits (largeT a, largeT b, unsigned d)
{
  char res[20];
  res[d] = 0;

  return constructPalindrome (a, b, res, res, static_cast<int> (d));
}

/* Solve a single case.  */
void
solve_case ()
{
  largeT a, b;
  scanf ("%llu %llu", &a, &b);

  unsigned digitsMin, digitsMax;
  largeT cur = 1;
  unsigned d = 1;
  while (true)
    {
      if (cur > a)
        digitsMin = d - 1;
      if (cur > b)
        {
          digitsMax = d - 1;
          break;
        }
      cur *= 10;
      ++d;
    }

  /* Square has about half as many digits, just include a safety margin.  */
  digitsMin = digitsMin / 2;
  if (digitsMin > 0)
    digitsMin -= 1;
  if (digitsMin <= 0)
    digitsMin = 1;
  digitsMax = digitsMax / 2 + 2;

  largeT res = 0;
  for (unsigned d = digitsMin; d <= digitsMax; ++d)
    res += findWithDigits (a, b, d);

  printf ("%llu", res);
}

/* Main routine, handling the different cases.  */
int
main ()
{
  int n;

  scanf ("%d\n", &n);
  for (int i = 1; i <= n; ++i)
    {
      printf ("Case #%d: ", i);
      solve_case ();
      printf ("\n");
    }

  return EXIT_SUCCESS;
}
