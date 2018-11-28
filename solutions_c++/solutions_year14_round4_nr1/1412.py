#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int solve() {
  int n, x;
  cin >> n >> x;
  vector<int> v(n);
  for (int i = 0; i < n; ++i) cin >> v[i];
  sort(v.begin(), v.end());
  int res = 0;
  int i = 0, j = n - 1;
  while (i <= j) {
    if (i == j) return res + 1;
    if (v[i] + v[j] <= x) {
      ++i;
      --j;
    }
    else --j;
    ++res;
  }
  return res;
}

int main() {
  int casos;
  cin >> casos;
  for (int i = 1; i <= casos; ++i) cout << "Case #" << i << ": " << solve() << endl;
}
