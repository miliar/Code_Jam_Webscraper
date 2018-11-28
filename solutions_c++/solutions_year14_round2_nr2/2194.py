/*
 * Tibor Mezei (zemei)
 * Google Code Jam 2014
 * Standard: C++11 with GCC-4.8.2
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
#include <ios>
#include <iomanip>
#include <fstream>
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


int main() {

  ifstream fi;		// input file
  ofstream fo;		// output file
  int numCases;	    // number of cases

  fi.open("input.txt");
  fo.open("output.txt");


  fi >> numCases;

  for (int cases=1; cases<=numCases; ++cases) {
    // -----------------------------------------------------------------------------
    int A, B, K;
    fi >> A >> B >> K;
    int result = 0;
    for (int i = 0; i < A; ++i) {
        for (int j = 0; j < B; ++j) {
            if ((i&j) < K)
                ++result;
        }
    }
    // ------------------------------------------------------------------------------
    fo << "Case #" << cases << ": ";
    fo << result;
    fo << endl;
  }

  fi.close();
  fo.close();
  return 0;
}


