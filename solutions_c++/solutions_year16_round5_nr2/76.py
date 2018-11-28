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
#define N 111
void build(){
  srand( 10211021 );
}
int n , p[ N ] , m , len[ N ] , cnt[ N ];
vector<int> v[ N ];
char cc[ N ] , c[ N ][ N ];
int go( int now ){
  int tcnt = 1;
  for( int x : v[ now ] )
    tcnt += go( x );
  return cnt[ now ] = tcnt;
}
void init(){
  n = getint();
  for( int i = 1 ; i <= n ; i ++ ){
    v[ i ].clear();
    cnt[ i ] = 0;
  }
  for( int i = 1 ; i <= n ; i ++ ){
    p[ i ] = getint();
    if( p[ i ] )
      v[ p[ i ] ].PB( i );
  }
  scanf( "%s" , cc + 1 );
  m = getint();
  for( int i = 0 ; i < m ; i ++ ){
    scanf( "%s" , c[ i ] );
    len[ i ] = strlen( c[ i ] );
  }
  for( int i = 1 ; i <= n ; i ++ )
    if( p[ i ] == 0 )
      go( i );
}
#define K 220000
int got[ N ] , deg[ N ];
char kk[ N ];
bool in[ N ];
set< int > S;
inline bool match( int idx ){
  for( int i = 1 ; i + len[ idx ] - 1 <= n ; i ++ )
    for( int j = 0 ; j < len[ idx ] ; j ++ ){
      if( kk[ i + j ] != c[ idx ][ j ] ) break;
      if( j + 1 == len[ idx ] )
        return true;
    }
  return false;
}
int v2;
inline void gen(){
  v2 = 0;
  vector<int> vv;
  for( int i = 1 ; i <= n ; i ++ )
    in[ i ] = false;
  for( int i = 1 ; i <= n ; i ++ )
    if( p[ i ] == 0 ){
      vv.PB( i );
      in[ i ] = true;
    }
  for( int i = 1 ; i <= n ; i ++ ){
    int sum = 0 , x = 0;
    for( int j : vv ) sum += cnt[ j ];
    int u = rand() % sum , pre = 0;
    for( int j = 0 ; j < (int)vv.size() ; j ++ ){
      pre += cnt[ vv[ j ] ];
      if( pre > u ){
        x = vv[ j ];
        swap( vv[ j ] , vv.back() );
        vv.pop_back();
        break;
      }
    }
    kk[ i ] = cc[ x ];
    v2 = add( mul( v2 , 13131 ) , x );
    for( int nxt : v[ x ] )
      if( !in[ nxt ] ){
        vv.PB( nxt );
        in[ nxt ] = true;
      }
  }
}
inline D adjust( D x ){
  if( x > 0.97 ) return 0.97;
  if( x < 0.03 ) return 0.03;
  return x;
}
void solve(){
  for( int i = 0 ; i < m ; i ++ )
    got[ i ] = 0;
  S.clear();
  int all = 0;
  for( int i = 0 ; i < K ; i ++ ){
    gen();
    if( S.count( v2 ) ) continue;
    S.insert( v2 );
    all ++;
    for( int j = 0 ; j < m ; j ++ )
      if( match( j ) )
        got[ j ] ++;
  }
  cerr << _cs << " " << all << endl;
  if( all == 0 ) all ++;
  printf( "Case #%d:" , ++ _cs );
  for( int i = 0 ; i < m ; i ++ )
    printf( " %.6f" , adjust( (D)got[ i ] / (D)all ) );
  puts( "" );
}
int main(){
  build();
  __ = getint();
  while( __ -- ){
    init();
    solve();
  }
}
