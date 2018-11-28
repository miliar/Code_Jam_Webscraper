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


  
struct Unionfind{
  vi size, par;
  Unionfind(){}
  Unionfind( int n ) :  size(n,1), par(n){
    REP( i , n ) par[i] = i;
  }
  void init( int n ){
    size = vi( n , 1 );
    par.resize( n );
    REP( i , n ) par[i] = i;
  }
  int find( int x ){
    if( par[x] == x ) return x;
    return par[x] = find( par[x] );
  }
  bool unite( int x , int y ){
    x = find(x);
    y = find(y);
    if( x == y ) return false;
    if( size[y] < size[x] ) swap( x , y );
    par[x] = y;
    size[y] += size[x];
    return true;
  }
  bool same( int x , int y ){
    return find(x) == find(y);
  }
};

Unionfind uf;

int tc;
int n, m;
int b[512];

int a[128][128][4];

int s[128], t[128], u[128];

int p( int y , int x , int k ){
  return ( y * m + x ) * 4 + k;
}

int main(){

  scanf( "%d" , &tc );
  REP( test , tc ){
    scanf( "%d %d" , &n , &m );
    REP( i , (n+m)*2 ){
      scanf( "%d" , &b[i] );
      b[i]--;
    }

    REP( j , m ) s[j] = 0          , t[j] = j        , u[j] = 1;
    REP( i , n ) s[m+i] = i        , t[m+i] = m-1    , u[m+i] = 0;
    REP( j , m ) s[n+m+j] = n-1    , t[n+m+j] = m-1-j, u[n+m+j] = 3;
    REP( i , n ) s[n+2*m+i] = n-1-i, t[n+2*m+i] = 0  , u[n+2*m+i] = 2;

    bool ok = false;
    printf( "Case #%lld:\n" , test+1 );
    REP( mask , PW(n*m) ){
      uf.init( n*m*4 );

      REP( i , n ) REP( j , m ){
	if( j < m-1 ) uf.unite( p( i , j , 0 ) , p( i , j+1 , 2 ) );
	if( i < n-1 ) uf.unite( p( i , j , 3 ) , p( i+1 , j , 1 ) );
      }
      
      REP( i , n ) REP( j , m ){
	if( mask & PW(i*m+j) ){
	  uf.unite( p( i , j , 0 ) , p( i , j , 1 ) );
	  uf.unite( p( i , j , 2 ) , p( i , j , 3 ) );
	} else {
	  uf.unite( p( i , j , 0 ) , p( i , j , 3 ) );
	  uf.unite( p( i , j , 1 ) , p( i , j , 2 ) );
	}
      }

      ok = true;
      REP( i , n+m ) if( !uf.same( p( s[b[i*2]] , t[b[i*2]] , u[b[i*2]] ) , p( s[b[i*2+1]] , t[b[i*2+1]] , u[b[i*2+1]] ) ) ) ok = false;
      if( ok ){
	
	REP( i , n ){
	  REP( j , m ) printf( "%c" , ( mask & PW(i*m+j) ) ? '\\' : '/' );
	  printf( "\n" );
	}
	break;
      }
    }

    if( !ok ) printf( "IMPOSSIBLE\n" );
  }
  
  return 0;
}
