#include <iostream>
#include <string>
using namespace std;
int d[10005];
int M[4][4] =
{
  { 0, 1, 2, 3},
  { 1, 0, 3, 2},
  { 2, 3, 0, 1},
  { 3, 2, 1, 0},
};
int S[4][4] =
{
  { 1, 1, 1, 1},
  { 1,-1, 1,-1},
  { 1,-1,-1, 1},
  { 1, 1,-1,-1},
};
int dfs( int v, int s, int a, int idx, int LX )
{
  if( a == 4 && idx == LX ) return 1;
  if( a == 4 ) return 0;
  if( idx == LX ) return 0;
  int nv = M[v][d[idx]];
  int ns = s * S[v][d[idx]];
  if( nv == a && ns == 1 ){
    int ret = dfs( 0, 1, a+1, idx+1, LX );
    if( ret ) return ret;
  }
  return dfs( nv, ns, a, idx+1, LX );
}
int main( void )
{
  int T,L,X;
  string str;
  cin >> T;
  for( int ti=1; ti<=T; ti++ ){
    cin >> L >> X;
    cin >> str;
    for( int i=0; i<L; i++ ){
      if     ( str[i] == 'i' ) d[i] = 1;
      else if( str[i] == 'j' ) d[i] = 2;
      else                     d[i] = 3;
    }
    for( int i=1; i<X; i++ ){
      for( int j=0; j<L; j++ ){
        d[i*L+j] = d[j];
      }
    }
    int ret = dfs( 0, 1, 1, 0, L*X );
    if( ret ){
      cout << "Case #" << ti << ": YES" << endl;
    } else {
      cout << "Case #" << ti << ": NO" << endl;
    }
  }
}
