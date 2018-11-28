#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <math.h>

using namespace std;

bool solve(int X, int R, int C) {
  if (X >= 7) return false;
  if (R*C % X != 0) return false;
  if ((X+1) / 2 > R || (X+1) / 2 > C) return false;
  if (X == 4) {
    if (C <= 2 || R <= 2) return false;
  }
  if (X == 5) {
    if (C <= 3 || R <= 3) return false;
  }
  if (X == 6) {
    if (C <= 3 || R <= 3) return false;
  }
  if (X > R && X > C) return false;
  return true;
}

int main() {
  int T = 0;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int X, R, C;
    cin >> X >> R >> C;
    bool res = solve(X, R, C);
    cout << "Case #" << i << ": ";
    // cout << X << " " << R << " " << C << " ";
    if (res) {
      cout << "GABRIEL";
    } else {
      cout << "RICHARD";
    }
    cout << endl;
  }
}
