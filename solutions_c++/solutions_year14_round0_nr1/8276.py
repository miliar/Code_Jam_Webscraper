#include <iostream>
#include <fstream>

using namespace std;

int main() {
  int T, arr1[5][5], arr2[5][5], a1, a2, tmp, match;
  ifstream fin;
  ofstream fout;
  fin.open("input.txt");
  fout.open("output.txt");
  fin >> T;
  for (int i = 1; i <= T; ++i) {
    match = -1;
    fin >> a1;
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        fin >> arr1[j][k];
      }
    }
    fin >> a2;
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        fin >> arr2[j][k];
      }
    }
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        if (arr1[a1 - 1][j] == arr2[a2 - 1][k]) {
          if (match != -1) {
            match = 0;
          } else {
            match = arr1[a1 - 1][j];
          }
        }
      }
    }
    if (match == -1) {
      fout << "Case #" << i << ": Volunteer cheated!\n";
    } else if (match == 0) {
      fout << "Case #" << i << ": Bad magician!\n";
    } else {
      fout << "Case #" << i << ": " << match << endl; 
    }
  }
  fin.close();
  fout.close();
  return 0;
}