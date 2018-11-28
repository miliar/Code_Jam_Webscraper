#include <iostream>
using namespace std;

int main() {
  cout.setf(ios::fixed);
  cout.precision(7);
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    cout << "Case #" << cas << ": ";
    double C, F, X;
    cin >> C >> F >> X;
    double t = 0;
    int f = 0;
    while (C/(2 + f*F) + X/(2 + (f+1)*F) < X/(2 + f*F)) {
      t += C/(2 + f*F);
      ++f;
    }
    t += X/(2 + f*F);
    cout << t << endl;
  }
}