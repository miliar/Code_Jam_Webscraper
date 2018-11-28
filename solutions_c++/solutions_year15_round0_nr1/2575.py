#include <iostream>
#include <string>
using namespace std;
int main( void )
{
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for( int ti = 1; ti <= T; ti++ ){
    int N;
    string S;
    cin >> N >> S;
    N++;
    int d = 0;
    int ret = 0;
    for( int i=0; i<N; i++ ){
      if( d < i ){
        ret += i - d;
        d = i;
      }
      d += S[i] - '0';
    }
    cout << "Case #" << ti << ": " << ret << endl;
  }
}
