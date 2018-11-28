#include <iostream>
using namespace std;

bool count(int, int, int);

int main() {
  int T;
  cin >> T;

  for (int k = 1; k<=T; ++k) {
    int X, R, C, tmp;
    bool flag = false;
    cin >> X >> R >> C;

    if (R > C) {
      tmp = R;
      R = C;
      C = tmp;
    }
    flag = count(X, R, C);
    if (flag) {
      cout << "Case #" << k << ": GABRIEL" << endl;
    } else {
      cout << "Case #" << k << ": RICHARD" << endl;
    }
  }
  return 0;
}

bool count(int X, int R, int C) {
  if (X == 1)
    return true;
  if (X == 2) {
    if (C < 2 || (R%2 !=0 && C%2 != 0 )) { 
      return false;
    }
    return true;
  }
  if (X == 3) {
    if (R < 2 || C < 3 || (R==4 && C==4) || (R==2 && C==4)) {
      return false;
    }
    return true;
  }
  if (X == 4) {
    if (R < 3 || C < 4 ) {
      return false;
    }
    return true;
  }
  return false;
}
