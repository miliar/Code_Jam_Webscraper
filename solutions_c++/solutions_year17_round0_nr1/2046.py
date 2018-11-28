#include <iostream>
#include <string>
using namespace std;
int main()
{
  ios::sync_with_stdio(false);
  int T, K;
  string S;
  cin >> T;
  for( int testcase = 1; testcase <= T; testcase++ ){
    cin >> S >> K;
    int L = S.size();
    int ret = 0;
    for( int i = 0; i <= L - K; i++ ){
      if( S[i] == '-' ){
        ret++;
        for( int j=0; j<K; j++ ){
          if( S[i+j] == '-' ) S[i+j] = '+';
          else S[i+j] = '-';
        }
      }
    }
    int f = 1;
    for( int i = L-K+1; i < L; i++ ){
      if( S[i] == '-' ){
        f = 0;
        break;
      }
    }
    if( f ) cout << "Case #" << testcase << ": " << ret << endl;
    else cout << "Case #" << testcase << ": IMPOSSIBLE" << endl;
  }
}
