#include <iostream>
using namespace std;

#define MAX_N 1000002

double lnFac[MAX_N];
double lnOf2;

double binProb(int n, int k) // fac[n]/(fac[k]*(fac[n-k])*2^n)
{
   double ln2PowN = n * lnOf2;
   double lnRet = lnFac[n] - (lnFac[k] + lnFac[n-k] + ln2PowN);
   if (lnRet > 0.00001)
   {
      cout << "ERROR!" << endl;
   }
   return exp(lnRet);
}

double calcProb(int toAdd, int filled, int x, int y)
{
   // filled = 1: 1x1 filled
   // filled = 3: 3x3 filled
   // ...
   if (x + y <= filled) // Equal is not needed
      return 1.0;
   if (x + y > filled+2)
      return 0.0;
   if (x == 0) // Will the top one exist?
      return 0.0; // No, then that layer would have been filled.

   int sideLength = filled + 1; // Excluding the top.
   int minFilledEachSide = max(toAdd - sideLength, 0);
   double ret = 0;
   for (int i = 0; i <= toAdd; ++i)
   {
      int left = max(i, minFilledEachSide);
      int right = toAdd - left;
      double iProb = binProb(toAdd, i);
      if (left > y)
         ret += iProb;
   }
   return ret;
}

int main()
{
   lnOf2 = log(2.0);
   lnFac[0] = 0;
   lnFac[1] = 0;
   for (int i = 2; i < 20; ++i)
   {
      lnFac[i] = lnFac[i-1] + log((double)i);
      // cout << exp(lnFac[i]) << endl;
   }

   int T;
   cin >> T;
   for (int t = 0; t < T; ++t)
   {
      int n, x, y;
      cin >> n >> x >> y;
      int filled;
      int leftToAdd = n;
      for (filled = 1; ; filled += 2)
      {
         int area = filled*(filled+1) / 2;
         if (area > n)
            break;
         leftToAdd = n - area;
      }
      filled -= 2;
      double prob = calcProb(leftToAdd, filled, abs(x), y);
      cout << "Case #" << (t+1) << ": " << prob << endl;
   }
   return 0;
}
