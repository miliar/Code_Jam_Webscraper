#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
using namespace std;

#define eps 1e-9

int main() {

  long long int t;
  cin >> t;

  for ( long long int tt = 0; tt < t; tt++ ) {

    cout << "Case #" << tt+1 << ": ";


    long long int n;
    cin >> n;
    long double v, x;
    cin >> v >> x;

    vector< long double > r, c;

    for ( long long int i = 0; i < n; i++ ) {

      long double in_r, in_c;
      cin >> in_r >> in_c;

      r.push_back( in_r );
      c.push_back( in_c );

    }

    if ( n == 1 ) {
      if ( c[0] == x ) {
	cout << fixed << setprecision(20) << v / r[0] << endl;
      }else {
	cout << "IMPOSSIBLE" << endl;
      }
      continue;
    }

    if ( c[0] == c[1] ) {
      if ( c[0] == x ) {
	cout << fixed << setprecision(20) << v / ( r[0] + r[1] ) << endl;
      }else {
	cout << "IMPOSSIBLE" << endl;
      }
      continue;
    }

    long double max_c = c[0];
    long double min_c = c[0];

    for ( long long int i = 0; i < n; i++ ) {
      max_c = max( max_c, c[i] );
      min_c = min( min_c, c[i] );
    }

    if ( min_c > x || x > max_c ) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }

    long double t[100];
    for ( long long int i = 0; i < n; i++ ) {

      t[i] = abs( ( c[ 1 - i ] - x ) / ( c[0] - c[1] ) * v / r[i] );

    }

    cout << fixed << setprecision(20) << max( t[0], t[1] ) << endl;

  }

  return 0;

}
