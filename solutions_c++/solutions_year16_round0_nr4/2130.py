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
      unsigned K = 0;
      unsigned C = 0;
      unsigned S = 0;

      cin >> K;
      cin >> C;
      cin >> S;

      cout << "Case #" << t + 1 << ":";
      if (K != S) {
         cout << " UNKNOWN";
      } else {
         for (unsigned i = 0; i < K; ++i) {
            cout << ' ' << i+1;
         }
      }

      cout << endl;
   }

   return 0;
}

