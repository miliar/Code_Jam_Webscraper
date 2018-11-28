#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int, char> ic;
ic v[26];

int main() {
  ios_base::sync_with_stdio(false);
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cout << "Case #" << t << ":";
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
      cin >> v[i].first;
      v[i].second = 'A' + i;
    }
    sort(v, v + n);
    for (int i = n - 1; i > 0; --i) {
      while (v[i].first > v[i - 1].first) {
        for (int k = i; k < n; ++k) {
          cout << ' ' << v[k].second;
          --v[k].first;
        }
      }
    }
    for (int q = 0; q < v[0].first; ++q) {
      for (int i = 2; i < n; ++i) cout << ' ' << v[i].second;
      cout << ' ' << v[0].second << v[1].second;
    }
    cout << endl;
  }
}