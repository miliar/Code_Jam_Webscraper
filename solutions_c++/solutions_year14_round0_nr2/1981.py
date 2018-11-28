#include <iostream>
#include <iomanip>   
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
    // read input
    double C, F, X;
    input >> C >> F >> X;
    
    // compute output
    double t = X/2.f, tPrev;
    int nFarm = 0;
    do{
      tPrev = t;
      t += X/(2+(nFarm+1)*F) + (C-X)/(2+nFarm*F);
      nFarm ++;
    }while(t < tPrev);
    
    // write output file
    output << "Case #" << std::setprecision(7) << fixed << k+1 << ": " << tPrev << endl;
  }

  return 0;
}