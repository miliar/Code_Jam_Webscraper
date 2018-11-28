#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <sstream>
#include <cmath>
#include <limits>
#include <vector>
using namespace std;

#define print(x) cout << #x " = " << x << endl;

int numberOfCases(ifstream &infile);
int readCaseFromStream(ifstream &infile, unsigned int &begin, unsigned int &end);
bool isPalindrome(unsigned int i);

int main ( int argc, char* argv[] ) {
  if ( argc < 2 ) { 
    cerr << "Usage: main <file.in>" << endl;  
    return EXIT_FAILURE; 
  }
  ifstream infile; infile.open(argv[1]);
  
  int numCases = numberOfCases(infile);
  unsigned int begin = 0, end = 0;

  for ( int k = 0; k < numCases; ++k ) {
    readCaseFromStream(infile, begin, end);    
    int count = 0;
    cout << "Case #" << k+1 << ": ";
    for ( unsigned int i = begin; i <= end; ++i ) {
      //      print(i);
      if ( isPalindrome(i) && isPalindrome(i*i) ) count++;     
    }
    cout << count << endl;
  }


  infile.close();
  return 0;
}

bool isPalindrome(unsigned int i) {
  stringstream ss; ss << i;
  string num = ss.str();
  int n = floor(num.length()/2);      
  if ( n == 0 ) {
    return true;
  } else {
    bool same = true;
    int j = 0;
    while ( (j < n) && same ) {
      if ( num[j] == num[num.length()-j-1] ) {
	++j;
      } else {
	same = false;
      }
    }
    return same;
  }
}

int readCaseFromStream(ifstream &infile, unsigned int &begin, unsigned int &end) { 
  if ( infile ) {
    string s;
    getline(infile, s);
    unsigned pos = s.find(" ");
    begin = ceil(sqrt(atoi(s.substr(0, pos).c_str())));
    end = floor(sqrt(atoi(s.substr(pos).c_str())));
    return 1;
  }     
  return 0;
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
