#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

long long pgcd(long long a, long long b)
{
   return b == 0 ? a : pgcd(b, a % b);
}

int f(long long n)
{
   int r = 0;
   while(n > 1)
   {
      n /= 2;
      r++;
   }
   return r;
}


int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      long long a, b;
      scanf("%lld/%lld", &a, &b);
      long long p = pgcd(a, b);
      a /= p;
      b /= p;
      int r = f(b);
      if(b != 1 << r)
         cout << "Case #" << test << ": " << "impossible" << endl;
      else
         cout << "Case #" << test << ": " << r - f(a) << endl;
   }
   return 0;
}