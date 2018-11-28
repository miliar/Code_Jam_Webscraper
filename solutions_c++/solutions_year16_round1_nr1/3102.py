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

  int n_test;
  cin >> n_test;
  for( int tc = 1; n_test--; tc++ ) {
    string s; cin >> s;
    deque< char > ans;
    for( auto& e : s ) {
      if( ans.empty( ) )
        ans.PB( e );
      else {
        if( e >= ans.front( ) )
          ans.PF( e );
        else
          ans.PB( e );
      }
    }
    cout << "Case #" << tc << ": ";
    for( auto& e: ans )
      cout << e;
    cout << "\n";
  }

  return 0;
}
