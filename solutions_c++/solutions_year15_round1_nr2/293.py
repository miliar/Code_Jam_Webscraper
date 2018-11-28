// {{{ template
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<pii> vpii;
// }}}

int main() {
  cin.sync_with_stdio(0); cin.tie(0);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n, b;
    cin >> n >> b;
    vi a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    vll tmp(n);
    long long lo = -1, hi = (long long)1e17 + 100;
    while (lo + 1 < hi) {
      long long mid = (lo + hi) >> 1;
      long long count = 0;
      for (int i = 0; i < n; i++) {
        long long t = (mid + a[i] - 1) / a[i];
        count += t;
        tmp[i] = t * a[i];
      }
      if (count < b) {
        lo = mid;
      } else {
        hi = mid;
      }
    }
    long long count = 0;
    for (int i = 0; i < n; i++) {
      long long t = (lo + a[i] - 1) / a[i];
      count += t;
      tmp[i] = t * a[i];
    }
    assert(count < b);
    long long mini = LLONG_MAX;
    vector<int> candidate;
    for (int i = 0; i < n; i++) {
      if (tmp[i] < mini) {
        mini = tmp[i];
        candidate.clear();
        candidate.push_back(i);
      } else if (tmp[i] == mini) {
        candidate.push_back(i);
      }
    }
    assert((int)candidate.size() >= b - count);
    cout << "Case #" << t << ": " << candidate[b - count - 1] + 1 << endl;
  }
  return 0;
}

