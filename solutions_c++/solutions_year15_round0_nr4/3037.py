#include<bits/stdtr1c++.h>
using namespace std;

int main () {
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    int X, R, C; cin >> X >> R >> C;
    bool good = (R * C) % X == 0;
    if (R + C <= X) good = false;
    if (X >= 3 && min(R, C) <= 1) good = false;
    if (X == 4 && min(R, C) == 2) good = false;
    cout << "Case #" << t << ": " << ((good)? "GABRIEL" : "RICHARD") << endl;
  }
  return 0;
}
