#include <iostream>
#include <cmath>
using namespace std;

int main() {
  cout.setf(ios::fixed);
  cout.precision(7);
  int T; cin >> T;
  for (int x = 1; x <= T; ++x) {
    double C, F, X; cin >> C >> F >> X;
    double n = max(0., ceil(X/C - 2./F - 1.)); //optimal number of farms
    double y = 0;
    for (int i = 0; i < n-0.1; ++i) y += C/(2. + i*F);
    y += X/(2. + n*F);
    cout << "Case #" << x << ": " << y << endl;
  }
}
