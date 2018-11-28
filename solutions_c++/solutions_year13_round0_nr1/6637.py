#include <iostream>

using namespace std;

char board[4][4];

bool IsType(char value, bool is_x) {
  if (value == 'T') {
    return true;
  } else if (is_x) {
    return (value == 'X');
  } else {
    return (value == 'O');
  }
}

bool TestRow(int row, bool is_x) {
  for (int xx = 0; xx < 4; ++xx) {
    if (!IsType(board[row][xx], is_x)) {
      return false;
    }
  }
  return true;
}

bool TestAllRow(bool is_x) {
  for (int row = 0; row < 4; ++row) {
    if (TestRow(row, is_x)) {
      return true;
    }
  }
  return false;
}

bool TestCol(int col, bool is_x) {
  for (int xx = 0; xx < 4; ++xx) {
    if (!IsType(board[xx][col], is_x)) {
      return false;
    }
  }
  return true;
}

bool TestAllCol(bool is_x) {
  for (int col = 0; col < 4; ++col) {
    if (TestCol(col, is_x)) {
      return true;
    }
  }
  return false;
}

bool TestDiag(bool fall, bool is_x) {
  for (int xx = 0; xx < 4; ++xx) {
    if (!IsType(board[fall ? xx : 3-xx][xx], is_x)) {
      return false;
    }
  }
  return true;
}

bool TestAllDiag(bool is_x) {
  return TestDiag(false, is_x) || TestDiag(true, is_x);
}

bool TestAll(bool is_x) {
  return TestAllRow(is_x) || TestAllCol(is_x) || TestAllDiag(is_x);
}

int main() {

  int cases;
  cin >> cases;

  for (int cc = 0; cc < cases; ++cc) {
    cout << "Case #" << (cc + 1) << ": ";

    bool game_done = true;
    for (int aa = 0; aa < 4; ++aa) {
      for (int bb = 0; bb < 4; ++bb) {
        cin >> board[aa][bb];
        if (board[aa][bb] == '.') {
          game_done = false;
        }
      }
    }

    if (TestAll(true)) {
      cout << "X won";
    } else if (TestAll(false)) {
      cout << "O won";
    } else if (game_done) {
      cout << "Draw";
    } else {
      cout << "Game has not completed";
    }
    cout << "\n";
  }

  return 0;
}
