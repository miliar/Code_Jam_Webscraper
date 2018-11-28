#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

const int NO_WAY_TO_CHOOSE = 1;
const int HAVE_WAY_TO_CHOOSE = 0;
const string RESULT[2] = { "RICHARD", "GABRIEL" };

int main() {
  freopen("d.inp", "r", stdin);
  freopen("d.out", "w", stdout);

  int nTest;
  scanf("%d", &nTest);

  for (int test = 1; test <= nTest; test++) {
    int x, r, c;
    int result;
    scanf("%d %d %d", &x, &r, &c);
    if (x == 1) {
      result = NO_WAY_TO_CHOOSE; // right
      goto exits;
    }

    if (r * c % x != 0) {
      result = HAVE_WAY_TO_CHOOSE; // right
      goto exits;
    }

    if (x == 2) {
      result = NO_WAY_TO_CHOOSE; // right
    }

    if (x == 3) {
      if (r * c == 3) result = HAVE_WAY_TO_CHOOSE; //
      if (r * c == 6) result = NO_WAY_TO_CHOOSE; //
      if (r * c == 9) result = NO_WAY_TO_CHOOSE; //
      if (r * c == 12) result = NO_WAY_TO_CHOOSE; //
    }

    if (x == 4) {
      if (r * c == 4) result = HAVE_WAY_TO_CHOOSE; //
      if (r * c == 8) result = HAVE_WAY_TO_CHOOSE; //
      if (r * c == 12) result = NO_WAY_TO_CHOOSE;
      if (r * c == 16) result = NO_WAY_TO_CHOOSE;
    }

    exits:
    cout << "Case #" << test << ": " << RESULT[result] << endl;
  }

  return 0;
}
