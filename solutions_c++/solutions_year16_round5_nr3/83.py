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
#define N 1021
int n , s;
int x[ N ] , y[ N ] , z[ N ];
void build(){

}
void init(){
  n = getint();
  s = getint();
  for( int i = 0 ; i < n ; i ++ ){
    x[ i ] = getint();
    y[ i ] = getint();
    z[ i ] = getint();
    int dump = getint();
    dump = getint();
    dump = getint();
  }
}
D dst[ N ];
bool got[ N ];
inline D sqr( D _x ){ return _x * _x; }
inline D dist( int i , int j ){
  return sqrt( sqr( x[ i ] - x[ j ] ) +
               sqr( y[ i ] - y[ j ] ) +
               sqr( z[ i ] - z[ j ] ) );
}
inline D cal(){
  for( int i = 0 ; i < n ; i ++ ){
    dst[ i ] = 1e20;
    got[ i ] = false;
  }
  dst[ 0 ] = 0.0;
  for( int _ = 0 ; _ < n ; _ ++ ){
    int bst = -1;
    for( int i = 0 ; i < n ; i ++ )
      if( !got[ i ] && ( bst == -1 ||
                         dst[ i ] < dst[ bst ] ) )
        bst = i;
    got[ bst ] = true;
    for( int i = 0 ; i < n ; i ++ )
      dst[ i ] = min( dst[ i ] , max( dst[ bst ] , dist( bst , i ) ) );
  }
  return dst[ 1 ];
}
void solve(){
  printf( "Case #%d: %.12f\n" , ++ _cs , cal() );
}
int main(){
  build();
  __ = getint();
  while( __ -- ){
    init();
    solve();
  }
}
