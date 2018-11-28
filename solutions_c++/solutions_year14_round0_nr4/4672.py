#include <iostream>
#include <istream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iomanip>
using namespace std;

int numbricks = 0;
int currentCase = 0;
vector<double> naobricks;
vector<double> kenbricks;

void printDoubleVect(vector<double> & vect) {
  vector<double>::iterator it = vect.begin();
  while (it != vect.end()) {
    cout << " " << setprecision(10) << *it ;
    it++;
  }
  cout << endl;
}

vector<string> split(const string &s, const char* delim) {
  vector<string> itemarr;
  stringstream ss(s);
  string item;
  while (getline(ss, item, *delim)) {
    itemarr.push_back(item);
  }
  return itemarr;
}

vector<double> stringArrToDoubleArr(vector<string> stringarr) {
  vector<double> itemarr;
  vector<string>::iterator it = stringarr.begin();
  while (it != stringarr.end()) {
    itemarr.push_back(atof((*it).c_str()));
    it++;
  }
  return itemarr;
}

void sortIncreasing(vector<double> & arr) {
  sort(arr.begin(), arr.end());
}

// void sortDecreasing(vector<double> & arr) {
//   sortIncreasing(arr); // not done yet
// }

int getNormalScore(vector<double> & naobricks, vector<double> & kenbricks, int naoid, int kenid) {
  //cout << "before while naoid: " << naoid << " kenid: " << kenid << endl;
  if (naoid >= kenbricks.size()) return 0;
 // cout << "before while" << endl;
  while (kenid < kenbricks.size() && naobricks[naoid] > kenbricks[kenid]) kenid++;
 // cout << "After while" << endl;
  //cout << "after while - naoid: " << naoid << " kenid: " << kenid << endl;
  if (kenid >= kenbricks.size()) return kenbricks.size() - naoid;
  else {
   // cout << "recurssing on naoid: " << naoid + 1 << " kenid: " << kenid + 1 << endl;
    return getNormalScore(naobricks, kenbricks, ++naoid, ++kenid);
  }
}

int getDeceitScore(vector<double> & naobricks, vector<double> & kenbricks, int naoid, int kenid) {
  if (naoid >= naobricks.size()) return 0;
  if (naobricks[naoid] < kenbricks[kenid]) {
    //kenbricks.pop_back();
    return getDeceitScore(naobricks, kenbricks, ++naoid, kenid);
  }
  return 1 + getDeceitScore(naobricks, kenbricks, ++naoid, ++kenid);
}

void solveProblem(ofstream & resultfile) {
  sortIncreasing(naobricks);
  sortIncreasing(kenbricks);
 // cout << "sort finishes" << endl;
  int normwar = getNormalScore(naobricks, kenbricks, 0, 0);
  // cout << "norm finishes" << endl;
  int dctwar = getDeceitScore(naobricks, kenbricks, 0, 0);   
  // cout << "deceit finishes" << endl;
  
  resultfile << "Case #" << currentCase << ":";
  resultfile << " " << dctwar << " " << normwar;
  resultfile << endl;
  // cout << "Case #" << currentCase << ":";
  // cout << " " << dctwar << " " << normwar;
  // cout << endl;
}

int main () {
  ofstream resultfile;
  ifstream inputfile;
  inputfile.open ("input.in");
  resultfile.open ("result.txt");
  
  string line;
  int linenum = 0; // Line number starting from 1
  getline (inputfile, line);
  while ( getline (inputfile, line)) {
    linenum++;
    if (linenum == 1) {
      numbricks = atoi(line.c_str());
      continue;
    }
    if (linenum == 2) {
      naobricks = stringArrToDoubleArr(split(line, " "));
      continue;
    }
    if (linenum == 3) {
      kenbricks = stringArrToDoubleArr(split(line, " "));
      linenum = 0;

      currentCase++; 
      solveProblem(resultfile);
      continue;
    }
  }
  inputfile.close();
  resultfile.close();
  return 0;
}
