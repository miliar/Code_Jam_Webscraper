#include <iostream>
#include <cstring>
using namespace std;

static const char* results[2] = {
   "NO",
   "YES"
};


int main(int, char**) {
   unsigned T = 0;
   cin >> T;

   char h[100][100];
   char rowMax[100];
   char colMax[100];

   for (unsigned t = 0; t < T; ++t) {
      unsigned result = 1;
      unsigned N = 0;
      unsigned M = 0;
      char v = 0;

      memset(h, 0, 10000);
      memset(rowMax, 0, 100);
      memset(colMax, 0, 100);

      cin >> N >> M;
      for (unsigned n = 0; n < N; ++n) {
         for (unsigned m = 0; m < M; ++m) {
            cin >> v;
            h[n][m] = v;
            if (v > rowMax[n]) {
               rowMax[n] = v;
            }
            if (v > colMax[m]) {
               colMax[m] = v;
            }
         }
      }

      if (N < 2 || M < 2) {
         cout << "Case #" << t + 1 << ": " << results[result] << endl;
         continue;
      }

      for (unsigned n = 0; n < N; ++n) {
         for (unsigned m = 0; m < M; ++m) {
            v = h[n][m];
            if (rowMax[n] > v && colMax[m] > v) {
               result = 0;
               goto done;
            }
         }
      }

      done:
      cout << "Case #" << t + 1 << ": " << results[result] << endl;
   }

   return 0;
}

