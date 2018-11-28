#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;


unsigned run(unsigned n) {
   unsigned num = 10;
   bool has[10] = { 0 };

   if (n == 0) return n;

   unsigned i = 1;
   for (; num > 0; ++i) {
      unsigned tmp = n * i;

      for (; tmp > 0; tmp /=10) {
         unsigned r = tmp % 10;
         if (!has[r]) {
            has[r] = true;
            --num;
         }
         if (num == 0) break;
      }
   }

   return n * (i - 1);
}


int main(int, char**) {
   unsigned T = 0;
   cin >> T;

   for (unsigned t = 0; t < T; ++t) {
      unsigned n = 0;
      cin >> n;
      unsigned result = run(n);

      cout << "Case #" << t + 1 << ": ";
      if (result != 0) {
         cout << result;
      } else {
         cout << "INSOMNIA";
      }
      cout << endl;
   }

   return 0;
}

