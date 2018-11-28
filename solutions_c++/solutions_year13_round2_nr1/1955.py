#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <cmath>
#include <limits>
#include <vector>
#include <gmpxx.h>
#include <sstream>
#include <algorithm>
using namespace std;

#define print(x) cout << #x " = " << x << endl;

int numberOfCases(ifstream &infile);
int readCaseFromStream(ifstream &infile, mpz_class &A, vector<long> &motes);

int main ( int argc, char* argv[] ) {
  if ( argc < 2 ) { 
    cerr << "Usage: main <file.in>" << endl;  
    return EXIT_FAILURE; 
  }
  ifstream infile; infile.open(argv[1]);
  
  int numCases = numberOfCases(infile);
  for ( int k = 0; k < numCases; ++k ) {
    mpz_class A;
    vector<long> motes;
    int count = 0;
    vector<int> stopping;
    
    readCaseFromStream(infile, A, motes);   
    sort(motes.begin(), motes.end());

    int j = 0;      
    bool impossible = false;
    while ( (A > motes[j]) && (j < motes.size()) ) {
      A += motes[j++];
    }
    while ( j < motes.size() ) {   
      if ( A <= motes[j] ) {
	stopping.push_back((motes.size() - j) + count); // remove the rest of the motes
	if ( (A-1) == 0 ) {
	  impossible = true;
	  break;
	} else {
	  A += (A-1);
	  count++;
	}
      } else {
	A += motes[j++];
      }      
    }
    if ( !impossible ) stopping.push_back(count);
    sort(stopping.begin(), stopping.end());
    
    cout << "Case #" << k+1 << ": ";   
    cout << stopping[0];
    cout << endl;   
  }
  
  infile.close();
  return 0;
}

int readCaseFromStream(ifstream &infile, mpz_class &A, vector<long> &motes) {
  if ( infile ) {
    string s;
    getline(infile, s);
    unsigned pos = s.find(" ");
    A = atoi(s.substr(0,pos).c_str());
    string token, s1;
    getline(infile, s1);
    istringstream ss(s1);
    long x;
    while ( getline(ss, token, ' ') ) {      
      x = atoi(token.c_str());
      motes.push_back(x);
    }
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
