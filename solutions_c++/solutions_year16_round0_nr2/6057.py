#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream in("data.in");
ofstream out("data.out");

string flip(string s) {
  string z = "";
  for (int i=s.size()-1; i>=0; i--) {
    if (s[i] == '+') {
      z += '-';
    } else {
      z += '+';
    }
  }
  return z;
}

string opposite(string s) {
  string z = "";
  for (int i=0; i<s.size(); i++) {
    if (s[i] == '+') {
      z += '-';
    } else {
      z += '+';
    }
  }
  return z;
}

int compute(string s) {
  if (s == "") {
    return 0;
  }
  if (s[s.size()-1] == '+') {
    return compute(s.substr(0,s.size()-1));
  }

  if (s[0] == '-') {
    s = flip(s);
    return 1 + compute(s.substr(0,s.size()-1));
  }
  
  return 1 + compute(opposite(s.substr(0,s.size()-1)));
}

int main() {
  int t;
  in >> t;
  for (int caseNum = 1; caseNum <= t; caseNum++) {
    string s;
    in >> s;
    
    out << "Case #" << caseNum << ": " << compute(s) << endl;
  }
}
