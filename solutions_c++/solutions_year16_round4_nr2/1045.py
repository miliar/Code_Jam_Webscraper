#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
double d[17];
double g[17];
int main( void )
{
  ios::sync_with_stdio(false);
  int T, N, K;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    cin >> N >> K;
    for( int i=0; i<N; i++ ){
      cin >> d[i];
    }
    double ret = 0;
    for( int i=0; i<(1<<N); i++ ){
      int j=i,c=0,k=0;
      while( j>0 ){
        if(j&1){
          g[c++] = d[k];
        }
        j >>= 1; k++;
      }
      if( c != K ) continue;
      double r = 0;
      for( int j=0; j<(1<<K); j++ ){
        int k=j, c=0, l=0;
        double rr=1;
        for( int l=0; l<K; l++ ){
          if( k & 1 ){
            rr *= g[l];
            c++;
          } else {
            rr *= (1.0-g[l]);
          }
          k>>=1;
        }
        if( c*2 != K ) continue;
        r += rr;
      }
      ret = max( ret, r );
    }
    printf( "Case #%d: %.12f\n", testcase, ret );
  }
}
