#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char * argv[]) {
  int T;
  char row1,row2,row3,row4,col1,col2,col3,col4,diag1,diag2;
  ifstream input;
  input.open(argv[1]);
  input >> T;
  for (int i=0; i<T; i++) {
    char game[4][4] = {0};
    for (int j=0; j<4; j++) {
      string row;
      input >> row;
      for (int k=0; k<4; k++) {
        game[j][k] = row[k];
      }
    }

    char winner = 'n';
    bool dot = false;

    // check rows
    for (int l=0; l<4; l++) {
      char first = game[l][0];
      for (int m=0; m<4; m++) {
        if (game[l][m] == '.') {
          dot = true;
          break;
        }
        if (game[l][m] != first && game[l][m] != 'T') break;
        if (m==3) {
          winner = first;
        }
      }
    }

    // check columns
    for (int l=0; l<4; l++) {
      char first = game[0][l];
      for (int m=0; m<4; m++) {
        if (game[m][l] == '.')
          break;
        if (game[m][l] != first && game[m][l] != 'T') break;
        if (m==3) {
          winner = first;
        }
      }
    }

    // check diagonals
    for (int n=0; n<4; n++) {
      char first = game[0][0];
      if (first == '.') break;
      if (game[n][n] != first && game [n][n] != 'T') break;
      if (n==3) {
        winner = first;
      }
    }
      
    for (int n=0; n<4; n++) {
      char first = game[0][3];
      if (first == '.') break;
      if (game[n][3-n] != first && game [n][3-n] != 'T') break;
      if (n==3)
        winner = first;
    }

    // output winner
    if (winner != 'n')
      cout << "Case #" << i+1 << ": " << winner << " won" << endl;
    else if (dot) 
      cout << "Case #" << i+1 << ": " << "Game has not completed" << endl;
    else
      cout << "Case #" << i+1 << ": " << "Draw" << endl;
  }
}

