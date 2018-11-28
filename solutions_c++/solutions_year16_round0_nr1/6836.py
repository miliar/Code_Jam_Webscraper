#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <map>
using namespace std;

int targetRequired = 55;
string solve(int N) {
  if (!N%5) {
    return "INSOMNIA";
  }
  map<int,bool> numberMap;
  for (int i=0;i<9;++i) {
    numberMap[i] = false;
  }
  int multiplier = 1;
  int NM;
  while(targetRequired > 0) {
    NM = N*multiplier;
    multiplier++;
    string NasString = to_string(NM);
    for (int i=0;i<NasString.size();++i) {
      int d = NasString[i] - '0';
      //cout << "procesisng digit " << d << " of number " <<  NasString <<  " Char: " << NasString[i] << endl;
      if (!numberMap[d]) {
        if (d) {
          targetRequired-=d;
        } else {
          targetRequired-=10;
        }
        numberMap[d] = true;
      }
    }
  }
  return to_string(N*(multiplier-1));
}




int main(int argc, char* argv[]) {
  string filename = argv[1];
  ifstream ifs(filename.c_str());
  string line;
  getline(ifs,line);
  int numTests = atoi(line.c_str());
  for (int i=0;i<numTests;++i) {
    getline(ifs,line);
    int N = atoi(line.c_str());
    targetRequired=55;
    string result = solve(N);
    cout << "Case #" << i+1 << ": " << result << endl;
  }
}
