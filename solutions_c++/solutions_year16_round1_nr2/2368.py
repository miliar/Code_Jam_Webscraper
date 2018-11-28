#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long int n;
bool kansu( vector< vector< long long int > > v, vector< vector< long long int > > ans, vector< bool > ch, long long int k ) {

  if ( k == n * 2 - 1 ) {
    for ( long long int i = 0; i < n; i++ ) {
      if ( ch[i] == false ) {
	for ( long long int j = 0; j < n; j++ ) {
	  cout << " " << ans[i][j];
	}
	cout << endl;
	return true;
      }
    }
    for ( long long int i = n; i < n * 2; i++ ) {
      if ( ch[i] == false ) {
	for ( long long int j = 0; j < n; j++ ) {
	  cout << " " << ans[j][i - n];
	}
	cout << endl;
	return true;
      }
    }
  }

  for ( long long int i = 0; i < n; i++ ) {
    if ( ch[n+i] == true ) continue;
    if ( ans[0][i] == v[k][0] ) {
      bool f = true;
      for ( long long int j = 1; j < n; j++ ) {
	if ( ans[j][i] != 0 && ans[j][i] != v[k][j] ) {
	  f = false;
	  break;
	}
      }
      if ( f == true ) {
	for ( long long int j = 1; j < n; j++ ) {
	  ans[j][i] = v[k][j];
	}
	ch[n+i] = true;
	if ( kansu( v, ans, ch, k + 1 ) == true ) return true;
	ch[n+i] = false;
	for ( long long int j = 1; j < n; j++ ) {
	  if ( ch[j] == false ) ans[j][i] = 0;
	}
      }
    }
  }
  for ( long long int i = 0; i < n; i++ ) {
    if ( ch[i] == true ) continue;
    if ( ans[i][0] == v[k][0] ) {
      bool f = true;
      for ( long long int j = 1; j < n; j++ ) {
	if ( ans[i][j] != 0 && ans[i][j] != v[k][j] ) {
	  f = false;
	  break;
	}
      }
      if ( f == true ) {
	for ( long long int j = 1; j < n; j++ ) {
	  ans[i][j] = v[k][j];
	}
	ch[i] = true;
	if ( kansu( v, ans, ch, k + 1 ) == true ) return true;
	ch[i] = false;
	for ( long long int j = 1; j < n; j++ ) {
	  if ( ch[j+n] == false ) ans[i][j] = 0;
	}
      }
    }
  }
  return false;

}


bool kansu2( vector< vector< long long int > > v, vector< vector< long long int > > ans, vector< bool > ch, long long int k ) {

  if ( k == n*2-1 ) {
    for ( long long int i = 0; i < n; i++ ) {
      if ( ch[i] == false ) {
	for ( long long int j = 0; j < n; j++ ) {
	  cout << " " << -ans[i][n-1-j];
	}
	cout << endl;
	return true;
      }
    }
    for ( long long int i = n; i < n * 2; i++ ) {
      if ( ch[i] == false ) {
	for ( long long int j = 0; j < n; j++ ) {
	  cout << " " << -ans[n-1-j][i - n];
	}
	cout << endl;
	return true;
      }
    }
  }

  for ( long long int i = 0; i < n; i++ ) {
    if ( ch[n+i] == true ) continue;
    if ( ans[0][i] == v[k][0] ) {
      bool f = true;
      for ( long long int j = 1; j < n; j++ ) {
	if ( ans[j][i] != 0 && ans[j][i] != v[k][j] ) {
	  f = false;
	  break;
	}
      }
      if ( f == true ) {
	for ( long long int j = 1; j < n; j++ ) {
	  ans[j][i] = v[k][j];
	}
	ch[n+i] = true;
	if ( kansu2( v, ans, ch, k + 1 ) == true ) return true;
	ch[n+i] = false;
	for ( long long int j = 1; j < n; j++ ) {
	  if ( ch[j] == false ) ans[j][i] = 0;
	}
      }
    }
  }
  for ( long long int i = 0; i < n; i++ ) {
    if ( ch[i] == true ) continue;
    if ( ans[i][0] == v[k][0] ) {
      bool f = true;
      for ( long long int j = 1; j < n; j++ ) {
	if ( ans[i][j] != 0 && ans[i][j] != v[k][j] ) {
	  f = false;
	  break;
	}
      }
      if ( f == true ) {
	for ( long long int j = 1; j < n; j++ ) {
	  ans[i][j] = v[k][j];
	}
	ch[i] = true;
	if ( kansu2( v, ans, ch, k + 1 ) == true ) return true;
	ch[i] = false;
	for ( long long int j = 1; j < n; j++ ) {
	  if ( ch[j+n] == false ) ans[i][j] = 0;
	}
      }
    }
  }
  return false;

}


int main() {

  long long int t;
  cin >> t;

  for ( long long int tt = 0; tt < t; tt++ ) {

    cout << "Case #" << tt+1 << ":";

    cin >> n;

    vector< vector< long long int > > v;

    for ( long long int i = 0; i < n * 2 - 1; i++ ) {

      vector< long long int > in_v;
      for ( long long int j = 0; j < n; j++ ) {
	long long int in;
	cin >> in;
	in_v.push_back( in );
      }
      v.push_back( in_v );

    }

    sort( v.begin(), v.end() );


    vector< vector< long long int > > ans;
    for ( long long int i = 0; i < n; i++ ) {
      vector< long long int > aa;
      for ( long long int j = 0; j < n; j++ ) {
	aa.push_back( 0 );
      }
      ans.push_back( aa );
    }
    ans[0][0] = v[0][0];

    vector< bool > ch;
    for ( long long int i = 0; i < n * 2; i++ ) {
      ch.push_back( false );
    }
    vector< vector< long long int > > vv;
    for ( long long int i = 0; i < n * 2 - 1; i++ ) {
      vector< long long int > aa;
      for ( long long int j = 0; j < n; j++ ) {
	aa.push_back( -v[i][n-1-j] );
      }
      vv.push_back( aa );
    }

    if ( kansu( v, ans, ch, 0 ) == false ) {
      sort( vv.begin(), vv.end() );
      ans[0][0] = 0;
      ans[0][0] = vv[0][0];
      kansu2( vv, ans, ch, 0 );
    }

  }

  return 0;

}
