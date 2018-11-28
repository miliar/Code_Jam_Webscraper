#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;


int main(int, char**) {
   unsigned T = 0;
   cin >> T;

   for (unsigned t = 0; t < T; ++t) {
      unsigned result = 0;
      unsigned flags[17] = { 0 };

      unsigned first;
      cin >> first;

      for (unsigned i = 0; i < 4; ++i) {
         unsigned c1, c2, c3, c4;
         cin >> c1;
         cin >> c2;
         cin >> c3;
         cin >> c4;
         if (i == (first - 1)) {
            flags[c1] = 1;
            flags[c2] = 1;
            flags[c3] = 1;
            flags[c4] = 1;
         }
      }

      unsigned second;
      cin >> second;

      for (unsigned i = 0; i < 4; ++i) {
         unsigned c1, c2, c3, c4;
         cin >> c1;
         cin >> c2;
         cin >> c3;
         cin >> c4;
         if (i == (second - 1)) {
            if (flags[c1]) {
               flags[0]++;
               result = c1;
            }
            if (flags[c2]) {
               flags[0]++;
               result = c2;
            }
            if (flags[c3]) {
               flags[0]++;
               result = c3;
            }
            if (flags[c4]) {
               flags[0]++;
               result = c4;
            }
         }
      }

      string resultString;
      if (flags[0] == 0) {
         resultString = "Volunteer cheated!";
      } else if (flags[0] > 1) {
         resultString = "Bad magician!";
      } else {
         resultString = to_string(result);
      }
      cout << "Case #" << t + 1 << ": "<< resultString << endl;
   }

   return 0;
}

