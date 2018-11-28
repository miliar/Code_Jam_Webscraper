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
    int F, D;
    fi >> F >> D;
    vector<int> f(F);
    for (int i = 0; i < F; ++i)
        fi >> f[i];
    sort(f.begin(), f.end());
    int result = 0;
    int pairs = 0;
    for (int i = 0; i < f.size(); ++i) {
        auto it = f.begin() + i;
        auto it2 = upper_bound(f.begin(), f.end(), D - f[i]);
        if (it2 - it > 1) {
            it2--;
            f.erase(it2);
            f.erase(it);
            ++pairs;
            --i;
        }
    }
    
    result = f.size() + pairs;

    // ------------------------------------------------------------------------------
    fo << "Case #" << cases << ": ";
    fo << result;  // TODO
    fo << endl;
  }

  fi.close();
  fo.close();
  return 0;
}


