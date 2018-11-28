#include "stdio.h"

const double INF = 1000000000000.0;

int main(){

  FILE *fp = fopen( "B-large.in" , "r" );
  FILE *fo = fopen( "clout" , "w" );

  int n;
  fscanf( fp , "%d" , &n );

  for( int t = 1; t <= n; t++ ){
    double c , f , x;
    fscanf( fp , "%lf %lf %lf" , &c , &f , &x );
    double cps = 2.0;
    double ans = INF;
    double time = 0;
    while( ans > time ){
      if( ans > time + x / cps ) ans = time + x / cps;
      time += c / cps;
      cps += f;
    }
    fprintf( fo , "Case #%d: %.7lf\n" , t , ans );
  }
  
  return 0;
}
