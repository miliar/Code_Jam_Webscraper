#include<stdio.h>

int main()
{
   int N, i=0;
   long double C, F, X;
   long double sec, cookie, cookie_sec, now_sec, next_sec, next_cookie;
   scanf("%d",&N);
   while( i++ < N )
   {
      scanf("%Lf %Lf %Lf",&C,&F,&X);
      sec = 0.0;
      cookie = 2.0;
      now_sec = X/cookie;
      while(1)
      { 
         cookie_sec = (C/cookie);
         next_cookie = cookie+F;
         next_sec = (X/next_cookie);
         if( now_sec < cookie_sec + next_sec )   break;

         cookie = next_cookie;
         sec += cookie_sec;
         now_sec = next_sec;
      }
      printf("Case #%d: %.7Lf\n", i, sec+now_sec);
   }
   return 0;
}
