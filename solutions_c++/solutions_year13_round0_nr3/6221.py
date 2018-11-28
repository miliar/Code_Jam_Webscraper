#include <iostream>
#include <iomanip>
#include <string.h>
#include <math.h>

using namespace std;

bool checkPal(int original)
{
   int rev=0;
   int digit=0;
   int num = original;
   while(num > 0)
   {
      digit = num % 10;
      rev = (rev * 10) + digit;
      num = num / 10;
   }
   if(rev == original) return true;
   return false;
}

bool checkSquare(int num)
{
   int sqr = sqrt(num);
   if((sqr * sqr) == num)
   {
      if(checkPal(sqr)) return true;
   }
   return false;
}

int calcFancySquares(int min, int max)
{
   bool pal, square;
   int count = 0;
   for(int num = min; num <= max; num++)
   {
      pal = checkPal(num);
      square = checkSquare(num);
      if(pal == true && square == true) count++;
   }
   return count;
}


int main()
{
   int testCases;
   int min, max, count;
   cin >> testCases;
   for(int i = 0; i < testCases; i++)
   {
      cin >> min;
      cin >> max;

      count = calcFancySquares(min, max);
      cout << "Case #" << i + 1 << ": " << count  << endl;
   }
   return 0;
}
