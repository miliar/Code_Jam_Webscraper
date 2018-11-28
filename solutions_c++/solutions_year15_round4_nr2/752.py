#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int T;
  cin >> T;
  cout.precision(8);
  for (int i = 0; i < T; ++i) {
    int N;
    double V, X;
    cin >> N >> V >> X;
    cout << "Case #" << i+1 << ": ";
    if (N == 1) {
      double R, C;
      cin >> R >> C;
      if (C == X) {
        // cout << "R: " << R << ", C: " << C << endl;
        cout << V/R << endl;
      }
      else {
        cout << "IMPOSSIBLE" << endl;
      }
      continue;
    }
    else { // N == 2
      double R1, C1, R2, C2;
      cin >> R1 >> C1 >> R2 >> C2;
      // cout << "R1: " << R1 << ", C1: " << C1 << endl;
      // cout << "R2: " << R2 << ", C2: " << C2 << endl;
      if (C1 < X && C2 < X) {
        cout << "IMPOSSIBLE" << endl;
      }
      else if (C1 > X && C2 > X) {
        cout << "IMPOSSIBLE" << endl;
      }
      else if (C1 == C2) {
        cout << (V/(R1+R2)) << endl;
      }
      else {
        double V2 = V*(X-C1)/(C2-C1);
        double V1 = V*(X-C2)/(C1-C2);
        // cout << "V1: " << V1 << ", V2: " << V2 << endl;
        cout << max(V2/R2, V1/R1) << endl;
      }
      continue;
    }
  }
}
