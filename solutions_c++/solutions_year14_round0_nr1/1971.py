#include <iostream>
#include <fstream>

using namespace std;

int main () {
  
  int a1[4][4];
  int a2[4][4];
  ifstream in;
  in.open("pa.in");
  ofstream out;
  out.open("pa.out");
  int T;
  in >> T;
  int row1, row2, res, t = 1;
  while (t <= T) {
    res = -1;

    in >> row1;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        in >> a1[i][j];
      }
    }

    in >> row2;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        in >> a2[i][j];
      }
    }

    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        if (a1[row1-1][i] == a2[row2-1][j]) {
          if (res == -1) {
            res = a1[row1-1][i];
          } else {
            res = 20;
            break;
          }
        }
      }
    }
    
    if (res == -1) {
      out << "Case #" << t << ": " << "Volunteer cheated!"; 
    } else if (res > 16) {
      out << "Case #" << t << ": " << "Bad magician!";
    } else {
      out << "Case #" << t << ": " << res;
    }
    if (t != T) out << "\n";
    t++;
  }
}
