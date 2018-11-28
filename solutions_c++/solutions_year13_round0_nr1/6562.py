#include <stdio.h>
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;



void output(int table[4][4]) {
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      cout << table[i][j];
    }
  }
}

int winner(int table[4][4]) {
  int ti, tj, n;
  bool tb = false,
       ob = false,
       xb = false;
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (table[i][j] == 3) {
        ti = i; tj = j;
        tb = true; break;
      }
    }
  }

  // See if X is winner
  n = 1;
  if (tb) {table[ti][tj] = n;}
  for (int i = 0; i < 4; i++) {
    if (table[i][0] == n && table[i][1] == n && table[i][2] == n && table[i][3] == n) {
        xb = true; break;
    } else if (table[0][i] == n && table[1][i] == n && table[2][i] == n && table[3][i] == n) {
        xb = true; break;
    }
  }
  if (table[0][0] == n && table[1][1] == n && table[2][2] == n && table[3][3] == n) {
        xb = true;
  } else if (table[3][0] == n && table[2][1] == n && table[1][2] == n && table[0][3] == n) {
        xb = true;
  }

  if (xb) return n;

  // See if O is winner
  n = 2;
  if (tb) {table[ti][tj] = n;}
  for (int i = 0; i < 4; i++) {
    if (table[i][0] == n && table[i][1] == n && table[i][2] == n && table[i][3] == n) {
        ob = true; break;
    } else if (table[0][i] == n && table[1][i] == n && table[2][i] == n && table[3][i] == n) {
        ob = true; break;
    }
  }
  if (table[0][0] == n && table[1][1] == n && table[2][2] == n && table[3][3] == n) {
        ob = true;
  } else if (table[3][0] == n && table[2][1] == n && table[1][2] == n && table[0][3] == n) {
        ob = true;
  }

  if (ob) return n;

  // See if Game has not completed
  n = 0;
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
      if (table[i][j] == 0) {
        return n;
      }
    }
  }

  // draw
  n = 3;
  return n;

}

int main() {
  int nrGames, result;
  int table[4][4];
// X = 1, O = 2, T = 3, . = 0
    FILE *f,*f2;
    f=fopen("A.in","r");
    f2=fopen("A.out","w");
    if(f==NULL){return 0;}


  fscanf(f, "%d", &nrGames);

  for (int w = 1; w <= nrGames; w++) {
fgetc(f);

//    read(table);
// read
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {

      char ch = fgetc(f);

      if (ch == 'X') {
         table[i][j] = 1;
      } else if (ch == 'O') {
          table[i][j] = 2;
      } else if (ch == 'T') {
          table[i][j] = 3;
      } else {
          table[i][j] = 0;
      }

    }
    fgetc(f);
  }
// end read

//    output(table);
    result = winner(table);

    if (result == 1) { fprintf(f2, "Case #%d: X won\n", w);}
    else if (result == 2) { fprintf(f2, "Case #%d: O won\n", w);}
    else if (result == 3) { fprintf(f2, "Case #%d: Draw\n", w);}
    else { fprintf(f2, "Case #%d: Game has not completed\n", w);}
  }

return 0;
}
