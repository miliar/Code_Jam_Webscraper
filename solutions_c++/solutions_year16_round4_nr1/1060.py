#include <iostream>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
typedef pair<int,int> P;
string tbl[3] = {"R","P","S"};
map< P, string > m;
string dfs( int t, int N ){
  if( N == 0 ) return tbl[t];
  if( m.find( P(t,N) ) != m.end() ){
    return m[P(t,N)];
  }
  string ret0,ret1;
  if( t == 0 ){
    ret0 = dfs( 0, N-1 );
    ret1 = dfs( 2, N-1 );
  } else if( t == 1 ){
    ret0 = dfs( 0, N-1 );
    ret1 = dfs( 1, N-1 );
  } else {
    ret0 = dfs( 1, N-1 );
    ret1 = dfs( 2, N-1 );
  }
  if( ret0 < ret1 ){
    m[P(t,N)] = ret0.append( ret1 );
  } else {
    m[P(t,N)] = ret1.append( ret0 );
  }
  return m[P(t,N)];
}
int main( void )
{
  ios::sync_with_stdio(false);
  int T, N, R, P, S;
  cin >> T;
  for( int testcase=1; testcase<=T; testcase++ ){
    cin >> N;
    cin >> R >> P >> S;
    int d[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
    d[0][0] = 1;
    d[1][1] = 1;
    d[2][2] = 1;
    for( int i=0; i<N; i++ ){
      for( int j=0; j<3; j++ ){
        int dd[3] = {0,0,0};
        dd[0] += d[j][0]; dd[2] += d[j][0];
        dd[0] += d[j][1]; dd[1] += d[j][1];
        dd[1] += d[j][2]; dd[2] += d[j][2];
        d[j][0] = dd[0]; d[j][1] = dd[1]; d[j][2] = dd[2];
      }
    }
    string ret;
    if( R == d[0][0] && P == d[0][1] && S == d[0][2] ){
      ret = dfs(0,N);
    } else if( R == d[1][0] && P == d[1][1] && S == d[1][2] ){
      ret = dfs(1,N);
    } else if( R == d[2][0] && P == d[2][1] && S == d[2][2] ){
      ret = dfs(2,N);
    } else {
      ret = "IMPOSSIBLE";
    }
    cout << "Case #" << testcase << ": " << ret << endl;
  }
}
