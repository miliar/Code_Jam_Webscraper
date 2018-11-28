#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <cmath>
#include <limits>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

#define print(x) cout << #x " = " << x << endl;

int numberOfCases(ifstream &infile);
void readCaseFromStream(ifstream &infile, string &s, int &n);
bool isAllConsonants(string s);

int main ( int argc, char* argv[] ) {
  if ( argc < 2 ) { 
    cerr << "Usage: main <file.in>" << endl;  
    return EXIT_FAILURE; 
  }
  ifstream infile; infile.open(argv[1]);

  int numCases = numberOfCases(infile);
  for ( int k = 0; k < numCases; ++k ) {
    string s; int n;
    readCaseFromStream(infile, s, n);
    int len = s.size(), len_ = len - n + 1;
    vector<vector<int> > M(len_);
    for ( int i = 0; i < len_; ++i ) { M[i].resize(len_, 0); }
    
    int count = 0;
    for ( int i = 0; i < len_; ++i ) {
      string s_ = s.substr(i, n);
      if ( isAllConsonants(s_) ) M[i][i] = ++count;            
    }

    for ( int i = 1; i < len_; ++i ) {
      for ( int j = i; j < len_; ++j ) {
	int i_ = j-i, j_ = j;
	if ( M[i_+1][j_] || M[i_][j_-1] ) M[j-i][j] = ++count;
      }
    }
    
    cout << "Case #" << k+1 << ": ";   
    cout << count;
    cout << endl;   
  }
  infile.close();
  return 0;
}

bool isAllConsonants(string s) {
  const char *str = s.c_str();
  for (int i = 0; i < s.size(); ++i ) {
    if ( (str[i] == 'a') ||
	 (str[i] == 'e') ||
	 (str[i] == 'i') ||
	 (str[i] == 'o') ||
	 (str[i] == 'u') ) 
      return false;
  }
  return true;
}

void readCaseFromStream(ifstream &infile, string &s, int &n) {
  if ( infile ) {
    string str;
    getline(infile, str);
    unsigned pos = str.find(" ");
    s = str.substr(0, pos);
    n = atoi(str.substr(pos).c_str());
  }
}

int numberOfCases(ifstream &infile) {
  if ( infile ) {
    string s;
    if ( getline(infile, s) ) {
      return atoi(s.c_str());
    } 
    return 0;  
  } 
  return 0;
}
