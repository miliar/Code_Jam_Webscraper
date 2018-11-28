#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using namespace std;

void myIToA(unsigned long long num, char* str)
{
  int count = 0;
  do{
    str[count++] = '0' + num%10;
    num = num/10;
  } while(num);
  str[count] = '\0';
}

int isPalindrome(unsigned long long &num)
{
  char str[50];
  myIToA(num, str);

  int len = strlen(str);
  for (int i = 0; i <= (len-1)/2; i++)
    {
      if (str[i] != str[len - 1 -i])
        {
          return 0;
        }
    }
  return 1;
}

int checkFairSqaure(unsigned long long &A, unsigned long long &B)
{
  unsigned long long a1 = sqrt(A);
  unsigned long long a2 = sqrt(B);
  if (a1*a1 != A) {
      a1+=1;
  }
  unsigned long long mul = (a1-1)*(a1-1);
  int count = 0;
  for(unsigned long long i = a1; i <= a2; i++)
    {
      mul = mul + 1 + 2*(i-1);
      if (isPalindrome(i) && isPalindrome(mul))
        {
          count++;
        }
    }
  return count;
}

int main()
{
  int num_cases = 0;
  scanf("%d", &num_cases);
  unsigned long long A, B;
  for (int i = 0; i < num_cases; i++)
    {
      scanf("%llu %llu", &A, &B);
//      printf("%llu %llu\n", A, B);
      printf ("Case #%d: %d\n", i+1, checkFairSqaure(A,B));
    }
  return 0;
}

