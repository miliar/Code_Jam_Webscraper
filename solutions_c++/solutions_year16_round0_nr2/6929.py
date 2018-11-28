#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <map>
using namespace std;

int solve(string input) {
  if(input.find('-') == string::npos) {
    return 0;
  }
  int numTurns = 0;
  while (input.find('-') != string::npos) {

    char first = input[0];
    char alternate = (first=='+')?'-':'+';
    size_t pos = input.find_first_of(alternate);
    if (pos == string::npos) {
      return ++numTurns;
    }
    input.replace(0,pos,pos,alternate);
    numTurns++;
  }
  return numTurns;
}

int main(int argc, char* argv[]) {
  string filename = argv[1];
  ifstream ifs(filename.c_str());
  string line;
  getline(ifs,line);
  int numTests = atoi(line.c_str());
  for (int i=0;i<numTests;++i) {
    getline(ifs,line);
    int result = solve(line);
    cout << "Case #" << i+1 << ": " << result << endl;
  }
}
