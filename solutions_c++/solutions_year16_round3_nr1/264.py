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
    freopen( "A-large.in", "r", stdin );
    freopen( "output", "w", stdout );
  #endif // LOCAL

  ios_base::sync_with_stdio( 0 );
  cin.tie( 0 ); cout.tie( 0 );

  int nTest;
  cin >> nTest;
  for( int tc = 1; nTest--; tc++ ) {
    cerr << "In case " << tc << "\n";
    int n; cin >> n;
    int total = 0;
    priority_queue< pii > pq;
    for( int i = 0; i < n; i++ ) {
      int p; cin >> p;
      pq.push( { p, i } );
      total += p;
    }
    cout << "Case #" << tc << ":";
    while( !pq.empty( ) ) {
      pii cur = pq.top( ); pq.pop( );
      if( cur.FI > 1 ) {
        pq.push( { cur.FI-1, cur.SE } );
      }
      cout << " " << char( cur.SE+'A' );
      total--;
      if( ( total != 2 ) && !pq.empty( ) ) {
        cur = pq.top( ); pq.pop( );
        if( cur.FI > 1 ) {
          pq.push( { cur.FI-1, cur.SE } );
        }
        cout << char( cur.SE+'A' );
        total--;
      }
    }
    cout << "\n";
  }

  return 0;
}
