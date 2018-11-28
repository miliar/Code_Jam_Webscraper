#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    double r, w;
    cin >> r >> w;
    double ans;
    ans = (sqrt(1 + 8 * w / (2 * r - 1) / (2 * r - 1)) - 1 ) / 4 * (2 * r - 1);
    ans += 0.00000000001;
    cout << "Case #" << t + 1 << ": " << (long long)ans << endl;
  }
  return 0;
}
