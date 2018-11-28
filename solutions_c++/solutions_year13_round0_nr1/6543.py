#include <iostream>

using namespace std;

const unsigned int SIZE = 4;
const unsigned int VERTICAL   = 1;
const unsigned int HORIZONTAL = 2;
const unsigned int DIAGONAL   = 3;

char solveForWinner(char matrix[][SIZE], const unsigned int mode); 

int main() {
  char matrix[SIZE][SIZE];
  unsigned int T;

  // Read in # test cases
  cin >> T;
  for (unsigned int i = 1; i <= T; ++i) {
    // Read matrix
    bool fully_occupied = true;
    for (unsigned int row = 0; row < SIZE; ++row) {
      for (unsigned int col = 0; col < SIZE; ++col) {
	cin >> matrix[row][col];

	// See if the matrix has at least one empty spot
	if (matrix[row][col] == '.') {
	  fully_occupied = false;
	}
      }
    }

    // Solve
    char win_player = solveForWinner(matrix, HORIZONTAL);
    if (win_player == '.') {
      win_player = solveForWinner(matrix, VERTICAL);
    }
    if (win_player == '.') {
      win_player = solveForWinner(matrix, DIAGONAL);
    }

    // Print
    if (win_player == 'X' || win_player == 'O') {
      cout << "Case #" << i << ": " << win_player << " won\n";
    } else if (fully_occupied) {
      cout << "Case #" << i << ": Draw\n";
    } else {
      cout << "Case #" << i << ": Game has not completed\n";
    }
  }

  return 0;
}

char solveForWinner(char matrix[][SIZE], const unsigned int mode) {
  for (unsigned int i = 0; i < SIZE; ++i) {
    char player = '.';
    for (unsigned int j = 0; j < SIZE; ++j) {
      char candidate;
      if (mode == VERTICAL) {
	candidate = matrix[j][i];
      } else if (mode == HORIZONTAL) {
	candidate = matrix[i][j];
      } else {
	if (i == 0) {
	  candidate = matrix[j][j];
	} else {
	  candidate = matrix[j][i - j];
	}
      }

      if (candidate == 'T') {
	continue;
      } else if (candidate == '.' || 
		 (candidate != player && player != '.')) {
	// No possible win
	player = '.';
	break;
      }

      player = candidate;
    }

    // We have a winner
    if (player != '.') {
      return player;
    }

    // For diagonal, we only execute the outer loop twice
    if (mode == DIAGONAL) {
      i += SIZE - 2;
    }
  }

  // No winner
  return '.';
}
