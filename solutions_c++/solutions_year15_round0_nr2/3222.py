#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(int eatTurns, vector<int> pn) {
   int flips = 0;
   for (int i = pn.size()-1; i > eatTurns; --i) {
      int f = pn[i];
      if (!f) continue;
      int fpp = (i - 1) / eatTurns;
      flips += fpp * f;
   }
   return flips + eatTurns;
}
string doCase() {
   int D;
   cin >> D;
   vector<int> p(D);
   vector<int> pn(1001);
   for (int i = 0; i < D; ++i) {
      cin >> p[i];
      pn[p[i]]++;
   }
   int best = -1;
   for (int et = 1; et < 1001; ++et) {
      int c = solve(et, pn);
      if (c < best || best < 0) best = c;
   }
   stringstream ss2; ss2 << best;
   return ss2.str();
}
int main() {
   int cases;
   cin >> cases;
   cin.ignore();
   for (int c = 0; c < cases; ++c) {
      cout << "Case #" << c + 1 << ": " << doCase() << '\n';
   }
   return 0;
}