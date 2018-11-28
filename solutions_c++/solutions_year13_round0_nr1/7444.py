#include <queue>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>

using namespace std;

void printBoard(int board[4][4]);
int checkValue(int res) {
   if (res == 1 || res == 3) { // 1 * 1 * 1 * 1 || 1 * 1 * 1 * 3 (where T == 3)
      cout << "X won\n";
      return 1;
   } else if (res == 16 || res == 24) { // 2 * 2 * 2 * 2 || 2 * 2 * 2 * 3
      cout << "O won\n";
      return 1; 
   }
   return 0;
}


void evaluateBoard(int board[4][4]) {
   int res = 0;
   // check each row
   for (int cases = 0; cases < 4; cases++) {
      res = board[cases][0] * board[cases][1] * board[cases][2] * board[cases][3];
      if (checkValue(res)) return;
   }

   // check each column 
   for (int cases = 0; cases < 4; cases++) {
      res = board[0][cases] * board[1][cases] * board[2][cases] * board[3][cases];
      if (checkValue(res)) return;
   }

   // check the 2 diagonals
   res = board[0][0] * board[1][1] * board[2][2] * board[3][3];
   if (checkValue(res)) return;
   res = board[0][3] * board[1][2] * board[2][1] * board[3][0];
   if (checkValue(res)) return;

   res = 1;
   for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
         res *= board[i][j];
      }
   }

   if (res == 0) {
      cout << "Game has not completed\n";
   } else {
      cout << "Draw\n";
   }
}

void printBoard(int board[4][4]) {
   for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
         cout << board[i][j];
      }
      cout << endl;
   }
}

int main(void) {
   int numProblems;
   std::string line, word;
   // process the first line containing rows, column, non zero entry counts
   getline(cin, line);
   numProblems = atoi(line.c_str());
   int board[4][4];
   for (int count = 0; count < numProblems; count++) {
      for (int lines = 0; lines < 4; lines++) {
         getline(cin, line);
         //cout << "'" << line << "'" << line.length() << endl;
         for (int index = 0; index < 4; index++) {
            if (line[index] == '.') {
               board[lines][index] = 0;
            } else if (line[index] == 'X') {
               board[lines][index] = 1;
            } else if (line[index] == 'O') {
               board[lines][index] = 2;
            } else if (line[index] == 'T') {
               board[lines][index] = 3;
            }
         }
      }
      //printBoard(board);
      cout << "Case #" << (count+1) << ": ";
      evaluateBoard(board);
      getline(cin, line);
   }
   return 0;
}


