
// default code for competitive programming
// ver 3.1415 {{{

// Includes
#include <bits/stdc++.h>

// Defines
#define NAME(x) #x
#define SZ(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()
#define FOR(i, e) for( int i = 0 ; i < (e) ; i++ )
#define ITER(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define REP(i, s, e) for(int i = (s); i <= (e); i++)
#define REPD(i, s, e) for(int i = (s); i >= (e); i--)
#define IOS ios_base::sync_with_stdio( 0 )
#define DEBUG 1
#define fst first
#define snd second
#define PB push_back
#ifdef ONLINE_JUDGE
#define FILE( fn ) \
    freopen(fn".in","r",stdin); \
    freopen(fn".out","w",stdout);
#else
#define FILE( fn )
#endif

#ifdef AKAI
#define debug( ... ) fprintf( stderr , __VA_ARGS__ )
#else
#define debug( ... )
#endif

using namespace std;

// Typedefs
typedef double real;
typedef long long ll;
typedef pair<ll, int> pli;
typedef tuple<ll, int> tli;
typedef pair<int, int> pii;
typedef tuple<int, int> tii;
typedef unsigned long long ull;

// Some common const.
const double EPS = 1e-8;
const double Pi = acos(-1);

// Equal for double
bool inline equ(double a, double b)
{return fabs(a - b) < EPS;}

int _R( int& x ) { return scanf( "%d" , &x ); }
int _R( ll& x ) { return scanf( "%" PRId64 , &x ); }
int _R( double& x ) { return scanf( "%lf" , &x ); }
int _R( char* s ) { return scanf( "%s" , s ); }

int R() { return 0; }

template< typename T1 , typename... T2 >
int R( T1& x , T2&... tail )
{
  int tmp = _R( x );
  return tmp + R( tail... );
}

template< typename Iter , typename F >
inline void out( Iter s , Iter e , F of )
{
  bool flag = 0;
  for( Iter it = s ; it != e ; it++ )
  {
    if( flag ) printf( " " );
    else flag = 1;
    of( *it );
  }
  puts( "" );
}

// }}}
// start ~~QAQ~~

const int MAXN = 210;

typedef double D;

int n , K;
D p[ MAXN ] , gp[ MAXN ];
D dp[ MAXN ][ MAXN ];
inline void chk( D& a , D b ) {
  a = max( a , b );
}

inline D calc() {
  dp[ 0 ][ 0 ] = 1;
  REP( i , 1 , K ) REP( j , 0 , i ) {
    dp[ i ][ j ] = 0;
    dp[ i ][ j ] += gp[ i ]*dp[ i-1 ][ j-1 ];
    dp[ i ][ j ] += (1-gp[i])*dp[ i-1 ][ j ];
  }
  return dp[ K ][ K/2 ];
}

int main()
{
  int tc;R(tc);
  REP( _ , 1 , tc ) {
    printf( "Case #%d: " , _ );
    R( n , K );
    REP( i , 1 , n ) R( p[ i ] );
    sort( p+1 , p+1+n );
    D ans = 0;
    REP( i , 0 , K ) {
      REP( j , 1 , i ) gp[ j ] = p[ j ];
      REP( j , 1 , K-i ) gp[ K-j+1 ] = p[ n-j+1 ];
      chk( ans , calc() );
    }
    printf( "%.12f\n" , ans );
  }
}
