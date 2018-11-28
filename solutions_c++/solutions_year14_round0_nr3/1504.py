#include <cstdio>
#include <iostream>

using namespace std;

char board[50][50];

int main() {
   int n;
   scanf("%d", &n);
   
   for (int t = 1; t <= n; ++t) {
      int r, c, m;
      
      scanf("%d%d%d", &r, &c, &m);
      
      //printf("Case #%d: r: %d, c: %d, m: %d\n", t, r, c, m);
      
      //Can't believe you missed this 
      if (m == r * c - 1) {
         printf("Case #%d:\n", t);
         for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
               if (i == 0 && j == 0) {
                  printf("c");
               } else {
                  printf("*");
               }
            }
            printf("\n");
         }
         continue;
      }
      
      int total = r*c;
      
      if (r == 1 || c == 1) {
         if (m > max(r, c) - 2 && m != 0) {
            printf("Case #%d:\nImpossible\n", t);
            continue;
         }
      } else if (m >= (total - 3)) {
         printf("Case #%d:\nImpossible\n", t);
         continue;
      }
      
      for (int i = 0; i < r; ++i) {
         for (int j = 0; j < c; ++j) {
            board[i][j] = '.';
         }
      }

      int mines = 0;
      
      board[0][0] = 'c';

      if (m == c - 1 && c % 2 == 0 && r % 2 == 0 && r > 2 && c > 2) {
         for (int i = r - 1; r > 1 && mines < m; --i) {
            for (int j = c - 1; j > 1 && mines < m; --j) {
               board[i][j] = '*';
               mines++;
            }
         }
      }

      int row;
      for (row = r - 1; row > 1; --row) {
         //if (m - mines != c - 1) {
            if (m - mines >= c || ((m - mines) % c) <= c - 2) {
               for (int j = c - 1; j >= 0 && m - mines > 0; --j) {
                  board[row][j] = '*';
                  mines++;
               }
            } else {
               break;
            }
         //}
      }
      
      //if ((m - mines) % 2 == 1) {
         if (row > 2 && (m - mines) <= 2 * (c - 2)) {
         
            for (int i = c - 1; i > 1 && m - mines > 0; --i) {
               if (m - mines > 0) {
                  board[row][i] = '*';
                  mines++;
               }
               if (m - mines > 0) {
                  board[row-1][i] = '*';
                  mines++;
               }
            }
         }
      //}

      int col;
      for (col = c - 1; col > 1 && row != 1; --col) {
         if (m - mines >= row + 1) {
            for (int j = 0; j <= row; ++j) {
               board[j][col] = '*';
               mines++;
            }
         } else {
            break;
         }
      }
      
      
      //cout << "Row: " << row << " Col: " << col << " left: " << m - mines << endl;
      
      for (int i = row; i > 1; --i) {
         if (m - mines < col - 1) {
            for (int j = col; j > 1 && m - mines > 0; --j) {
               board[i][j] = '*';
               mines++;
            }
         }
      }
      
      //cout << "Mines left: " << m - mines << endl;
      if ((m - mines) % 2 == 1) {
         if (c <= 3 || r <= 2 || ((m - mines + 3) >= (c - 2) * 2)) {
            printf("Case #%d:\nImpossible\n", t);
            continue;
         } else {
            if (board[2][0] == '*' && board[2][1] == '*' && board[2][2] == '*') {
               board[2][0] = '.';
               board[2][1] = '.';
               board[2][2] = '.';
               mines -= 3;
            }
         }
      } 

      for (int i = c - 1; i > 1 && mines < m; --i) {
         if (board[2][i] != '.' || r <= 2) {
         board[0][i] = '*';
         board[1][i] = '*';
         mines += 2;
         }
      }
      
      printf("Case #%d:\n", t);
      if (m - mines == 0) {
         for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
               printf("%c", board[i][j]);
            }
            printf("\n");
         }      
      } else {
         printf("Impossible\n", t);
      }
   }

   return 0;
}