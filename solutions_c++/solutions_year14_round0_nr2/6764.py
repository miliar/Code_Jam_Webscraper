#include <iostream>
#include <limits>

using namespace std;

int main() {
  int T;
  cin >> T;
  cout.precision(numeric_limits<double>::digits10);
  for (int t = 0; t < T; ++t) {
    double C, F, X;
    cin >> C >> F >> X;
    double rate = 2.0;
    double time = 0.0;
    double total = 0.0;
    while ((total + X/rate)>(total + C / rate + X/(rate + F))) {
      total += C / rate;
      rate += F;
    }
    total += X/rate;
    cout << "Case #" << t+1 << ": " << total << endl;
  }
}
