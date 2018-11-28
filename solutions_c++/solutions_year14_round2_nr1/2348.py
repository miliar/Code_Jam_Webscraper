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

int a[105][105];


int main() {

  ifstream fi;		// input file
  ofstream fo;		// output file
  int numCases;	    // number of cases

  fi.open("input.txt");
  fo.open("output.txt");


  fi >> numCases;

  for (int cases=1; cases<=numCases; ++cases) {
    // -----------------------------------------------------------------------------
    for (int i = 0; i < 105; ++i)
        for (int j = 0; j < 105; ++j)
            a[i][j] = 0;

    int result = 0;
    bool felga = false;
    int N;
    fi >> N;

    std::string original;
    for (int i = 0; i < N; ++i) {
        std::string str, str2;
        fi >> str2;
        str = str2;
        auto it = unique(str.begin(), str.end());
        str.resize(it - str.begin());

        if (i == 0) {
            original = str;
        } else {
            if (str != original) {
                felga = true;
                break;
            }
        }
        int j = 0;
        for (int k = 0; k < str2.size(); ++k)  {
            if (str2[k] != original[j])
                j++;
            a[j][i]++;
        }
    }

    if (!felga) {
        for (int i = 0; i < original.size(); ++i) {
            int min = 1000000000;

            for (int j = 1; j < 105; ++j) {
                int current = 0;
                for (int k = 0; k < N; ++k) {
                    current += abs(a[i][k] - j);
                    if (current > min)
                        break;
                }
                if (current < min)
                    min = current;
            }
            result += min;
        }
    }

    // ------------------------------------------------------------------------------
    fo << "Case #" << cases << ": ";
    if (felga)
        fo << "Fegla Won";
    else
        fo << result;
    fo << endl;
  }

  fi.close();
  fo.close();
  return 0;
}


