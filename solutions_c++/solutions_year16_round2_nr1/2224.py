#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

//"", "ONE", "", "THREE", "FOUR", "", "", "", "", ""
// ONE THREE FOUR FIVE SEVEN EIGHT NINE 
string solve(string line) {
  vector<int> resultAsVec;
  while(line.find_first_of('Z') != string::npos) {
    line.replace(line.find_first_of('Z'),1,"");
    line.replace(line.find_first_of('E'),1,"");
    line.replace(line.find_first_of('R'),1,"");
    line.replace(line.find_first_of('O'),1,"");
    resultAsVec.push_back(0);
  }
  while(line.find_first_of('X') != string::npos) {
    line.replace(line.find_first_of('S'),1,"");
    line.replace(line.find_first_of('I'),1,"");
    line.replace(line.find_first_of('X'),1,"");
    resultAsVec.push_back(6);
  }
  while(line.find_first_of('W') != string::npos) {
    line.replace(line.find_first_of('T'),1,"");
    line.replace(line.find_first_of('W'),1,"");
    line.replace(line.find_first_of('O'),1,"");
    resultAsVec.push_back(2);
  }
  while(line.find_first_of('U') != string::npos) {
    line.replace(line.find_first_of('F'),1,"");
    line.replace(line.find_first_of('O'),1,"");
    line.replace(line.find_first_of('U'),1,"");
    line.replace(line.find_first_of('R'),1,"");
    resultAsVec.push_back(4);
  }

  while(line.find_first_of('F') != string::npos) {
    line.replace(line.find_first_of('F'),1,"");
    line.replace(line.find_first_of('I'),1,"");
    line.replace(line.find_first_of('V'),1,"");
    line.replace(line.find_first_of('E'),1,"");
    resultAsVec.push_back(5);
  }
  while(line.find_first_of('V') != string::npos) {
    line.replace(line.find_first_of('S'),1,"");
    line.replace(line.find_first_of('E'),1,"");
    line.replace(line.find_first_of('V'),1,"");
    line.replace(line.find_first_of('E'),1,"");
    line.replace(line.find_first_of('N'),1,"");
    resultAsVec.push_back(7);
  }
  while(line.find_first_of('G') != string::npos) {
    line.replace(line.find_first_of('E'),1,"");
    line.replace(line.find_first_of('I'),1,"");
    line.replace(line.find_first_of('G'),1,"");
    line.replace(line.find_first_of('H'),1,"");
    line.replace(line.find_first_of('T'),1,"");
    resultAsVec.push_back(8);
  }
  while(line.find_first_of('I') != string::npos) {
    line.replace(line.find_first_of('N'),1,"");
    line.replace(line.find_first_of('I'),1,"");
    line.replace(line.find_first_of('N'),1,"");
    line.replace(line.find_first_of('E'),1,"");
    resultAsVec.push_back(9);
  }
  while(line.find_first_of('N') != string::npos) {
    line.replace(line.find_first_of('O'),1,"");
    line.replace(line.find_first_of('N'),1,"");
    line.replace(line.find_first_of('E'),1,"");
    resultAsVec.push_back(1);
  }
  while(line.find_first_of('T') != string::npos) {
    line.replace(line.find_first_of('T'),1,"");
    line.replace(line.find_first_of('H'),1,"");
    line.replace(line.find_first_of('R'),1,"");
    line.replace(line.find_first_of('E'),1,"");
    line.replace(line.find_first_of('E'),1,"");
    resultAsVec.push_back(3);
  }
  string result;
  sort(resultAsVec.begin(),resultAsVec.end());
  for (int i=0;i<resultAsVec.size();++i) {
    result += to_string(resultAsVec[i]);
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
    cout << "Case #" << i+1 << ": " << solve(line) << endl;
  }
}
