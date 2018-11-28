#include <iostream>

using namespace std;

bool solve(int X, int R, int C) {
   int L = (R > C) ? R : C;
   int W = (R > C) ? C : R;
   if (L < X) return false;
   if ((R * C) % X) return false;
   if (X == 1) return true;
   else if (X == 2) return W >= 1;
   else if (X == 3) return W >= 2;
   else if (X == 4 || X == 5) return W >= 3;
   else if (X == 6) return W >= 4;
   else return false;
}

int main() {
   // parse T
   int T; cin >> T; if (T <= 0) return 0;
   // parse X, R, C
   for (int i = 0; i < T; ++i) {
      int X, R, C; cin >> X >> R >> C;
      bool result = solve(X, R, C);
      cout << "Case #" << (1 + i) << ": " << (result ? "GABRIEL" : "RICHARD") << endl;
   }
   return 0;
}

