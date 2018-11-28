#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cassert>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;


struct test_case_t {
  long long r;
  long long t;

  static test_case_t read( istream & infile ) {
    string line;
    struct test_case_t one;
    getline(infile,line);
    sscanf(line.c_str(), "%ld %ld", &(one.r), &(one.t));
    return one;
  }
  
  long long solve() {    
    long long n;
    long long r1 = r;
    long long fin =0;
    for( n=0;fin<=t;n++) {      
      fin += 2*r1+1;
      r1 += 2;
    }
    printf( "   t: %ld, fin: %ld, n: %ld\n", t, fin, n );
    return n-1;
  }
};

int main(int argc, char ** argv ) {
    if( argc != 2 ) {
    cerr << "Pass in the input filename (" << argc << " args)" << endl;
    return ( -1 );
  }
  ifstream infile(argv[1]);
  string outname(argv[1]);
  ofstream outfile((outname + string(".out")).c_str());
  string line;
  getline(infile,line);
  int test_count;
  sscanf( line.c_str(), "%d", &test_count );
  for( int test=1;test<=test_count;test++) {
    printf("reading %d test of %d\n", test,test_count );
    test_case_t tc = test_case_t::read(infile);
    outfile << "Case #" << test << ": " << tc.solve() << endl;
  }
  outfile.close();
}
