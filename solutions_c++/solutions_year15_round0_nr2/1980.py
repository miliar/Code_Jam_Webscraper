#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {

  int t;
  cin >> t;

  for (int tc = 1; tc <= t; tc++) {
    int n;
    cin >> n;
    vector<int> v(n);
    int ans = 0;

    while (n--) {
      cin >> v[n];
      ans = max(ans, v[n]);
    }

    for (int i = 1; i <= 1000; i++) {
      int cnt = 0;

      for (int j = 0; j < v.size(); j++) {
        cnt += (v[j] - 1) / i;
      }

      ans = min(ans, cnt + i);
    }

    cout << "Case #" << tc << ": " << ans << '\n';
  }

  return 0;
}
