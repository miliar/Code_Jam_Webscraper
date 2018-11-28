#include <iostream>

using namespace std;

char board[4][4];

int main() {
  int nX, nO, nT;
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {

    cout << "Case #" << (i + 1) << ": ";
    for (int r = 0; r < 4; r++) {
      string line;
      cin >> line;

      for (int c = 0; c < 4; c++) {
        board[r][c] = line[c];
      }
    }

    string blank;
    getline(cin, blank);

    // check each row
    for (int r = 0; r < 4; r++) {
      int numX = 0;
      int numO = 0;
      int numT = 0;
      for (int c = 0; c < 4; c++) {
        if (board[r][c] == 'X') {
          numX++;
        } else if (board[r][c] == 'O') {
          numO++;
        } else if (board[r][c] == 'T') {
          numT++;
        }
      }
      //cout << numX << " " << numY << " " << numT << endl;
      if (numX + numT == 4) {
        cout << "X won" << endl;
        goto DONE;
      }
      if (numO + numT == 4) {
        cout << "O won" << endl;
        goto DONE;
      }
    }

    for (int c = 0; c < 4; c++) {
      int numX = 0;
      int numO = 0;
      int numT = 0;
      for (int r = 0; r < 4; r++) {
        if (board[r][c] == 'X') {
          numX++;
        } else if (board[r][c] == 'O') {
          numO++;
        } else if (board[r][c] == 'T') {
          numT++;
        }
      }
      //cout << numX + numT << " " << numY + numT << endl;
      if (numX + numT == 4) {
        cout << "X won" << endl;
        goto DONE;
      }
      if (numO + numT == 4) {
        cout << "O won" << endl;
        goto DONE;
      }
    }

    nX = 0;
    nO = 0;
    nT = 0;
    for (int d = 0; d < 4; d++) {
      if (board[d][d] == 'X') {
        nX++;
      } else if (board[d][d] == 'O') {
        nO++;
      } else if (board[d][d] == 'T') {
        nT++;
      }
    }

    if (nX + nT == 4) {
      cout << "X won" << endl;
      goto DONE;
    } else if (nO + nT == 4) {
      cout << "O won" << endl;
      goto DONE;
    }

    nX = 0;
    nO = 0;
    nT = 0;
    for (int d = 0; d < 4; d++) {
      if (board[d][3 -d] == 'X') {
        nX++;
      } else if (board[d][3 - d] == 'O') {
        nO++;
      } else if (board[d][3 - d] == 'T') {
        nT++;
      }
    }

    if (nX + nT == 4) {
      cout << "X won" << endl;
      goto DONE;
    } else if (nO + nT == 4) {
      cout << "O won" << endl;
      goto DONE;
    }

    for (int r = 0; r < 4; r++) {
      for (int c = 0; c < 4; c++) {
        if (board[r][c] == '.') {
          cout << "Game has not completed" << endl;
          goto DONE;
        }
      }
    }

    cout << "Draw" << endl;

    DONE:
      int donothing;
  }
}
