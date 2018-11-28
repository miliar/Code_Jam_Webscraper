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
#define N 101010
void build(){

}
int len;
char c[ N ];
void init(){
  scanf( "%s" , c );
  len = strlen( c );
}
bool got[ 55 ][ 55 ];
int dp[ 55 ][ 55 ];
int DP( int l , int r ){
  if( r - l < 1 ) return 0;
  if( r - l == 1 ) return c[ l ] == c[ r ] ? 10 : 5;
  if( got[ l ][ r ] ) return dp[ l ][ r ];
  got[ l ][ r ] = true;
  int tdp = 0;
  for( int i = l + 2 ; i < r ; i += 2 )
    tdp = max( tdp , DP( l , i - 1 ) + DP( i , r ) );
  return dp[ l ][ r ] = tdp;
}
void solve(){
  int ans = 0;
  vector<int> v;
  for( int i = 0 ; i < len ; i ++ ){
    int now = ( c[ i ] == 'C' ? 0 : 1 );
    if( v.size() && now == v.back() ){
      v.pop_back();
      ans += 10;
    }else v.push_back( now );
  }
  int sz = (int)v.size();
  for( int l = 0 , r = sz - 1 ; l < r ; l ++ , r -- )
    ans += ( v[ l ] == v[ r ] ? 10 : 5 );
  if( len <= 50 ){
    for( int i = 0 ; i < len ; i ++ )
      for( int j = 0 ; j < len ; j ++ )
        got[ i ][ j ] = false;
    int tans = DP( 0 , len - 1 );
    if( tans > ans ){
      ans = tans;
      cerr << "better" << endl;
    }
  }
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
