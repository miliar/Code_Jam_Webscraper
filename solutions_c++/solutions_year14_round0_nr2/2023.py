//Joe Snider
//4/14
//
//Codejam 2014 qual prob 2
// pipe input output (cat input.txt | ./a.out > output.txt)

#include <iostream>
#include <vector>
#include <set>

using namespace std;

//recurse the number of cookies (stop when new t is more, only gets worse)
double cook(double C, double F, double X, double m, double b, double t) {
   double newM = m+F;
   double newB = newM/m*(b-C);
   double newT = (X-newB)/newM;
   if (newT > t) {
      return t;
   } else {
      return cook(C, F, X, newM, newB, newT);
   }
}

int main() {
   int T;
   double C, F, X;
   cin >> T;
   for(int t = 1; t <= T; ++t) {
      cin >> C >> F >> X;
      cout.precision(10);
      cout << "Case #" << t << ": " << cook(C, F, X, 2.0, 0., X/2.0) << "\n" << flush;
   }
}
