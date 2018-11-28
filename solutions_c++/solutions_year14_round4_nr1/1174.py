#include <algorithm>
#include <cmath>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <random>
#include <set>
using namespace std;

int a[1<<15];

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T;
  cin >> T;
  for (int tests = 0; tests < T; ++tests) {
    cout << "Case #" << tests+1 << ": ";
    int n, x;
    cin >> n >> x;
    for (int i = 0; i < n; ++i) {
      cin>>a[i];
    }

    sort(a, a + n);
    int L = 0, R = n -1;
    int res = 0;
    while (L < R) {
      if (a[L] + a[R] <= x) {
        ++res;
        a[L] = -1;
        a[R] = -1;
        ++L;
        --R;
      } else {
        --R;
      }
    }
    for (int i = 0; i < n; ++i) {
      if (a[i] != -1) {
        ++res;
      }
    }

    cout << res << endl;
  }

  return 0;
}