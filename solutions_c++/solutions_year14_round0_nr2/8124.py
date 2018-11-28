#include <bits/stdc++.h>
using namespace std ;


int main()
{
 double cost ,l1 ,l2 ,x,f,ans,rate ,cookies ;
 int noOfTestCase ;
 scanf("%d",&noOfTestCase);
 for ( int loopVar = 1 ; loopVar <= noOfTestCase ; loopVar++ ){
 	  scanf("%lf %lf %lf",&cost , &f , &x);
      l1 = l2 = ans = cookies = 0.0 ;
      rate = 2.0 ;
      while (1){
          if ( cookies >= x)
          break ;

          l1 = ((x-cookies)/rate) ;
          l2 = (cost/rate) +(x/(rate+f)) ;
          if ( l1 < l2){
          	 ans += l1 ; cookies = x ;
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
