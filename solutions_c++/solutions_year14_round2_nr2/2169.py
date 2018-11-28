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

      unsigned A;
      unsigned B;
      unsigned K;

      cin >> A;
      cin >> B;
      cin >> K;

      for (unsigned i = 0; i < A; ++i) {
         for (unsigned j = 0;j < B; ++j) {
            if ((i & j) < K) {
               ++result;
            }
         }
      }
      cout << "Case #" << t + 1 << ": " << result << endl;
   }

   return 0;
}

