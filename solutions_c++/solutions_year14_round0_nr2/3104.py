#include <iostream>
#include <cmath>
#include <cassert>

using namespace std;

typedef unsigned long long ull;
typedef long double ld;

//ld resolve(ld C, ld F, ld X) {
//#ifdef DEBUG
//  cout << "----------------------------------" << endl;
//  cout << "C\tF\tX" << endl;
//  cout << C << "\t" << F << "\t" << X << endl;
//#endif
//  ld s = 0;
//  ld x = 1.0L / 2;
//  ld last = X / 2;
//  ull n = 1;
//  while (true) {
//    s += x;
//    x = 1 / (2 + n * F);
//    ld t = C * s + X * x;
//#ifdef DEBUG
//    cout << "n: " << n << endl;;
//    cout << "s: " << s << endl;;
//    cout << "x: " << x << endl;;
//#endif
//    if (abs(last - t) < 0.000001 || last < t)
//      break;
//    last = t;
//    n++;
//  }
//  return last;
//}

ld resolve(ld C, ld F, ld X) {
  ld s = 0;
  ld x = 1.0L / 2;
  ld m = X / 2;
  ull n = 1;
  while (n <= 100000) {
    s += x;
    x = 1 / (2 + n * F);
    ld t = C * s + X * x;
    if (!(abs(m - t) < 0.000001 || m < t))
      m = t;
    n++;
  }
  return m;
}

int main() {
  cout.precision(7);
  cout << fixed;
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    ld C, F, X;
    cin >> C >> F >> X;
    cout << "Case #" << t + 1 << ": " << resolve(C, F, X) << endl;
  }
  return 0;
}

