#include <cstdlib>
#include <string>
#include <iostream>
#include <set>

using namespace std;

int main() {
  // Number of cases.
  int N;
  cin >> N;

  // For each test case.
  for (int i=1; i<=N; i++) {

    int X, R, C;
    cin >> X >> R >> C;

    int surface = R*C;

    if (surface%X != 0)
      cout << "Case #" << i << ": RICHARD" << endl;
    else if (X <= 2)
      cout << "Case #" << i << ": GABRIEL" << endl;
    else if (R < 2 || C < 2)
      cout << "Case #" << i << ": RICHARD" << endl;
    else if ((R == 2 || C == 2) && X == 4)
      cout << "Case #" << i << ": RICHARD" << endl;
    else
      cout << "Case #" << i << ": GABRIEL" << endl;

  }

  return 0;
}