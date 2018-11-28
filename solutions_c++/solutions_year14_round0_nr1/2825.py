
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>


#define rep(i,m,n) for(int i = m; i < (int)n; i++)
#define REP(i,n) rep(i,0,n)

using namespace std;

int T, row[2]; 
int board[2][4][4];
stringstream ss;

void input() {
  cin >> row[0]; --row[0];
  REP(i, 4) REP(j, 4) cin >> board[0][i][j];
  cin >> row[1]; --row[1];
  REP(i, 4) REP(j, 4) cin >> board[1][i][j];
}

string solve() {
  int *first = board[0][row[0]];
  int *second = board[1][row[1]];
  sort(first, first + 4);
  sort(second, second + 4);
  vector<int> v(4);
  vector<int>::iterator it =
    set_intersection(first, first+4, second, second+4, v.begin());
  v.resize(it-v.begin());
  if (v.size() == 0) {
    return "Volunteer cheated!";
  } else if (v.size() == 1) {
    ss.str("");
    ss << v[0];
    return ss.str();
  }
  return "Bad magician!";
}

int main() {
  cin >> T;
  REP(t, T) {
    input();
    cout << "Case #" << t+1 << ": "
	 << solve() << endl;
  }
  return 0;
}
