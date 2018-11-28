/*
 * Tibor Mezei (zemei)
 * Google Code Jam 2015
 * Standard: C++14 with GCC-4.9.2
*/

#include <deque>
#include <list>
#include <tuple>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

#include <algorithm>
#include <complex>
#include <iostream>
#include <fstream>
#include <ios>
#include <iomanip>
#include <regex>
#include <string>

#include <cctype>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


// Prime number tester
bool isPrime(uint64_t x) {
  if (x<2) return false;
  for (uint64_t i=2; i*i<=x; ++i)
    if (x%i==0) return false;
  return true;
}


int main(int argc, char **argv) {

  ifstream fi;		// input file
  ofstream fo;		// output file
  int numCases;	    // number of cases

  if (argc!=2) { 
    printf("No input!\n"); 
    return -1; 
  }

  fi.open(argv[1]);
  fo.open("output.txt");


  fi >> numCases;

  for (int cases=1; cases<=numCases; ++cases) {
    // -----------------------------------------------------------------------------
    int N;
    string str;
    fi >> N >> str;
    int friends = 0, ovation = 0;
    for (int i = 0; i <= N; ++i) {
        friends += (ovation + friends) < i ? 1 : 0;
        ovation += str[i] - '0';
    }
    // ------------------------------------------------------------------------------
    fo << "Case #" << cases << ": ";
    fo << friends;  // TODO
    fo << endl;
  }

  fi.close();
  fo.close();
  return 0;
}


