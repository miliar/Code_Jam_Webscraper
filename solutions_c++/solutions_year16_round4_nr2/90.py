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
#define eps 1e-12
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
#define N 222
void build(){

}
int n , k;
D prob[ N ];
vector<D> vv;
void init(){
  n = getint();
  k = getint();
  vv.clear();
  for( int i = 1 ; i <= n ; i ++ ){
    scanf( "%lf" , &prob[ i ] );
    vv.PB( prob[ i ] );
  }
  sort( ALL( vv ) );
}
D nprob[ N ];
D dp[ N ][ N ];
D cal(){
  dp[ 0 ][ 0 ] = 1.0;
  for( int i = 1 ; i <= k ; i ++ )
    for( int j = 0 ; j <= i ; j ++ ){
      dp[ i ][ j ] = dp[ i - 1 ][ j ] * ( 1.0 - nprob[ i ] );
      if( j )
        dp[ i ][ j ] += dp[ i - 1 ][ j - 1 ] * nprob[ i ];
    }
  return dp[ k ][ k / 2 ];
}
void solve(){
  D ans = 0.0;
  for( int l = 0 ; l <= k ; l ++ ){
    int got = 1;
    for( int j = 1 ; j <= l ; j ++ )
      nprob[ got ++ ] = vv[ j - 1 ];
    for( int j = 1 ; j <= k - l ; j ++ )
      nprob[ got ++ ] = vv[ n - j ];
    ans = max( ans , cal() );
  }
  printf( "Case #%d: %.12f\n" , ++ _cs , ans );
}
int main(){
  build();
  __ = getint();
  while( __ -- ){
    init();
    solve();
  }
}
