
// default code for competitive programming
// c2251393 ver 3.141 {{{

// Includes
#include <bits/stdc++.h>

// Defines
#define NAME(x) #x
#define SZ(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()
#define FOR(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define REP(i, s, e) for(int i = (s); i <= (e); i++)
#define REPD(i, s, e) for(int i = (s); i >= (e); i--)
#define DEBUG 1
#define fst first
#define snd second
 
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
const double EPS = -1e8;
const double Pi = acos(-1);
 
// Equal for double
bool inline equ(double a, double b)
{return fabs(a - b) < EPS;}

// }}}
// start ~~QAQ~~

const int MAXN = 110;

int n , m;
char in[ MAXN ][ MAXN ];
int dx[ 4 ] = { -1 , 0 , 1 , 0 };
int dy[ 4 ] = { 0 , 1 , 0,  -1 };
map< char , int > mp{
  { '^' , 0 },
  { '>' , 1 },
  { 'v' , 2 },
  { '<' , 3 }
};

bool ok( int i , int j )
{return 1 <= i && i <= n && 1 <= j && j <= m;}

int id( int i , int j )
{return ( i - 1 ) * m + j;}

vector< pii > g[ MAXN*MAXN ];

int main()
{
  int tc;scanf( "%d" , &tc );
  REP( _ , 1 , tc )
  {printf( "Case #%d: " , _ );
    scanf( "%d%d" , &n , &m );
    REP( i , 1 , n ) scanf( "%s" , in[ i ] + 1  );
    REP( i , 0 , MAXN-1 ) g[i].clear();
    bool flag = 1;
    int ans = 0;
    REP( i , 1 , n ) REP( j , 1 , m )
    {
      if( !mp.count( in[ i ][ j ] ) ) continue ;
      int typ = mp[ in[ i ][ j ] ];
      //printf( "%d %d typ %d\n" , i , j , typ );
      REP( k , 0 , 3 )
      {
        int px = i , py = j;
        while( ok( px , py ) )
        {
          px = px + dx[ k ];
          py = py + dy[ k ];
          if( !ok( px , py ) )
          {
            g[ id( i , j ) ].push_back( pii( 0 , k == typ ) );
            break ;
          }
          if( mp.count( in[ px ][ py ] ) )
          {
            g[ id( i , j ) ].push_back( pii( id( px , py ) , k == typ ) );
            break ;
          }
        }
      }
      bool mustdead = 1 , borndead = 0;
      for( pii& e : g[ id( i , j ) ] )
      {
        //printf( "-e %d %d %d\n" , id( i , j ) , e.first , e.second );
        int v = e.first , pri = e.second;
        if( v != 0 ) mustdead = 0;
        if( v == 0 && pri == 1 ) borndead = 1;
      }
      if( mustdead )
      {
        flag = 0;
        break ;
      }
      if( borndead ) ans++;
    }
    if( flag ) printf( "%d\n" , ans );
    else puts( "IMPOSSIBLE" );
  }
}
