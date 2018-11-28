#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef unsigned int uint;

inline int
count_bits(uint n) {
  int res;
  for (res = 0; n; ++res) {
    n &= n - 1;
  }

  return res;
}

inline bool
valid(int r, int c, vector<string>& board) {
  return (r >= 0 && r < board.size() 
          && c >= 0 && c < board[0].length());
}

inline bool
isolated(int r, int c, vector<string>& board) {
  int cnt = 0;
  for (int i = -1; i <= 1; ++i) {
    for (int j = -1; j <= 1; ++j) {
      cnt += (valid(r+i, c+j, board) && board[r+i][c+j] == '*');
    }
  }

  return (cnt == 0);
}

void
visit(int r, int c, vector<string>& board) {
  if (!valid(r, c, board)) return;
  if (board[r][c] != '.') return;

  board[r][c] = 'v';

  if (!isolated(r, c, board)) return;

  for (int i = -1; i <= 1; ++i) {
    for (int j = -1; j <= 1; ++j) {
      visit(r+i, c+j, board);
    }
  }
}

void
print_board(vector<string>& board) {
  for (int i = 0; i < board.size(); ++i)
    cerr << board[i] << endl;

  cerr << "------" << endl;
}

inline bool
win(int r, int c, vector<string> board) {
  visit(r, c, board);

  for (int i = 0; i < board.size(); ++i) {
    for (int j = 0; j < board[0].length(); ++j) {
      if (board[i][j] == '.') return false;
    }
  }

  return true;
}

void
solve(int R, int C, int M) {
  for (uint b = 0; b < ((uint)1 << (R*C)); ++b) {
    if (count_bits(b) != M) continue;
    vector<string> board;
    
    for (int i = 0; i < R; ++i) {
      string r;
      for (int j = 0; j < C; ++j) {
        if (b & ((uint)1 << (i * C + j))) {
          r = r + "*";
        } else {
          r = r + ".";
        }
      }
      board.push_back(r);
    }

    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        if (board[i][j] == '.' && win(i, j, board)) {
          board[i][j] = 'c';
          for (int k = 0; k < R; ++k) {
            cout << board[k] << endl;
          }
          return;
        }
      }
    }
  }

  cout << "Impossible" << endl;
}

int
main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    int R, C, M;
    cin >> R >> C >> M;
    cout << "Case #" << t << ":" << endl;
    solve(R, C, M);
  }

  return 0;
}
