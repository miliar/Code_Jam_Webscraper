#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <iterator>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <cassert>

using namespace std;


const double EPS = 0.00000001;
double C,F,X;
double noFTime(double cookies, double f)
{
   return (X-cookies)/f;

}

double withFTime(double cookies, double f)
{
   double reqCookies = max(0.0, C - cookies);
   double reqTime = reqCookies/f;
   cookies += (reqCookies - C);
   return reqTime +  max(0.0, X- cookies)/(f + F);
}

bool isEqual(double f1, double f2)
{

   return fabs(f1-f2) <= EPS;
}
int main()
{
   freopen("B-small-attempt0.in", "r", stdin);
   freopen("B-small.out", "w", stdout);

   int T;
   scanf("%d", &T);

   for(int tc = 1; tc <= T; tc++) {
      double cookies = 0.0, f = 2.0;
      scanf("%lf %lf %lf", &C, &F, &X);
      double timeTaken = 0.0;
      int cnt = 0;
      while(fabs(X-cookies) != EPS && cookies < X) {
         double nft = noFTime(cookies, f);
         double wft = withFTime(cookies, f);
         if(!isEqual(wft, nft) && wft < nft) {
            cookies  += max(0.0, C - cookies);
            cookies -= C;
            timeTaken += max(0.0, C - cookies) / f;
            f += F;
         }else {
            timeTaken += (X - cookies)/f;
            cookies += (X - cookies);
         }



      }
      printf("Case #%d: %.7lf\n", tc, timeTaken);
   }
   return 0;
}

