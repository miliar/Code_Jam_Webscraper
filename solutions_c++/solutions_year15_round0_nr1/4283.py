#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;


int main(int, char**) {
   unsigned T = 0;
   cin >> T;

   for (unsigned t = 0; t < T; ++t) {
      unsigned result = 0;

      // Read inputs
      unsigned sMax = 0;
      cin >> sMax;
///
//cout << "sMax = " << sMax << endl;

      vector<unsigned> s(sMax + 1);
      for (unsigned i = 0; i <= sMax; ++i) {
         char c = 0;
         cin >> c;
         c -= '0';
///
//cout << "c = " << unsigned(c) << endl;
         s[i] = c;
      }

      // run test
      unsigned has = s[0];
      for (unsigned i = 1; i <= sMax; ++i) {
         if (has < i) {
            result += i - has;
            has += i - has;
         }
         has += s[i];
      }

      cout << "Case #" << t + 1 << ": " << result << endl;
   }

   return 0;
}

