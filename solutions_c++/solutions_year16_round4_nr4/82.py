// eddy1021
#include <bits/stdc++.h>
using namespace std;
typedef double D;
typedef long double LD;
typedef long long ll;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<LD,LD> Pt;
typedef tuple<int,int,int> tiii;
typedef tuple<LL,LL,LL> tlll;
#define mod9 1000000009ll
#define mod7 1000000007ll
#define INF  1023456789ll
#define INF16 10000000000000000ll
#define FI first
#define SE second
#define X FI
#define Y SE
#define PB push_back
#define MP make_pair
#define MT make_tuple
#define eps 1e-9
#define SZ(x) (int)(x).size()
#define ALL(x) (x).begin(), (x).end()
#ifndef ONLINE_JUDGE
#define debug(...) printf(__VA_ARGS__)
#else 
#define debug(...)
#endif
inline ll getint(){
  ll _x=0,_tmp=1; char _tc=getchar();    
  while( (_tc<'0'||_tc>'9')&&_tc!='-' ) _tc=getchar();
  if( _tc == '-' ) _tc=getchar() , _tmp = -1;
  while(_tc>='0'&&_tc<='9') _x*=10,_x+=(_tc-'0'),_tc=getchar();
  return _x*_tmp;
}
inline ll add( ll _x , ll _y , ll _mod = mod7 ){
  ll _ = _x + _y;
  if( _ >= _mod ) _ -= _mod;
  return _;
}
inline ll sub( ll _x , ll _y , ll _mod = mod7 ){
  ll _ = _x - _y;
  if( _ < 0 ) _ += _mod;
  return _;
}
inline ll mul( ll _x , ll _y , ll _mod = mod7 ){
  ll _ = _x * _y;
  if( _ >= _mod ) _ %= _mod;
  return _;
}
ll mypow( ll _a , ll _x , ll _mod ){
  if( _x == 0 ) return 1ll;
  ll _tmp = mypow( _a , _x / 2 , _mod );
  _tmp = mul( _tmp , _tmp , _mod );
  if( _x & 1 ) _tmp = mul( _tmp , _a , _mod );
  return _tmp;
}
ll mymul( ll _a , ll _x , ll _mod ){
  if( _x == 0 ) return 0ll;
  ll _tmp = mymul( _a , _x / 2 , _mod );
  _tmp = add( _tmp , _tmp , _mod );
  if( _x & 1 ) _tmp = add( _tmp , _a , _mod );
  return _tmp;
}
inline bool equal( D _x ,  D _y ){
  return _x > _y - eps && _x < _y + eps;
}
int __ = 1 , _cs;
/*********default*********/
#define N 30
int n;
char c[ N ][ N ];
int msk;
bool okay[ 5 ][ 1 << 16 ];
int p[ N ] , bt[ 1 << 16 ] , sz[ N ];
int find_p( int x ){
  return x == p[ x ] ? x : p[ x ] = find_p( p[ x ] );
}
void Union( int x , int y ){
  x = find_p( x );
  y = find_p( y );
  if( x == y ) return;
  p[ x ] = y;
  sz[ y ] += sz[ x ];
}
int aa[ N ][ N ] , amsk[ N ];
bool test( int in , int jm ){
  int all = 0;
  for( int i = 0 ; i < in ; i ++ ){
    amsk[ i ] = 0;
    for( int j = 0 ; j < in ; j ++ )
      if( ( jm >> ( i * in + j ) ) & 1 ){
        aa[ i ][ j ] = 1;
        amsk[ i ] |= ( 1 << j );
      }else aa[ i ][ j ] = 0;
    all |= amsk[ i ];
    if( amsk[ i ] == 0 ) return false;
  }
  if( all != ( 1 << in ) - 1 ) return false;
  for( int i = 0 ; i < in ; i ++ ) p[ i ] = i , sz[ i ] = 1;
  for( int j = 0 ; j < in ; j ++ ){
    int pre = -1;
    for( int i = 0 ; i < in ; i ++ )
      if( aa[ i ][ j ] ){
        if( pre != -1 ) Union( pre , i );
        pre = i;
      }
  }
  for( int i = 0 ; i < in ; i ++ )
    if( i == find_p( i ) ){
      if( bt[ amsk[ i ] ] != sz[ i ] )
        return false;
      for( int j = 0 ; j < in ; j ++ )
        if( find_p( j ) == i )
          if( amsk[ j ] != amsk[ i ] )
            return false;
    }
  return true;
}
void build(){
  for( int i = 1 ; i < ( 1 << 16 ) ; i ++ )
    bt[ i ] = bt[ i / 2 ] + i % 2;
  for( int i = 1 ; i <= 4 ; i ++ )
    for( int j = 0 ; j < ( 1 << ( i * i ) ) ; j ++ )
      okay[ i ][ j ] = test( i , j );
}
void init(){
  n = getint(); msk = 0;
  for( int i = 0 ; i < n ; i ++ ){
    scanf( "%s" , c[ i ] );
    for( int j = 0 ; j < n ; j ++ )
      if( c[ i ][ j ] == '1' )
        msk |= ( 1 << ( i * n + j ) );
  }
}
int ans;
void solve(){
  ans = n * n;
  for( int i = 0 ; i < ( 1 << ( n * n ) ) ; i ++ )
    if( okay[ n ][ i ] && ( ( i & msk ) == msk ) )
      ans = min( ans , bt[ i ^ msk ] );
  printf( "Case #%d: %d\n" , ++ _cs , ans );
}
int main(){
  build();
  __ = getint();
  while( __ -- ){
    init();
    solve();
  }
}
