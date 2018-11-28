#include <iostream>
#include <algorithm>

using namespace std;

int t_;
int n, res1, res2;
double a[1005], b[1005];

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  cin >> t_;
  for (auto cas = 1; cas <= t_; cas++) {
    res1 = res2 = 0;
    cin >> n;
    for (auto i = 0; i < n; i++) cin >> a[i];
    for (auto i = 0; i < n; i++) cin >> b[i];
    sort(a, a + n);
    sort(b, b + n);
    for (auto i = 0, j = 0; i < n; i++) {
      if (a[i] < b[j]) { 
        // Can't beat anyway, bluff out biggest
      } else {
        // Can beat, bluff out smallest
        res1++;
        j++;
      }
    }
    for (auto i = 0, j = 0; i < n; i++, j++) {
      while (j < n && b[j] < a[i]) j++;
      if (j == n) res2 = n - i;
    }
    cout << "Case #" << cas << ": " << res1 << " " << res2 << endl;
  }
  return 0;
}