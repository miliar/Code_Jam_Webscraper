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
    int Smax;
    string s;
    input >> Smax >> s;
    
    // parse input
    int clapping = 0;
    int needed = 0;
    for(int i = 0; i < s.size(); i++){
      //cout << i << "/" << s[i] - '0' << "/" << clapping << "/" << needed << endl;
      if(clapping < i){
        needed ++;
        clapping ++;
      }
      clapping += s[i] - '0';
    }
    //cout << "*" << "/" << "*" << "/" << clapping << "/" << needed << endl;
    //cout << "--------" << endl;
    // write output file
    output << "Case #" << std::setprecision(7) << fixed << k+1 << ": " << needed << endl;
  }

  return 0;
}