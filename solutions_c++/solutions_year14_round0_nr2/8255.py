#include <bits/stdc++.h>
using namespace std ;


int main()
{
 double x,f,ans,rate ,cookies,cost ,r1 ,r2  ;
 int tc ;
 scanf("%d",&tc);
 for ( int loopVar = 1 ; loopVar <= tc ; loopVar++ ){
 	  scanf("%lf %lf %lf",&cost , &f , &x);
      r1 = r2 = ans = cookies = 0.0 ;
      rate = 2.0 ;
      while (1){
          if ( cookies >= x)
          break ;

          r1 = ((x-cookies)/rate) ;
          r2 = (cost/rate) +(x/(rate+f)) ;
          if ( r1 < r2){
          	 ans += r1 ; cookies = x ;
          }
          else {
          	   ans += (cost/rate) ;
          	   rate += f ;
          	   cookies = 0.0 ;
          }
      }
      printf("Case #%d: %0.7lf\n",loopVar,ans);
 }


	return 0 ;
}
