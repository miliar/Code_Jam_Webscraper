#include <bits/stdc++.h>
 
#define FOR(i,a,b) for( ll i = (a); i < (ll)(b); i++ )
#define REP(i,n) FOR(i,0,n)
#define YYS(x,arr) for(auto& x:arr)
#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort( (x).begin(),(x).end() )
#define REVERSE(x) reverse( (x).begin(),(x).end() )
#define UNIQUE(x) (x).erase( unique( ALL( (x) ) ) , (x).end() )
#define PW(x) (1LL<<(x))
#define SZ(x) ((ll)(x).size())

#define pb emplace_back
#define fi first
#define se second

using namespace std;

typedef long double ld;
typedef long long int ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<ld> vd;
typedef vector<pi> vpi;
typedef vector<pl> vpl;
typedef vector<vpl> gr;
typedef vector<vl> ml;
typedef vector<vd> md;
typedef vector<vi> mi;

const ll INF = (ll)1e9 + 10;
const ll INFLL = (ll)1e18 + 10;
const ld EPS = 1e-10;
const ll MOD = 1e9+7;

template<class T> T &chmin( T &a , const T &b ){ return a = min(a,b); }
template<class T> T &chmax( T &a , const T &b ){ return a = max(a,b); }

template<class T> inline T sq( T a ){ return a * a; }

// head

int n;
int r, s, p;
int tc;


string rec( string cur , int d ){
  if( SZ(cur) == PW(n) ){
    int cntr = 0, cnts = 0, cntp = 0;
    YYS( w , cur ){
      if( w == 'P' ) cntp++;
      if( w == 'R' ) cntr++;
      if( w == 'S' ) cnts++;
    }
    if( cnts == s && cntr == r && cntp == p ) return cur;
    else return "Z";
  } else {
    string nex = "";
    YYS( w , cur ){
      if( w == 'P' ) nex += "PR";
      if( w == 'R' ) nex += "RS";
      if( w == 'S' ) nex += "PS";
    }
    string res = rec( nex , d+1 );
    if( res == "Z" ) return res;
    string ans = "";
    for( int i = 0; i < SZ(res); i += PW(d+1) ){
      string a = res.substr( i , PW(d) );
      string b = res.substr( i + PW(d) , PW(d) );
      ans += min( a , b ) + max( a , b );
    }
    return ans;
  }
}

int main(){

  scanf( "%d" , &tc );
  REP( testcase , tc ){
    scanf( "%d %d %d %d" , &n , &r , &p , &s );

    string ans = "Z";
    chmin( ans , rec( "R" , 0 ) );
    chmin( ans , rec( "P" , 0 ) );
    chmin( ans , rec( "S" , 0 ) );

    if( ans == "Z" ) printf( "Case #%lld: IMPOSSIBLE\n" , testcase+1 );
    else printf( "Case #%lld: %s\n" , testcase+1 , ans.c_str() );
  }
  
  return 0;
}
