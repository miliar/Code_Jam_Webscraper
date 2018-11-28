#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      double C, F, X;
      cin >> C >> F >> X;
      double z = 2;
      double t = X;
      double c = 0;
      while(c < t)
      {
         t = min(t, c + X / z);
         c += C / z;
         z += F;
      }
      cout << "Case #" << test << ": ";
      printf("%.7f\n", t);
   }
   return 0;
}