#include <iostream>
using namespace std;
int main( void )
{
  int T,A,B,K;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    int ret=0;
    cin >> A >> B >> K;
    for( int i=0; i<A; i++ ){
      for( int j=0; j<B; j++ ){
        int C = i&j;
        if( C < K ) ret++;
      }
    }
    cout << "Case #" << testcase << ": " << ret << endl;
  }
  return 0;
}
