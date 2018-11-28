#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <cmath>
#include <limits>
#include <vector>
#include <gmpxx.h>
using namespace std;

#define print(x) cout << #x " = " << x << endl;

int numberOfCases(ifstream &infile);
int readCaseFromStream(ifstream &infile, mpz_class &r, mpz_class &t);

int main ( int argc, char* argv[] ) {
  if ( argc < 2 ) { 
    cerr << "Usage: main <file.in>" << endl;  
    return EXIT_FAILURE; 
  }
  ifstream infile; infile.open(argv[1]);
  
  int numCases = numberOfCases(infile);
  for ( int k = 0; k < numCases; ++k ) {
    mpz_class r, t;
    int count = 0;
    
    readCaseFromStream(infile, r, t);   
    
    mpz_class base_usage = 2*r+1, alpha = 0;
    while ( t > 0 ) {      
      mpz_class ring = base_usage + 2*alpha;            
      t -= ring;       
      if ( t >= 0 ) count++;
      
      alpha = alpha + 2;
    }

    cout << "Case #" << k+1 << ": ";   
    cout << count;
    cout << endl;   
  }
  
  infile.close();
  return 0;
}

int readCaseFromStream(ifstream &infile, mpz_class &r, mpz_class &t) {
  if ( infile ) {
    string s;
    getline(infile, s);
    unsigned pos = s.find(" ");
    r = s.substr(0,pos); 
    t = s.substr(pos);    
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
