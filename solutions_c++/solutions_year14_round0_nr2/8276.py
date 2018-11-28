#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;

int main() {
  int T;
  long double C, F, X, rate, t, Xt, Ct;
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> C >> F >> X;
    rate = 2.0;
    t = 0;
    Xt = X / rate;
    Ct = C / rate + X / (rate + F);
    while (Xt > Ct) {
      t += C / rate;
      rate += F;
      Xt = X / rate;
      Ct = C / rate + X / (rate + F);
    }
    t += Xt;
    cout << "Case #" << i << ": ";
    fprintf(stdout, "%.8llf\n", t);
  }
  return 0;
}