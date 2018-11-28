#include <iostream>
using namespace std;

int main() {

  long long int t;
  cin >> t;

  for ( long long int tt = 0; tt < t; tt++ ) {

    cout << "Case #" << tt+1 << ": ";

    long long int s;
    cin >> s;

    long long int cnt = 0;
    long long int ans = 0;

    for ( long long int j = 0; j <= s; j++ ) {

      long long int k = max( 0LL, j - cnt );
      ans += k;
      cnt += k;

      char c;
      cin >> c;

      cnt += ( c - '0' );

    }

    cout << ans << endl;

  }

  return 0;

}
