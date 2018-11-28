
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

const int MAXN = 26;

int n;
char in[ MAXN ][ MAXN ];

int enc( int i , int j ) {
  return i*n+j;
}

bool chk( int cmb ) {
  static int g[ MAXN ][ MAXN ] , deg[ 2 ][ MAXN ];
  FOR( i , n ) deg[ 0 ][ i ] = deg[ 1 ][ i ] = 0;

  FOR( i , n ) FOR( j , n ) g[ i ][ j ] = 0;

  FOR( i , n ) FOR( j , n ) {
    if( in[ i ][ j ] == '1' ) g[ i ][ j ] = 1;
    else if( ( cmb >> enc( i , j ) ) & 1 ) g[ i ][ j ] = 1;
    deg[ 0 ][ i ] += g[ i ][ j ];
    deg[ 1 ][ j ] += g[ i ][ j ];
  }

  FOR( i , n ) FOR( j , n ) FOR( ii , n ) FOR( jj , n ) {
    if( g[ i ][ ii ] && g[ i ][ jj ] && g[ j ][ ii ] ) {
      if( !g[ j ][ jj ] ) return 0;
    }
  }
  FOR( i , n ) FOR( j , n ) if( g[ i ][ j ] ) {
    if( deg[ 0 ][ i ] != deg[ 1 ][ j ] ) return 0;
  }
  FOR( j , n ) if( deg[ 1 ][ j ] == 0 ) return 0;

  return 1;
}

void bf() {
  int ans = MAXN*MAXN;
  FOR( cmb , ( 1 << ( n*n ) ) ) {
    if( chk( cmb ) ) ans = min( ans , __builtin_popcount( cmb ) );
  }
  printf( "%d\n" , ans );
}

int main()
{
  int tc;R(tc);
  REP( _ , 1 , tc ) {
    printf( "Case #%d: " , _ );
    R( n );
    FOR( i , n ) R( in[ i ] );
    bf();
  }
}
