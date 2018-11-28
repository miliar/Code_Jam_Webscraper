#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    double C,F,X;
    cin >> C >> F >> X;
    double v = 2;
    double t = 0;
    while (1) {
      if (X < C) {
        t += X / v;
        break;
      }
      t += C / v;
      if ((X - C) / v < X / (v + F)) {
        t += (X - C) / v;
        break;
      } else {
        v += F;
      }
    }
    cout << "Case #" << i + 1 << ": " << setprecision(10) << t << endl;
  }
}
