#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int grid_one[4][4];
int grid_two[4][4];

int main() {
  ifstream readFile;
  ofstream writeFile;
  readFile.open("qualA_small.txt");
  writeFile.open("solution_qualA_small.txt");

  int numTestCases, rowNum_one, rowNum_two, n, answer;
  readFile >> numTestCases;
  
  for(int i = 0; i < numTestCases; i++) {
    answer = -1;
    readFile >> rowNum_one;
    
    for(int j = 0; j < 4; j++){
      for(int k = 0; k < 4; k++){
	readFile >> grid_one[j][k];
      }
    }

    readFile >> rowNum_two;

    for(int j = 0; j < 4; j++){
      for(int k = 0; k < 4; k++){
	readFile >> grid_two[j][k];
      }
    }

    for(int j = 0; j < 4; j++){
      for(int k = 0; k < 4; k++){
	if(grid_one[rowNum_one - 1][j] == grid_two[rowNum_two - 1][k] && answer==-1) {
	  //cout << "First repeated value: " << grid_one[rowNum_one][j] << endl;
	  answer = grid_one[rowNum_one - 1][j];
	}else if(grid_one[rowNum_one - 1][j] == grid_two[rowNum_two - 1][k]) {
	  answer = 0;
	}
      }
    }
    
    if(answer > 0){
      writeFile << "Case #" << i + 1 << ": " << answer << endl;
    } else if(answer == 0){
      writeFile << "Case #" << i + 1 << ": Bad magician!" << endl;
    } else {
      writeFile << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
    }
  }
  return 0;
}
