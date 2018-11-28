#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <numeric>

#define MAXN 50

using namespace std;

int nrows, ncols, numMines, numVacant;
char M[MAXN + 5][MAXN + 5];
bool found[MAXN + 5][MAXN + 5];

const char BOARD[][6] = {
"....*",
"...**",
"...**",
"*****",
"*****"
};

bool valid(int r, int c) {
  return r >= 0 && r < nrows && c >= 0 && c < ncols;
}

void readGameBoardSpec() {
  scanf("%d%d%d", &nrows, &ncols, &numMines);
  numVacant = nrows * ncols - numMines;
}

int traverse(int r, int c) {
  // cout << r << " " << c << endl;
  if (found[r][c]) {
    return 0;
  }
  found[r][c] = true;
  int numBoms = 0;
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      if (i != 0 || j != 0) {
        int rr = r + i, cc = c + j;
        if (valid(rr, cc) && M[rr][cc] == '*') {
          numBoms++;
        }
      }
    }
  }
  // cout << r << " " << c << " -- " << numBoms << endl;
  if (numBoms > 0) {
    return 1;
  }
  int ret = 1;
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      if (i != 0 || j != 0) {
        int rr = r + i, cc = c + j;
        if (valid(rr, cc) && M[rr][cc] == '.') {
          ret += traverse(rr, cc);
        }
      }
    }
  }
  return ret;
}

bool solveGameBoard() {
  if (numVacant == 1) {
    for (int i = 0; i < nrows; i++) {
      for (int j = 0; j < ncols; j++) {
        M[i][j] = '*';
      }
    }
    M[0][0] = 'c';
    return true;
  }
  int A[nrows * ncols + 2];
  for (int i = 0; i < nrows * ncols; i++) {
    if (i < numVacant) {
      A[i] = 0;
    } else {
      A[i] = 1;
    }
  }

  do {
    // cout << "come " << endl;
    int ctr = 0;
    for (int i = 0; i < nrows; i++) {
      for (int j = 0; j < ncols; j++) {
        if (A[ctr]) {
          M[i][j] = '*';
        } else {
          M[i][j] = '.';
        }
        ctr++;
      }
    }

    int fr = -1, fc = -1;
    for (int r = 0; r < nrows; r++) {
      for (int c = 0; c < ncols; c++) {
        if (M[r][c] == '*') {
          continue;
        }
        int numBoms = 0;
        for (int i = -1; i <= 1; i++) {
          for (int j = -1; j <= 1; j++) {
            if (i != 0 || j != 0) {
              int rr = r + i, cc = c + j;
              if (valid(rr, cc) && M[rr][cc] == '*') {
                numBoms++;
              }
            }
          }
        }
        if (numBoms == 0) {
          fr = r;
          fc = c;
          break;
        }
      }
      if (fr != -1) {
        break;
      }
    }
    if (fr == -1) {
      continue;
    }
    // cout << "almost" << endl;
    memset(found, 0, sizeof(found));
    if (traverse(fr, fc) == numVacant) {
      /*
      cout << fr << " -- " << fc << endl;
      for (int i = 0; i < nrows; i++) {
        for (int j = 0; j < ncols; j++) {
        }
      }
      */
      M[fr][fc] = 'c';
      // cout << "gotrue" << endl;
      return true;
    }
    // cout << "go" << endl;
  } while (next_permutation(A, A + (nrows * ncols)));
  return false;
}

void printGameBoard() {
  for (int i = 0; i < nrows; i++) {
    for (int j = 0; j < ncols; j++) {
      printf("%c", M[i][j]);
    }
    printf("\n");
  }
}

int main() {
  /*
  nrows = ncols = 5;
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
      M[i][j] = BOARD[i][j];
      printf("%c", M[i][j]);
    }
    printf("\n");
  }
  cout << traverse(1, 1) << endl;
  */
  int nTC, tc = 0;
  scanf("%d", &nTC);
  while (++tc && nTC--) {
    readGameBoardSpec();
    printf("Case #%d:\n", tc);
    if (solveGameBoard()) {
      printGameBoard();
    } else {
      printf("Impossible\n");
    }
  }
  return 0;
}

