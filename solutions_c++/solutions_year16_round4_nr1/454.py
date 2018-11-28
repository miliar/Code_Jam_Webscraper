
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

const int MAXN = 12;

int n , r , p , s;
char ans[ 5000 ];
char sig[ 3 ] = { 'R' , 'P' , 'S' };

typedef tuple<int,int,int> tiii;

string g( int tn , int win ) {
  if( tn == 0 ) return string( 1 , sig[ win ] );
  string s1 = g( tn-1 , win );
  string s2 = g( tn-1 , ( win+2 )%3 );
  if( s1 < s2 ) return s1+s2;
  return s2+s1;
}

tiii f( int win ) {
  string str = g( n , win );
  int cnt[ 3 ] = { 0 , 0 , 0 };
  for( char c : str ) {
    if( c == 'R' ) cnt[ 0 ]++;
    if( c == 'P' ) cnt[ 1 ]++;
    if( c == 'S' ) cnt[ 2 ]++;
  }
  return tiii( cnt[ 0 ] , cnt[ 1 ] , cnt[ 2 ] );
}

int main()
{
  int tc;R(tc);
  REP( _ , 1 , tc ) {
    printf( "Case #%d: " , _ );
    R( n , r , p , s );
    bool flag = 0;
    //cout << g( n , 0 ) << endl;
    //cout << g( n , 1 ) << endl;
    //cout << g( n , 2 ) << endl;
    FOR( i , 3 ) {
      if( tiii( r , p , s ) == f( i ) ) {
        string str = g( n , i );
        FOR( j , SZ( str ) ) ans[ j ] = str[ j ];
        ans[ SZ( str ) ] = 0;
        flag = 1;
        break ;
      }
    }
    if( !flag ) puts( "IMPOSSIBLE" );
    else puts( ans );
  }
}
