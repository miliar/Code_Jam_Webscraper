#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXN = 1010;
int a[MAXN];
int ind[MAXN];

bool myComp(const int& i, const int& j) {
  return a[i] < a[j];
}

int solve() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    ind[i] = i;
  }
  sort(ind, ind + n, myComp);
  int res = 0;
  for (int i = 0; i < n; ++i) {
    int left = ind[i];
    int right = n - 1 - ind[i];
    for (int j = 0; j < i; ++j) {
      if (ind[j] < ind[i]) {
        --left;
      }
      if (ind[j] > ind[i]) {
        --right;
      }
    }
    left = max(0, left);
    right = max(0, right);
    res += min(left, right);
  }
  return res;
}

int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  int nTests;
  cin >> nTests;
  for (int test = 1; test <= nTests; ++test) {
    int res = solve();
    cout << "Case #" << test << ": " << res << "\n";
  }
  return 0;
}
