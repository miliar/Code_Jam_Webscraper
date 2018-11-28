#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    double cc, f, x;
    cin >> cc >> f >> x;
    double tm = 0, r = 2;
    while (x/r > cc/r+x/(r+f)) {
      tm += cc/r;
      r += f;
    }
    tm += x/r;

    cout << "Case #" << c << ": " << setprecision(8) << fixed << tm << endl;
  }
}
