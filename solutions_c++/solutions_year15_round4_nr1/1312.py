#include <cmath>
#include <queue>
#include <cassert>
#include <stack>
#include <unordered_set>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int Solve(const vector<string> &board) {
  int score = 0;
  for (int i = 0; i < board.size(); i++) {
    for (int k = 0; k < board[0].size(); k++) {
      if (board[i][k] == '.')
        continue;

      int ss = 99;
#define CHECK(dx, dy, ds) {for (int ii = i + dx, kk = k + dy; ii >= 0 && kk >= 0 && ii < board.size() && kk < board[0].size(); ii += dx, kk += dy) { \
          if (board[ii][kk] == '.') \
            continue; \
          ss= min(ds, ss);\
        } }
      CHECK(-1, 0, int(board[i][k] != '^') );
      CHECK(1, 0, int(board[i][k] != 'v') );
      CHECK(0, -1, int(board[i][k] != '<') );
      CHECK(0, 1, int(board[i][k] != '>') );
      if (ss == 99)
        return -1;
      score += ss;
    }
  }
  return score;
}

int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  cout.tie(nullptr);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int TT = 1; TT <= T; TT++) {
    int R, C;
    cin >> R >> C;
    vector<string> board(R);
    for (int i = 0; i < R; i++)
      cin >> board[i];
    int ans = Solve(board);

    cout << "Case #" << TT <<": ";
    if (ans == -1)
      cout << "IMPOSSIBLE\n";
    else
      cout << ans << '\n';
  }
  return 0;
}
