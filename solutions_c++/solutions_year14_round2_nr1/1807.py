#include <iostream>
#include <string>
using namespace std;
#define ABS(x) ((x)<0?-(x):(x))
int C;
char c[105];
int len[105][105];
int main( void )
{
  int T,N;
  string s,t;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    cin >> N;
    int fegla=0;
    for( int i=0; i<N; i++ ){
      cin >> s;
      if( i==0 ) C=0;
      int cc=0;
      char prev=s[0];
      int k=0;
      for( int j=1; j<=s.size(); j++ ){
        if( j == s.size() || s[j] != prev ){
          if( i==0 ){
            c[C] = prev;
            len[C][0] = j-k;
            C++;
          } else {
            if( c[cc] != prev ){ cc=-1; break; }
            len[cc][i] = j-k;
            cc++;
          }
          prev = s[j];
          k = j;
        }
      }
      if( i>0 && cc != C ) fegla = 1;
    }
    if( fegla ){
      cout << "Case #" << testcase << ": Fegla Won" << endl;
    } else {
      int ret = 0;
      for( int i=0; i<C; i++ ){
        int sum=0;
        for( int j=0; j<N; j++ ){
          sum += len[i][j];
        }
        int ave = (sum*2+1) / (N*2);
        sum=0;
        for( int j=0; j<N; j++ ){
          sum += ABS( ave - len[i][j] );
        }
        ret += sum;
      }
      cout << "Case #" << testcase << ": " << ret << endl;
    }
  }
  return 0;
}
