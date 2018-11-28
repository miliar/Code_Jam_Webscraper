
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

int n;
map< string , int > mp;
vector< int > in[ MAXN ];
int st[ 3 ][ 10000000 ];
//set< int > st[ 3 ];

int main()
{
  int tc;cin >> tc;
  REP( _ , 1 , tc )
  {printf( "Case #%d: " , _ );
    cin >> n;
    string str , tmp;
    getline( cin , str );
    mp.clear();
    int tot = 0;
    REP( i , 1 , n )
    {
      in[ i ].clear();
      //cout << " i " << i << endl;
      str.clear();
      getline( cin , str );
      //cout << str << endl;
      stringstream ss( str );
      while( ss >> tmp )
      {
        if( !mp.count( tmp ) ) mp[ tmp ] = tot++;
        in[ i ].push_back( mp[ tmp ] );
      }
      //for( string& s : in[ i ] ) cout << s << endl;
    }
    int ans = 100000000;
    for( int comb = 0 ; comb < ( 1 << ( n - 2 ) ) ; comb++ )
    {
      fill( st[ 1 ] , st[ 1 ] + tot , 0 );
      fill( st[ 2 ] , st[ 2 ] + tot , 0 );
      REP( i , 1 , 2 ) for( int s : in[ i ] ) st[ i ][ s ]++;//.insert( s );
      REP( i , 3 , n )
      {
        int bel;
        if( comb & ( 1 << ( i - 3 ) ) ) bel = 1;
        else bel = 2;
        for( int s : in[ i ] ) st[ bel ][ s ]++;//.insert( s );
      }
      int cnt = 0;
      REP( s , 0 , tot - 1 ) if( st[ 1 ][ s ] && st[ 2 ][ s ] ) cnt++;
      ans = min( ans , cnt );
    }
    printf( "%d\n" , ans );
  }
}


