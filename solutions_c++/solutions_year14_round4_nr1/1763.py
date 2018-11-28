#include <iostream>
#include <algorithm>
using namespace std;
int S[10005];
int main( void )
{
  int T,N,X;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    cin >> N >> X;
    for( int i=0; i<N; i++ ) cin >> S[i];
    sort( S, S+N );
    int ret=0;
    int i=0,j=N-1;
    while( i<=j ){
      if( i==j ){ ret++; break; }
      if( S[j] + S[i] <= X ){
        ret++; i++; j--;
      } else {
        ret++; j--;
      }
    }
    cout << "Case #" << testcase << ": " << ret << endl;
  }

}
