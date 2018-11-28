#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cstring>
using namespace std;

void solve(int test) {
  double C, F, X;
  cin >> C >> F >> X;
  double currentSpeed = 2.0;
  double currentTime = 0.0;
  double best = X / currentSpeed;

  while (currentTime < best) {
    currentTime += C / currentSpeed;
    currentSpeed += F;
    double cand = currentTime + X / currentSpeed;
    if (cand < best) {
      best = cand;
    }
  }

  cout.setf(ios::fixed);
  cout.precision(7);
  cout << "Case #" << test << ": " << best << "\n";
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
      solve(test);
    }
    return 0;
}
