#include <bits/stdc++.h>

using namespace std;

int arr[10];

int main() {
  int n;
  cin >> n;
  string p;
  for (int i = 0; i < n; ++i) {
    cin >> p;
    bool minus = p[0] == '-';
    int acc = 0;
    for (int j = 0; j < p.size(); ++j) {
      if (p[j] == '-' && (!j || (p[j - 1] != p[j]))) ++acc;
    }
    int ans = acc * 2 - minus;
    cout << "Case #" << (i + 1) << ": " << ans << endl;
  }
  return 0;
}
