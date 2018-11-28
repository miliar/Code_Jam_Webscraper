#include <cstdio>

double cookies, cookiesps = 2.0;
double farm, pps, cost;
int t;
double ret, sol, res;

int main(){
    
    scanf( "%d", &t );
    
    for( int k = 0; k < t; ++k ){
      scanf( "%lf%lf%lf", &farm, &pps, &cost );
      while( 1 ){
        if( cost / cookiesps > farm / cookiesps + cost / ( cookiesps+pps ) ){
          sol += farm / cookiesps;
          cookiesps += pps;
        }
        else{
          sol += cost / cookiesps;
          break;
        }
      }
      printf( "Case #%d: %.7lf\n", k+1, sol );
      sol = 0.0;
      cookiesps = 2.0;
    }
      
    return 0;   
}
