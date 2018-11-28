#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

  long long int t;
  cin >> t;

  for ( long long int tt = 0; tt < t; tt++ ) {

    cout << "Case #" << tt+1 << ": ";

    long long int d;
    cin >> d;

    vector< long long int > p;

    for ( long long int i = 0; i < d; i++ ) {

      long long int in;
      cin >> in;

      p.push_back( in );

    }

    sort( p.begin(), p.end() );

    long long int ans = 10000;

    for ( long long int t = 1; t <= 1000; t++ ) {

      long long int cnt = 0;
      long long int m = 0;

      for ( long long int i = 0; i < d; i++ ) {

	if ( ( p[i] % t ) == 0 ) {

	  m = max( m, t );
	  cnt += p[i] / t - 1;

	}else {

	  long long int k = p[i] / t + 1;
	  m = max( m, p[i] / k + 1 );
	  cnt += p[i] / t;

	}

      }

      ans = min( cnt + m, ans );

    }

    cout << ans << endl;

  }

  return 0;

}
