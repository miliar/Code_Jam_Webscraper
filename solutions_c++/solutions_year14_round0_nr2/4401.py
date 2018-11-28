#include <iostream>
#include <vector>

using namespace std;

int main() {
  cout.setf(ios::fixed);
  cout.precision(7);
  
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    double c, f, x;
    cin >> c >> f >> x;
    
    double best = x/2.0;
    double bt = 0.0;
    for (int i = 0; bt < best; ++i) {
      double cur = bt + x/(2.0+double(i)*f);
      if (cur < best) best = cur;
      bt += c/(2.0+double(i)*f);
    }
    
    cout << "Case #" << ca << ": " << best << endl;
  }
}

