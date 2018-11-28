#include <iostream>
using namespace std;

string board[4];

bool check_player(char s) {
  for (int i = 0; i < 4; i++) {
    int c = 0;
    for (int j = 0; j < 4; j++) {
      if (board[i][j] == s || board[i][j] == 'T') ++c;
    }
    if (c > 3) return true;
  }
  for (int i = 0; i < 4; i++) {
    int c = 0;
    for (int j = 0; j < 4; j++) {
      if (board[j][i] == s || board[j][i] == 'T') ++c;
    }
    if (c > 3) return true;
  }

  int c = 0;
  for (int i = 0; i < 4; ++i) {
    if (board[i][i] == s || board[i][i] == 'T') ++c;
  }
  if (c > 3) return true;

  c = 0;
  for (int i = 0; i < 4; ++i) {
    if (board[i][3 - i] == s || board[i][3 - i] == 'T') ++c;
  }
  if (c > 3) return true;

  return false;
}

int main () {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    for (int j = 0; j < 4; j++) cin >> board[j];

    bool is_remaining = false;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        is_remaining = is_remaining || board[i][j] == '.';
      }
    }

    bool x_won = check_player('X');
    bool o_won = check_player('O');

    if (x_won) {
      cout << "Case #" << t + 1 << ": X won";
    } else if (o_won) {
      cout << "Case #" << t + 1 << ": O won";
    } else if (!is_remaining) {
      cout << "Case #" << t + 1 << ": Draw";
    } else {
      cout << "Case #" << t + 1 << ": Game has not completed";
    }
    cout << endl;
  }
}
