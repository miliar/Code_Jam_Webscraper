#include <iostream>
#include <stdio.h>
using namespace std ;

int main () {
  freopen( "B-small.in", "r", stdin );
  freopen( "B.out", "w", stdout );
  
  int t, n, cas ;
  double c, f, r, x, totTime ;

  scanf ( "%d" , &t );
  for ( cas = 1 ; cas <= t ; ++cas ){
    
    scanf ( "%lf %lf %lf", &c, &f, &x ) ;
    r = 2 ;

    totTime = 0 ;
    while ( x / r > c / r + x / (r + f) ) {
      
      totTime += c / r ;
      r += f ;

    }
    totTime += x / r ;

    // output
    printf ( "Case #%d: %.7lf\n", cas, totTime );
    
  }
}
