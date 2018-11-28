/*

  1 - as long as both dimensions are >= 3, 
 */

#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

void arrangeBoard(vector<char>& board, int R, int C, int M)
{
  // if there are only 2 rows, fill the columns starting from the right
  if (R == 2) {
    int noCols = M / 2;
    for (int r = 0; r < 2; ++r) {
      for (int c = C-noCols; c < C; ++c) {
	board[C*r + c] = '*';
      }
    }
  }
  // if there are only 2 columns, fill the rows starting from the bottom
  else if (C == 2) {
    std::fill(board.rbegin(), board.rbegin() + M, '*');
  }

  // start by filling as many bottom rows as possible (until 3 are left)
  else if (M < C*(R-3)) {

    // if there is one left to fill an entire row, send a mine up (cannot have a single blank in the row)
    if (M%C == C-1) {
      std::fill(board.rbegin(), board.rbegin() + M-1, '*');
      *(board.rbegin()+M+1) = '*';
    }
    else {
      std::fill(board.rbegin(), board.rbegin() + M, '*');
    }
  }

  else {

    std::fill(board.rbegin(), board.rbegin() + C*(R-3), '*');

  // then fill the last columns of the first three rows (until 3 columns are left    
    int remainingMines = M - C*(R-3);

    if (remainingMines < 3 * (C-3)) {
      // entire columns
      int noCols = remainingMines / 3;
      for (int r = 0; r < 3; ++r) {
	for (int c = C-noCols; c < C; ++c) {
	  board[C*r + c] = '*';
	}
      }

      int nextIdx = C*2+(C-noCols-1);
      switch(remainingMines%3) {
      case 2:
	board[nextIdx-1] = '*';
      case 1:
	board[nextIdx] = '*';
	break;
      }
    }
    
    // fill final 3x3 grid
    else {
      // entire columns
      for (int r = 0; r < 3; ++r) {
	for (int c = 3; c < C; ++c) {
	  board[C*r + c] = '*';
	}
      }

      remainingMines -= 3 * (C-3);
      switch(remainingMines) {
      case 5:
	board[C*0+2] = '*'; // r1 c3
	board[C*1+2] = '*'; // r2 c3
      case 3:
	board[C*2+0] = '*'; // r3 c1
	board[C*2+1] = '*'; // r3 c2
      case 1:
	board[C*2+2] = '*'; // r3 c3
	break;
      }
    }
  }
}

bool solveMinesweeper(vector<char>& board, int R, int C, int M)
{
  bool isPossible = false;

  board[0] = 'c';

  // POSSIBLE - zero Mines
  if (M == 0) {
    return true;
  }
  // POSSIBLE - single row / column boards
  if (R == 1 || C == 1) {

    std::fill(board.rbegin(), board.rbegin()+M, '*');

    return true;
  }

  // POSSIBLE - when M == R*C - 1
  else if (M == R*C - 1) {

    std::fill(board.begin()+1, board.end(), '*');

    return true;
  }

  // IMPOSSIBLE - when M == R*C - 2 or R*C - 3
  else if (M >= R*C - 3) {

    isPossible = false;
  }

  // double row / column
  else if (R == 2 || C == 2) {

    // IMPOSSIBLE - when M is odd
    if (M % 2 == 1) {
      isPossible =  false;
    }

    // POSSIBLE - when M is even
    else {
      isPossible = true;
    }
  }

  // for any board with both R and C larger than 3
  else {

    switch(R*C - M) {
      // IMPOSSIBLE - 5 or 7 free cells
    case 5:
    case 7:
      isPossible = false;
      break;

      // POSSIBLE - all other
    default:
      isPossible = true;
      break;
    }
  }

  // if possible, arrange board
  if (isPossible) {
    arrangeBoard(board, R, C, M);
  }

  return isPossible;
}

void print(vector<char> board, int R, int C)
{
  for (int r = 0; r < R; ++r) {
    for (int c = 0; c < C; ++c) {
      std::cout << board[C*r+c];
    }
    std::cout << std::endl;
  }
}

int main()
{

  int T;

  std::cin >> T;

  for (int i = 1; i <= T; ++i) {

    int R, C, M;

    std::cin >> R;
    std::cin >> C;
    std::cin >> M;

    vector<char> board(R*C, '.');

    std::cout << "Case #" << i << ":" << std::endl;
    if(solveMinesweeper(board, R, C, M)) {
      print(board, R, C);
    }
    else {
      std::cout << "Impossible" << std::endl;
    }
  }
  return 0;
}
