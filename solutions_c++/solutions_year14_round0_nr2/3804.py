#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
using namespace std;


int main(int, char**) {
   unsigned T = 0;
   cin >> T;

   for (unsigned t = 0; t < T; ++t) {
      double result = 0;
      double C, F, X;
      double inc = 2.0;

      cin >> C;
      cin >> F;
      cin >> X;

      while ((X - C) * (inc + F) > inc * X) {
         result += C / inc;
         inc += F;
      }
      result += X / inc;

      cout << "Case #" << t + 1 << ": " << fixed << setprecision(7) << result << endl;
   }

   return 0;
}

