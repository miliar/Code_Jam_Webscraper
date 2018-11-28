#include<iostream>
#include<cstdio>
using namespace std;


int main(){
    int t;
    scanf("%d",&t);
    double c , f , x ;
    for( int tc = 1 ; tc <= t ; ++tc ){
      printf("Case #%d: ",tc);
      scanf("%lf %lf %lf",&c,&f,&x);
      double ans = 1e+100;
      double time = 0;
      for( int i = 0 ; i <= 100003 ; ++i ){
         double tmp = time + x / ( f * i + 2.0 );
         ans = min( ans , tmp );
         time += c/( f * i + 2.0);
      }
      printf("%.7lf\n",ans);
    }
    return 0;
}
