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
      string result = "RICHARD";

      // read inputs
      unsigned X, R, C;
      cin >> X >> R >> C;
///
//cout << "X = " << X << ", R = " << R << ", C = " << C << endl;

      // run test
      if (R > C) {
         unsigned T = R;
         R = C;
         C = T;
      }
      switch (X) {
         case 1:
            result = "GABRIEL";
            break;

         case 2:
            if (!(R*C & 1)) {
               result = "GABRIEL";
            }
            break;

         case 3:
            if ((R == 2 && C ==3) ||
                (R == 3 && C ==3) ||
                (R == 3 && C ==4)) {
               result = "GABRIEL";
            }
            break;

         case 4:
            if ((R == 3 && C ==4) ||
                (R == 4 && C ==4)) {
               result = "GABRIEL";
            }
            break;

         default:
            break;
      };

      cout << "Case #" << t + 1 << ": " << result << endl;
   }

   return 0;
}

