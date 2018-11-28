#include <iostream>
#include <queue>
#include <vector>

using namespace std;

typedef priority_queue<int> pqi;
typedef vector<int> vi;

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int n;
    cin >> n;
    vi v(n);
    int mx = 0;
    for (int i = 0; i < n; ++i) {
      cin >> v[i];
      mx = max(mx, v[i]);
    }
    vi parts(n, 1);
    int r = mx;
    for (int d = 1; d < mx; ++d) {
      int iworst = -1, worst = 0;
      for (int i = 0; i < n; ++i) {
        if ((v[i] + parts[i] - 1) / parts[i] > worst) {
          iworst = i;
          worst = (v[i] + parts[i] - 1) / parts[i];
        }
      }
      ++parts[iworst];
      mx = 0;
      for (int i = 0; i < n; ++i) {
        mx = max(mx, (v[i] + parts[i] - 1) / parts[i]);
      }
      r = min(r, mx + d);
    }
    cout << "Case #" << t << ": " << r << endl;
  }
}