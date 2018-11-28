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

int tc;
int n;

char s[8][8];
bool a[8][8];

vi G[8];

int c[8];

void dfs( int x , int r ){
  c[x] = r;
  YYS( w , G[x] ) if( c[w] == -1 ) dfs( w , r );
}

int main(){

  scanf( "%d" , &tc );
  REP( test , tc ){
    scanf( "%d" , &n );
    REP( i , n ) scanf( "%s" , s[i] );

    int ans = INF;
    REP( mask , PW(n*n) ){
      REP( i , n ) REP( j , n ) a[i][j] = ( s[i][j] == '1' ? true : false );
      REP( i , n ) REP( j , n ) if( mask & PW(i*n+j) ) a[i][j] = true;

      REP( i , 2*n ) G[i].clear();
      REP( i , n ) REP( j , n ) if( a[i][j] ){
	G[i].pb( n+j );
	G[n+j].pb( i );
      }

      bool ok = true;
      REP( i , 2*n ) c[i] = -1;
      REP( i , 2*n ) if( c[i] == -1 ){
	dfs( i , i );
	REP( j , n ) REP( k , n ) if( c[j] == i && c[n+k] == i && !a[j][k] ) ok = false;
	int ca = 0, cb = 0;
	REP( j , n ) if( c[j] == i ) ca++;
	REP( k , n ) if( c[n+k] == i ) cb++;
	if( ca != cb ) ok = false;
      }

      if( ok ){
	chmin( ans , __builtin_popcount( mask ) );
      }
    }

    printf( "Case #%lld: %d\n" , test+1 , ans );
  }
  
  return 0;
}
