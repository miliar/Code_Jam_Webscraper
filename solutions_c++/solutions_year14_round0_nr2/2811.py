#include <iostream>
using namespace std;

const double eps = 1e-9;

int main() {
  cout.precision(7);
  int T; cin >> T;
  int ncase = 0;
  while (T--) {
    double cost, boost, target;
    cin >> cost >> boost >> target;
    double speed = 2.0;
    double t = 0;
    
    double best = target/speed;
    while (t < best+eps) {
      double inc = cost/speed;
      t += inc;
      speed += boost;
      best = min(best, t + target/speed);
    }
    cout << "Case #" << ++ncase << ": " << fixed << best << endl;
  }
}