#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
  string inPath = argv[1];
  string outPath = argv[2];

  // open two files
  ifstream input(inPath, std::ifstream::in);
  ofstream output(outPath, std::ios::out | std::ios::trunc);

  // read input file
  int nInput;
  input >> nInput;

  for(unsigned int k = 0; k < nInput; k++){
    // initialize table
    vector<int> magicNumber(17, 0);

    // read input
    for(unsigned int j = 0; j < 2; j++){
      int row, a, b, c, d;
      input >> row;
      for(unsigned int i = 0; i < 4; i++){
        input >> a >> b >> c >> d;
        if(i == row-1){
          magicNumber[a] += 1;
          magicNumber[b] += 1;
          magicNumber[c] += 1;
          magicNumber[d] += 1;
        }
      }
    }

    // compute output
    int answer, nCorrect = 0;
    for(unsigned int i = 0; i < 17; i++){
      if(magicNumber[i] == 2){
        answer = i;
        nCorrect ++;
      }
    }
    
    // write output file
    output << "Case #" << k+1 << ": ";
    if(nCorrect == 0){
      output << "Volunteer cheated!" << endl;
    }
    else if(nCorrect == 1){
      output << answer << endl;
    }
    else {
      output << "Bad magician!" << endl;
    }
  }

  return 0;
}