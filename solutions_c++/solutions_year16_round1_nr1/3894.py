#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <map>
using namespace std;

string solve(string input) {
  string result;
  for (int i=0;i<input.size();++i) {
    if (i==0) {
      result.insert(0,1,input[i]);
      continue;
    }
    if (result[0] <= input[i]) {
      result.insert(0,1,input[i]);
    } else {
      result += input[i];
    }
  }
return result;
}

int main(int argc, char* argv[]) {
  string filename = argv[1];
  ifstream ifs(filename.c_str());
  string line;
  getline(ifs,line);
  int numTests = atoi(line.c_str());
  for (int i=0;i<numTests;++i) {
    getline(ifs,line);
    string result = solve(line);
cout << "Case #" << i+1 << ": " << result << endl;
  }
}
