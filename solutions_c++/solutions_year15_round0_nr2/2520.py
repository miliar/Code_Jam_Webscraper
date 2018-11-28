#include <iostream>
#include <algorithm>
using namespace std;
int main( void )
{
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for( int ti=1; ti<=T; ti++ ){
    int D, d[1024];
    cin >> D;
    int ret = 0;
    for( int i=0; i<D; i++ ){
      cin >> d[i];
      ret = max( ret, d[i] );
    }
    for( int i=1; i<=500; i++ ){
      int r = i;
      for( int j=0; j<D; j++ ){
        if( d[j] > i ){
          int a = d[j] - i;
          a = a/i + ((a%i==0)?0:1);
          r += a;
        }
      }
      ret = min( ret, r );
    }
    cout << "Case #" << ti << ": " << ret << endl;
  }
}
