#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

  long long int T;

  cin >> T;

  for ( long long int tt = 0; tt < T; tt++ ) {

    long long int n, x, input;

    cin >> n >> x;

    vector< long long int > s;

    for ( long long int i = 0; i < n; i++ ) {

      cin >> input;

      s.push_back( input );

    }

    stable_sort( s.begin(), s.end() );

    long long int ans = 0;

    while( true ) {

      if ( s.size() == 0 ) break;

      ans++;

      if ( s.size() == 1 ) {
	break;
      }
      long long int k = x - s[ s.size() - 1 ];
      int lo = 0;
      int hi = s.size() - 2;
      while( lo < hi ) {
	int m = ( lo + hi ) / 2;
	if ( s[m] > k ) {
	  hi = m;
	}else {
	  lo = m + 1;
	}
      }
      if ( s[lo] <= k ) {
	vector< long long int >:: iterator it = s.begin() + lo;
	it = s.erase( it );
      }else if ( lo > 0 ) {
	lo--;
	if ( s[lo] <= k ) {
	  vector< long long int >:: iterator its = s.begin() + lo;
	  its = s.erase( its );
	}
      }
      s.pop_back();

    }

    cout << "Case #" << tt+1 << ": " << ans << endl;

  }

  return 0;

}
