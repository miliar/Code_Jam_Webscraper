#include <iostream>
#include <iomanip>   
#include <fstream>
#include <vector>
#include <string>

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
    // read input
    int X, R, C;
    input >> X >> R >> C;

    string winner;

    if(X == 1){
      winner = "GABRIEL";
    }
    else if(X == 2){
      winner = (R*C % 2 == 0)? "GABRIEL" : "RICHARD";
    }
    else if(X == 3){
       winner = (R*C % 3 == 0 && R > 1 && C > 1)? "GABRIEL" : "RICHARD";
    }
    else if(X == 4){
      winner = (R*C % 4 == 0 && R > 2 && C > 2)? "GABRIEL" : "RICHARD";
    }

    // write output file
    output << "Case #" << std::setprecision(7) << fixed << k+1 << ": " << winner << endl;
  }
  return 0;
}