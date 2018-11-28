#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
  int row1[4], row2[4], temp;
  int numCases, rowIndex1, rowIndex2;
  int i, j, k;
  int numMatch, cardValue;
  ifstream infile;
  ofstream outfile;

  infile.open("A-small-attempt0.in");
  outfile.open("output.txt");

  infile >> numCases;
  for (i = 0; i < numCases; i++){
    numMatch = 0;

    infile >> rowIndex1;
    for (j = 0; j < 4; j++)
      for (k = 0; k < 4; k++){
        if (j == (rowIndex1 - 1)){
          infile >> row1[k];
        } else { infile >> temp; }
      }

    infile >> rowIndex2;
    for (j = 0; j < 4; j++)
      for (k = 0; k < 4; k++){
        if (j == (rowIndex2 - 1)){
          infile >> row2[k];
        } else { infile >> temp; }
      }

    for (j = 0; j < 4; j++)
      for (k = 0; k < 4; k++){
        if (row1[j] == row2[k]){
          numMatch ++;
          cardValue = row1[j];
        }
      }

    outfile << "Case #" << i+1 << ":  ";
    switch (numMatch){
      case 0: 
		outfile << "Volunteer cheated!\n";
		break;
      case 1: 
		outfile << cardValue << "\n";
	 	break;
      default: 
		outfile << "Bad magician!\n";
    }
    
  }

  infile.close();
  outfile.close();
  return 0;
}
