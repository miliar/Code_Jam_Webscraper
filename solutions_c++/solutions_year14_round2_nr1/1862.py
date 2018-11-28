#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>
using namespace std;

int main() {

  long long int T;

  cin >> T;

  for ( long long int i = 0; i < T; i++ ) {

    cout << "Case #" << i+1 << ": ";

    long long int n;

    cin >> n;

    vector< string > a;

    string input;

    for ( long long int j = 0; j < n; j++ ) {

      cin >> input;

      a.push_back( input );

    }

    int cnt[100][100];

    long long int cnt2[100] = {0};

    for ( int j = 0; j < 100; j++ ) {

      for ( int l = 0; l < 100; l++ ) {

	cnt[j][l] = 0;

      }

    }

    string s2 = "";

    bool f = true;

    for ( long long int l = 0; l < n; l++ ) {

      string s = "";

      char k = '0';

      int b = -1;

      for ( long long int j = 0; j < a[l].size(); j++ ) {

	if ( k != a[l][j] ) {

	  s += a[l][j];

	  k = a[l][j];

	  b++;

	}

	cnt[l][b]++;
	cnt2[b]++;

      }

      if ( l == 0 ) {

	s2 = s;

      }else {

	if ( s != s2 ) {

	  cout << "Fegla Won" << endl;
	  f = false;
	  break;

	}

      }

    }

    if ( f == false ) continue;

    long long int ans = 0;

    for ( long long int j = 0; j < s2.size(); j++ ) {

      long long int c = ( cnt2[j] / n );
      long long int c2 = ( cnt2[j] / n + 1 );

      long long int d = 0;
      long long int d2 = 0;

      for ( long long int l = 0; l < n; l++ ) {

	d += abs( c - cnt[l][j] );
	d2 += abs( c2 - cnt[l][j] );

      }

      ans += min( d, d2 );

    }

    cout << ans << endl;

  }

  return 0;

}
