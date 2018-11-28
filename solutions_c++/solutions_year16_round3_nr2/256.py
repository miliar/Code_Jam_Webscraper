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

const int MAX = int( 1e7 );
const int MOD = int( 1e9+7 );
const int oo  = INT_MAX;

int main( ) {

  #ifdef LOCAL
    freopen( "B-large.in", "r", stdin );
    freopen( "output", "w", stdout );
  #endif // LOCAL

  ios_base::sync_with_stdio( 0 );
  cin.tie( 0 ); cout.tie( 0 );

  int nTest;
  cin >> nTest;
  for( int tc = 1; nTest--; tc++ ) {
    cerr << "In case " << tc << "\n";
    int b; ll m; cin >> b >> m;
    ll mx = 1LL<<( b-2 );
    cout << "Case #" << tc << ": ";
    if( m > mx )
      cout << "IMPOSSIBLE\n";
    else {
      cout << "POSSIBLE\n";
      vvi G( b, vi( b ) );
      ll mask = m;
      if( m == mx ) {
        mask |= ( mx-1LL );
        G[ 0 ][ b-1 ] = 1;
      }
      for( int i = 1; i < b; i++ )
        for( int j = i+1; j < b; j++ )
          G[ i ][ j ] = 1;
      for( int i = 0, j = b-2; i+2 < b; i++, j-- ) {
        if( ( mask>>i )&1 )
          G[ 0 ][ j ] = 1;
      }
      for( int i = 0; i < b; i++ ) {
        for( int j = 0; j < b; j++ )
          cout << G[ i ][ j ];
        cout << "\n";
      }
    }
  }

  return 0;
}
