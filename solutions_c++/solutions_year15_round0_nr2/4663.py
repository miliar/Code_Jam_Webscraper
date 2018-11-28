#include <iostream>
#include <climits>
using namespace std;

int t[1002];

int main() {
  int T;
  cin >> T;

  for (int CASE = 1; CASE <= T; CASE++) {
    cout << "Case #" << CASE << ": " ;

    int n;
    cin >> n;

    int maxH = 0;

    for (int i = 0; i < n; i++) {
      cin >> t[i];
      maxH = max(maxH, t[i]);
    }

    int ans = INT_MAX;

    for (int h = maxH; h >= 1; h--) {
      int sum = h;
      for (int i = 0; i < n; i++) {
        sum += (t[i] - 1) / h;
      }
      ans = min(ans, sum);
    }

    cout << ans << endl;
  }
}
