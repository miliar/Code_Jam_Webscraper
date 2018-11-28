#include <iostream>
#include <algorithm>
using namespace std;
int main( void )
{
  int T,N,M,a[128][128],b[2][128];
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    cin >> N >> M;
    for( int i=0; i<2; i++ ) for( int j=0; j<128; j++ )
      b[i][j]=0;
    for( int y=0; y<N; y++ ){
      for( int x=0; x<M; x++ ){
        cin >> a[y][x];
        b[0][y] = max( b[0][y], a[y][x] );
        b[1][x] = max( b[1][x], a[y][x] );
      }
    }
    int flag=1;
    for( int y=0; y<N; y++ ){
      for( int x=0; x<M; x++ ){
        if( a[y][x] != min( b[0][y], b[1][x] ) ){
          flag=0;
          goto END;
        }
      }
    }
END:
    cout << "Case #" << testcase << ": " << ((flag) ? "YES" : "NO") << endl;
  }
  return 0;
}
