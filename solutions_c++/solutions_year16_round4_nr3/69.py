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
#define N 200
void build(){

}
int R , C , ii[ N ] , l[ N ];
void init(){
  R = getint();
  C = getint();
  for( int i = 1 ; i <= 2 * ( R + C ) ; i ++ )
    ii[ i ] = getint();
  for( int i = 1 ; i <= 2 * ( R + C ) ; i += 2 ){
    l[ ii[ i     ] ] = ii[ i + 1 ];
    l[ ii[ i + 1 ] ] = ii[ i     ];
  }
}
bool mz[ N ][ N ];
int dr[]={1,0,-1,0};
int dc[]={0,-1,0,1};
int dir( int ndir , bool s ){
  if( !s ) return ndir ^ 1;
  return 3 - ndir;
}
inline bool in( int nr , int nc ){
  return 1 <= nr && nr <= R &&
         1 <= nc && nc <= C;
}
int tag[ N ][ N ] , stp;
inline int trans( int nr , int nc ){
  if( nr == 0 ) return nc;
  if( nr > R ) return R + C + C - nc + 1;
  if( nc == 0 ) return R + C + C + R - nr + 1;
  return C + nr;
}
int go( int ndir , int nr , int nc ){
  if( tag[ nr ][ nc ] == stp ) return -1;
  tag[ nr ][ nc ] = stp;
  int nxtdir = dir( ndir , mz[ nr ][ nc ] );
  int nxtr = nr + dr[ nxtdir ];
  int nxtc = nc + dc[ nxtdir ];
  if( !in( nxtr , nxtc ) ) return trans( nxtr , nxtc );
  return go( nxtdir , nxtr , nxtc );
}
bool test( int msk ){
  for( int i = 0 ; i < R ; i ++ )
    for( int j = 0 ; j < C ; j ++ )
      if( ( msk >> ( i * C + j ) ) & 1 )
        mz[ i + 1 ][ j + 1 ] = true;
      else mz[ i + 1 ][ j + 1 ] = false;
  for( int i = 1 ; i <= C ; i ++ ){
    stp ++;
    if( go( 0 , 1 , i ) != l[ trans( 0 , i ) ] )
      return false;
    stp ++;
    if( go( 2 , R , i ) != l[ trans( R + 1 , i ) ] )
      return false;
  }
  for( int i = 1 ; i <= R ; i ++ ){
    stp ++;
    if( go( 1 , i , C ) != l[ trans( i , C + 1 ) ] )
      return false;
    stp ++;
    if( go( 3 , i , 1 ) != l[ trans( i , 0 ) ] )
      return false;
  }
  for( int i = 0 ; i < R ; i ++ , puts( "" ) )
    for( int j = 0 ; j < C ; j ++ )
      if( ( msk >> ( i * C + j ) ) & 1 ) putchar( '\\' );
      else putchar( '/' );
  return true;
}
void solve(){
  printf( "Case #%d:\n" , ++ _cs );
  bool okay = false;
  for( int i = 0 ; i < ( 1 << ( R * C ) ) && !okay ; i ++ )
    okay = test( i );
  if( !okay ) puts( "IMPOSSIBLE" );
}
int main(){
  build();
  __ = getint();
  while( __ -- ){
    init();
    solve();
  }
}
