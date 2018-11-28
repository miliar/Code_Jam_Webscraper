#include <iostream>
using namespace std;

const unsigned p[5] = {1, 4, 9, 121, 484};


int main(int, char**) {
   unsigned T = 0;
   cin >> T;

   for (unsigned t = 0; t < T; ++t) {
      unsigned result = 0;
      unsigned A = 0;
      unsigned B = 0;
      unsigned belowA = 0;
      unsigned belowB = 0;

      cin >> A >> B;
      for (unsigned i = 0; i < 5; ++i) {
         if (A > p[i]) {
            ++belowA;
         }
         if (B >= p[i]) {
            ++belowB;
         }
      }

      result = belowB - belowA;

      cout << "Case #" << t + 1 << ": " << result << endl;
   }

   return 0;
}

