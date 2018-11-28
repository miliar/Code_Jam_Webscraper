#include <iostream>
#include <iomanip>

using namespace std;


int main()
{
  int T;

  cin >> T;

  for (int cas = 1; cas <= T; cas++) {
    double C, F, X;
    cin >> C >> F >> X;

    double t = 0;
    double c = 0;
    double r = 2.0;

    while (c < X) {
      double tfarm = c >= C ? 0 : (C - c) / r;
      double tend = (X - c) / r;

      double c2 = c + tfarm * r - C;
      double tend2 = c2 >= X ? 0 : (X - c2) / (r + F);

      if (tfarm + tend2 < tend) {
        c = c2;
        t += tfarm;
        r += F;
      } else {
        c = X;
        t += tend;
      }
    }

    cout << "Case #" << cas << ": " << fixed << setprecision(10) << t << endl;
  }

  return 0;
}
