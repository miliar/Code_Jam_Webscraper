#include <bits/stdc++.h>

using namespace std;

int k, n;
double ori[16];
double t[16];

double f(int p, int a, int b)
{
   if(p == k)
      return a == b;
   return t[p] * f(p+1, a+1, b) + (1 - t[p]) * f(p+1, a, b+1);
}

double g(int i, int j)
{
   if(i == k)
      return f(0, 0, 0);
   double r = 0;
   while(n - j >= k - i)
   {
      t[i] = ori[j];
      r = max(r, g(i+1, ++j));
   }
   return r;
}

int main()
{
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      cin >> n >> k;
      for(int i=0; i<n; i++)
         cin >> ori[i];
      printf("Case #%d: %.9f\n", test, g(0, 0));
   }
   return 0;
}