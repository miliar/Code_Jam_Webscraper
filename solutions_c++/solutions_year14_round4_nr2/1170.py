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

int a[1<<15], b[1<<15], need[1<<15];
int n;

int solve() {
  int r = 0;
  for (int i = 0; i < n - 1; ++i) {
    for (int j = i + 1; j < n; ++j) {
      if (need[i] > need[j]) {
        ++r;
      }
    }
  }
  return r;
}

bool valid() {
  for (int i = 0; i < n; ++i) {
    b[need[i]] = a[i];
  }
  int cnt = 0;
  for (int i = 0; i < n - 1; ++i) {
    if (cnt == 0) {
      if (b[i] < b[i + 1]) {
        continue;
      } else {
        ++cnt;
      }
    }
    if (cnt == 1) {
      if (b[i] > b[i + 1]) {
        continue;
      } else {
        return false;
      }
    }
  }
  return true;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T;
  cin >> T;
  for (int tests = 0; tests < T; ++tests) {
    cout << "Case #" << tests+1 << ": ";
    cin >> n;
    for (int i = 0; i < n; ++i) {
      cin>>a[i];
    }

    for (int i = 0; i < n; ++i) {
      need[i] = i;
    }

    int res = 1<<25;
    do {
      if (valid()) {
        res = min(res, solve());
      }
    } while (next_permutation(need, need+n));

    cout << res << endl;
  }

  return 0;
}