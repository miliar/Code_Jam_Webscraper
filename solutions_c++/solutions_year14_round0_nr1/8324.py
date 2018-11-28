#include <iostream>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;

string result( set<int>& res ) {
  ostringstream oss;
  if( res.empty() ) {
    oss << "Volunteer cheated!";
  } else if( res.size() > 1 ) {
    oss << "Bad magician!";
  } else
    oss << *res.begin();
  return oss.str();
}

int main( int argc, char* argv[] ) {
  int T;
  cin >> T;

  for( int ca=0; ca<T; ++ca ) {
    int ans1, ans2;
    cin >> ans1;

    int grid[4][4];
    for( int i=0; i<4; ++i ) {
      for( int j=0; j<4; ++j ) {
        cin >> grid[i][j];
      }
    }

    cin >> ans2;
    int grid2[4][4];
    for( int i=0; i<4; ++i ) {
      for( int j=0; j<4; ++j ) {
        cin >> grid2[i][j];
      }
    }

    sort( grid[ans1-1], grid[ans1] );
    sort( grid2[ans2-1], grid2[ans2] );

    set<int> res;
    set_intersection( grid[ans1-1], grid[ans1], grid2[ans2-1], grid2[ans2], inserter(res, res.begin()) );

    cout << "Case #" << (ca+1) << ": " << result( res ) << endl;
  }

  return 0;
}

