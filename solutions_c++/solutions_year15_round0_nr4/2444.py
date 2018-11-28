#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

int main() {
  int T;
  int c = 1;
  cin >> T;
  while (T--) {
    int X, R, C;
    bool gabriel = false;
    cin >> X >> R >> C;

    if (R > C) swap(R, C);

    switch (X) {
    case 1: // (0,16) cases
      gabriel = true;
      break;
    case 2:  // (8, 8) cases
      gabriel = (R*C) % 2 == 0;
      break;
    case 3:
      if (R*C % 3 != 0) break;
      if (R == 1 || C == 1) break;
      gabriel = true;
      break;
    case 4:
      if (R*C % 4 != 0) break;
      if (R <= 2) break;
      gabriel = true;
      break;
    }

    cout << "Case #" << c++ << ": ";
    if (gabriel) {
      cout << "GABRIEL";
    }
    else {
      cout << "RICHARD";
    }
    cout << endl;
  }

  return 0;

}