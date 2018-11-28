#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  int tests;
  int match, matches;
  int answer1, answer2;
  int grid1[4][4];
  int grid2[4][4];
  int possibleCards[8];
  
  ifstream fin;
  fin.open("input.txt");
  
  ofstream fout;
  fout.open("output.txt");
  
  fin >> tests;
  
  int i,j,k;
  for (i = 0; i < tests; i++) {
    fin >> answer1;
    for (j = 0; j < 4; j++) {
      for (k = 0; k < 4; k++) {
        fin >> grid1[j][k];
        cout << grid1[j][k] << " ";
      }
      cout << endl;
    }
    fin >> answer2;
    for (j = 0; j < 4; j++) {
      for (k = 0; k < 4; k++) {
        fin >> grid2[j][k];
        cout << grid2[j][k] << " ";
      }
      cout << endl;
    }
    
    matches = 0;
    for (j = 0; j < 4; j++) {
      for (k = 0; k < 4; k++) {
        cout << grid1[answer1-1][j] << " " << grid2[answer2-1][k] << endl;
        if(grid1[answer1-1][j] == grid2[answer2-1][k]){
          match = grid1[answer1-1][j];
          ++matches;
        }
      }
    }
    
    if(matches == 1){
      fout << "Case #" << (i+1) << ": " << match << endl;
    }
    else if(matches > 1){
      fout << "Case #" << (i+1) << ": Bad magician!" << endl;
    }
    else{
      fout << "Case #" << (i+1) << ": Volunteer cheated!" << endl;
    }
  
  }


};