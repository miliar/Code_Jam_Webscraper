#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

bool is_palindrome (int64_t num)
{
  int64_t tmp = num, reversed = 0;
  
  // if the last digit is zero, automatically not a palindrome
  if (tmp%10 == 0)
    return false;
  
  do {
  
    reversed *= 10;
    reversed += tmp%10;
    tmp /= 10;
  
  } while (tmp > 0);
  
  return (reversed == num);
}

bool is_fair_and_square (int64_t num)
{
  bool res = false;
  long double root = sqrt(num);
  
  double decimal = root - (long long) root;

//  printf("num=%lld, root=%Lf, dec=%f\n", num, root, decimal);
  if (decimal == 0) {
//    printf("found perfect square: num=%lld, root=%Lf\n", num, root);
    res = is_palindrome (root);
  }

  return res;
}

int main (void)
{
  int num_cases = 0;
  int64_t lower, upper;
  int pcount = 0;
  
  scanf ("%d", &num_cases);
  
  for (int curr_case = 1; curr_case <= num_cases; curr_case++)
  {
    scanf("%lld", &lower);
    scanf("%lld", &upper);
    
    pcount = 0;

    for (int64_t curr = lower; curr <= upper; curr++) {
        if ( is_palindrome (curr) ) {
  //        printf ("Found palindrome: %lld\n", curr);
          if ( is_fair_and_square (curr) ) {
            pcount++;
          }
        }
    }
    
    printf ("Case #%d: %d\n", curr_case, pcount);
  }

  return 0;
}
