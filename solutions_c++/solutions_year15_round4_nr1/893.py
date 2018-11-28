#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {

  long long int t;
  cin >> t;

  for ( long long int tt = 0; tt < t; tt++ ) {

    cout << "Case #" << tt+1 << ": ";

    long long int r, c;
    cin >> r >> c;

    vector< string > v;

    for ( long long int i = 0; i < r; i++ ) {

      string in;
      cin >> in;

      v.push_back( in );

    }

    long long int ans = 0;

    for ( long long int x = 0; x < c; x++ ) {

      for ( long long int y = 0; y < r; y++ ) {

	if ( v[y][x] == '.' ) continue;

	bool f = false;
	if ( v[y][x] == '^' ) {
	  for ( long long int dy = 0; dy < y; dy++ ) {
	    if ( v[dy][x] != '.' ) f = true;
	  }
	  if ( f == true ) continue;
	}else if ( v[y][x] == '>' ) {
	  for ( long long int dx = c - 1; dx > x; dx-- ) {
	    if ( v[y][dx] != '.' ) f = true;
	  }
	  if ( f == true ) continue;
	}else if ( v[y][x] == 'v' ) {
	  for ( long long int dy = r - 1; dy > y; dy-- ) {
	    if ( v[dy][x] != '.' ) f = true;
	  }
	  if ( f == true ) continue;
	}else if ( v[y][x] == '<' ) {
	  for ( long long int dx = 0; dx < x; dx++ ) {
	    if ( v[y][dx] != '.' ) f = true;
	  }
	  if ( f == true ) continue;
	}

	for ( long long int dx = 0; dx < c; dx++ ) {

	  if ( dx == x ) continue;
	  if ( v[y][dx] != '.' ) f = true;

	}

	for ( long long int dy = 0; dy < r; dy++ ) {

	  if ( dy == y ) continue;
	  if ( v[dy][x] != '.' ) f = true;

	}

	if ( f == false ) {
	  ans = -1;
	  break;
	}
	ans++;

      }

      if ( ans < 0 ) break;

    }

    if ( ans >= 0 ) {
      cout << ans << endl;
    }else {
      cout << "IMPOSSIBLE" << endl;
    }

  }

  return 0;

}
