#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int k = 1; k <= T; ++k) {
    int Smax;
    int ans = 0, total = 0;

    cin >> Smax;
    for (int i = 0; i <= Smax; ++i) {
      char Si;
      cin >> Si;
      int n = Si - '0';
      if (n > 0 && total < i) {
        ans += (i - total);
        total += (i - total);
      }
      total += n;
    }
    cout << "Case #" << k << ": " << ans << endl;
  }
  return 0;
}
