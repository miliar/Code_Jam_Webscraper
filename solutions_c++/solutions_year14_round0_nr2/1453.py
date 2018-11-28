#include <cstdio>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

const int CARDS = 16;

int main() {
   int n;
   scanf("%d", &n);
   
   for (int t = 1; t <= n; ++t) {
      //c = cookies per farm
      //f = rate increase per farm
      //x = target cookies
      double c, f, x;
      double rate = 2;
      double myCookies = 0;
      double timeTaken = 0;
      double timeToFarm = 0;
      
      scanf("%lg %lg %lg", &c, &f, &x);
      
      double timeToWin;
      double timeToWinWithFarm;
      
      timeToWin = (x - myCookies) / rate;
      timeToFarm = (c - myCookies) / rate;
      timeToWinWithFarm = (x - myCookies) / (rate + f);
      
      while (timeToWin > (timeToFarm + timeToWinWithFarm)) {
         timeTaken += timeToFarm;
         rate += f;
         
         timeToWin = (x - myCookies) / rate;
         timeToFarm = (c - myCookies) / rate;
         timeToWinWithFarm = (x - myCookies) / (rate + f);
      }
      
      timeTaken += timeToWin;
      
      printf("Case #%d: %f\n", t, timeTaken);
   }
   
   
   
   return 0;
}