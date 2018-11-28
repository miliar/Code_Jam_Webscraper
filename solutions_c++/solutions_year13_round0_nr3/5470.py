/********************************************************
 * Compiler: gcc version 3.2.3
 * To compile: g++ fair_small.cc -o fair_small
 * To run: ./fair_small <input file>
 ********************************************************/

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool isPalin(int pl)
{
   int reverse = 0, temp;

   temp = pl;

   while( temp != 0 )
   {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
   }

   if ( pl == reverse )
      return true;
   else
      return false;
}

int findFair(int lower, int upper)
{
  int totalPal = 0;
  for (int i = lower; i <= upper; ++i)
  {
    if (isPalin(i) == true)
    {
      int ii = (int)sqrt(double(i));
      if (ii * ii == i || (ii+1) * (ii+1) == i)
        if (isPalin(ii) == true)
          ++totalPal;
    }
  }
  return totalPal;
}


main(char argsc, char *argv[])
{
   int tc = 0, result = -1, lower = 0, upper = 0;

   ifstream in_file;
   in_file.open(argv[1]);

   in_file >> tc;

   if (tc < 1 || tc > 10)
      exit (0);

   int line = 0;
   while (line < tc)
   {
     in_file >> lower >> upper;
     ++line;

     result = findFair(lower, upper);
     cout << "Case #" << line << ": " << result << endl;
     result = -1;
   }
   in_file.close();
}
