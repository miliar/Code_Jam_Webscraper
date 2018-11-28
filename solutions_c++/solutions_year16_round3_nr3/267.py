#include <bits/stdc++.h>

#define PB          push_back
#define PF          push_front
#define MP          make_pair
#define FI          first
#define SE          second

using namespace std;

typedef long long           ll;
typedef unsigned long long  ull;
typedef long double         lf;
typedef pair< int, int >    pii;
typedef vector< bool >      vb;
typedef vector< double >    vd;
typedef vector< ll >        vll;
typedef vector< int >       vi;
typedef vector< vi >        vvi;
typedef vector< vvi >       vvvi;

const int MAX = int( 10 );
const int MOD = int( 1e9+7 );
const int oo  = INT_MAX;

struct Permutation { int j, p, s; };

int J, P, S, K;
int cnt[ MAX ][ MAX ][ MAX ];
vector< Permutation > ans, cur, p;

void go( int id ) {
  if( id >= int( p.size( ) ) ) {
    if( int( cur.size( ) ) > int( ans.size( ) ) )
      ans = cur;
    return ;
  }
  go( id+1 );
  auto e = p[ id ];
  if( cnt[ 0 ][ e.j ][ e.p ]+1 <= K && cnt[ 1 ][ e.j ][ e.s ]+1 <= K && cnt[ 2 ][ e.p ][ e.s ]+1 <= K ) {
    cnt[ 0 ][ e.j ][ e.p ]++; cnt[ 1 ][ e.j ][ e.s ]++; cnt[ 2 ][ e.p ][ e.s ]++;
    cur.PB( e );
    go( id+1 );
    cur.pop_back( );
    cnt[ 0 ][ e.j ][ e.p ]--; cnt[ 1 ][ e.j ][ e.s ]--; cnt[ 2 ][ e.p ][ e.s ]--;
  }
}

int main( ) {

  #ifdef LOCAL
    freopen( "C-small-attempt0.in", "r", stdin );
    freopen( "output", "w", stdout );
  #endif // LOCAL

  ios_base::sync_with_stdio( 0 );
  cin.tie( 0 ); cout.tie( 0 );

  int nTest;
  cin >> nTest;
  for( int tc = 1; nTest--; tc++ ) {
    cerr << "In case " << tc << "\n";
    cin >> J >> P >> S >> K;
    memset( cnt, 0, sizeof( cnt ) );
    p.clear( );
    for( int i = 0; i < J; i++ )
      for( int j = 0; j < P; j++ )
        for( int k = 0; k < S; k++ )
          p.PB( { i+1, j+1, k+1 } );
    ans.clear( ); cur.clear( );
    go( 0 );
    cout << "Case #" << tc << ": " << int( ans.size( ) ) << "\n";
    for( auto& e : ans )
      cout << e.j << " " << e.p << " " << e.s << "\n";
  }

  return 0;
}
