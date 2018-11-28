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
void build(){

}
int n , r , p , s;
void init(){
  n = getint();
  r = getint();
  p = getint();
  s = getint();
  n = 1 << n;
}
char w[]="PRS";
vector<string> ans;
string go( int winner , int round ){
  if( round == n ){
    string ss = "";
    ss += w[ winner ];
    return ss;
  }else{
    string s1 = go( winner , round * 2 );
    string s2 = go( ( winner + 1 ) % 3 , round * 2 );
    if( s1 < s2 ) return s1 + s2;
    else return s2 + s1;
  }
}
inline int trans( char ctmp ){
  if( ctmp == 'P' ) return 0;
  if( ctmp == 'R' ) return 1;
  if( ctmp == 'S' ) return 2;
  return -1;
}
inline void test( string ss ){
  int cnt[ 3 ] = {};
  int len = ss.length();
  for( int i = 0 ; i < len ; i ++ )
    cnt[ trans( ss[ i ] ) ] ++;
  if( cnt[ 0 ] == p &&
      cnt[ 1 ] == r &&
      cnt[ 2 ] == s )
    ans.PB( ss );
}
void solve(){
  ans.clear();
  test( go( 0 , 1 ) );
  test( go( 1 , 1 ) );
  test( go( 2 , 1 ) );
  printf( "Case #%d: " , ++ _cs );
  if( ans.empty() ) puts( "IMPOSSIBLE" );
  else{
    sort( ALL( ans ) );
    printf( "%s\n" , ans[ 0 ].c_str() );
  }
}
int main(){
  build();
  __ = getint();
  while( __ -- ){
    init();
    solve();
  }
}
