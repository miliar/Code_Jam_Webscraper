#include <bits/stdc++.h>
using namespace std ;


int main(){
 double cost , f , x ,t1 ,t2 ,ans,rate ,cookies ;
      
 int test ;
 scanf("%d",&test);
 for ( int kase = 1 ; kase <= test ; kase++ ){
 	  scanf("%lf %lf %lf",&cost , &f , &x);
      t1 = t2 = ans = cookies = 0.0 ;
      rate = 2.0 ;
      while (1){
          if ( cookies >= x)
          break ;

          t1 = ((x-cookies)/rate) ;
          t2 = (cost/rate) +(x/(rate+f)) ;
          if ( t1 < t2){
          	 ans += t1 ; cookies = x ;
          }
          else {
          	   ans += (cost/rate) ;
          	   rate += f ;
          	   cookies = 0.0 ;
          }
      }
      printf("Case #%d: %0.7lf\n",kase,ans);
 }


	return 0 ;
}