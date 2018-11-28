#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

typedef std::set <int> Set;

int X[2];
int T[2][4][4];

bool input() {
  for ( int i = 0; i < 2; ++ i ) {
    cin >> X[i];
    for ( int r = 0; r < 4; ++ r ) {
      for ( int c = 0; c < 4; ++ c ) {
        cin >> T[i][r][c];
      }
    }
  }
  return true;
}

Set solve() {
  Set S[2];
  S[0].clear();
  S[1].clear();
  for ( int i = 0; i < 4; ++ i ) S[0].insert(T[0][X[0] - 1][i]);
  for ( int i = 0; i < 4; ++ i ) S[1].insert(T[1][X[1] - 1][i]);
  Set res;
  set_intersection(S[0].begin(), S[0].end(), S[1].begin(), S[1].end(), inserter(res, res.begin()));
  return res;
}

int main() {
  int tests;
  cin >> tests;
  for ( int i = 0; i < tests; ++ i ) {
    input();
    Set ret = solve();
    cout << "Case #" << ( i + 1 ) << ": ";
    if ( ret.empty() ) {
      cout << "Volunteer cheated!" << endl;
    } else if ( ret.size() == 1 ) {
      cout << *ret.begin() << endl; 
    } else {
      cout << "Bad magician!" << endl;
    }
  }
  return 0;
}

