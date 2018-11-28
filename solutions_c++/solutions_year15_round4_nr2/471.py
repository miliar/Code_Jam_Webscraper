#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  cin.sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int N;
    double V, X;
    cin >> N >> V >> X;
    double rate[2], temp[2];
    for (int i = 0; i < N; i++) {
      cin >> rate[i] >> temp[i];
    }
    cout << "Case #" << cas << ": ";
    if (N == 1) {
      if (temp[0] == X) {
        cout << fixed << setprecision(10) << V / rate[0] << endl;
      } else {
        cout << "IMPOSSIBLE" << endl;
      }
    } else {
      if (temp[0] == temp[1]) {
        if (temp[0] == X) {
          cout << fixed << setprecision(10) << V / (rate[0] + rate[1]) << endl;
        } else {
          cout << "IMPOSSIBLE" << endl;
        }
      } else if (temp[0] > X && temp[1] > X || temp[0] < X && temp[1] < X) {
        cout << "IMPOSSIBLE" << endl;
      } else {
        double v2 = (X - temp[0]) / (temp[1] - temp[0]);
        double v1 = (X - temp[1]) / (temp[0] - temp[1]);
        if (v1 < 0 || v2 < 0) {
          cout << "IMPOSSIBLE" << endl;
        } else {
          double t1 = v1 / rate[0];
          double t2 = v2 / rate[1];
          cout << fixed << setprecision(10) << max(t1, t2)  * V << endl;
        }
      }
    }
  }
}
