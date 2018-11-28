#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cfloat>
using namespace std;
int main( void )
{
  int T;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    double C, F, X;
    cin >> C >> F >> X;
    double ans = DBL_MAX; 
    double t = 0;
    double r = 2;
    while( t < ans ){
      double aa = t + X/r;
      ans = min( ans, aa );
      t += C / r;
      r += F;
    } 
    printf( "Case #%d: %.7f\n", testcase, ans );
  }
  return 0;
}
