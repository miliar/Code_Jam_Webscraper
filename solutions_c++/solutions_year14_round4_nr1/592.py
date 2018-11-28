#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXN = 10010;
int a[MAXN];

void solve(int test) {
  int n, x;
  cin >> n >> x;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  sort(a, a + n);
  int res = 0;
  int j = n - 1;
  for (int i = 0; i <= j; ++i) {
    while (a[i] + a[j] > x && j >= i) {
      --j;
      ++res;
    }
    if (i <= j) {
      ++res;
      --j;
    }
  }
  cout << "Case #" << test << ": " << res << "\n";
}

int main() {
  cin.sync_with_stdio(false);
  cout.sync_with_stdio(false);
  int nTests;
  cin >> nTests;
  for (int test = 1; test <= nTests; ++test) {
    solve(test);
  }
  return 0;
}
