#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

char V[55][55];
bool M[55][55];
bool col[55];
bool row[55];

bool Valid(int n) {
  memset(col, 0, sizeof col);
  memset(row, 0, sizeof row);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      row[i] |= M[i][j];
      col[j] |= M[i][j];
    }
  }
  for (int i = 0; i < n; ++i) {
    if (!col[i] || !row[i]) {
      return false;
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      bool eq = false, uneq = false;
      for (int k = 0; k < n; ++k) {
        if (M[i][k] == M[j][k] && M[i][k] == 1) {
          eq = true;
        } else if (M[i][k] != M[j][k]) {
          uneq = true;
        }
      }
      if (eq && uneq) {
        return false;
      }
    }
  }
  for (int i = 0; i < n; ++i) {
    int qr = 0, p = -1, qc = 0;
    for (int j = 0; j < n; ++j) {
      qr += M[i][j];
      if (M[i][j]) {
        p = j;
      }
    }
    for (int j = 0; j < n; ++j) {
      qc += M[j][p];
    }
    if (qr != qc) {
      return false;
    }
  }
  return true;
}

void Solve() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> V[i];
  }
  int ans = 1 << 30;
  for (int i = 0; i < (1 << (n * n)); ++i) {
    int p = 0;
    bool fail = false;
    int cost = 0;
    for (int j = 0; j < n; ++j) {
      for (int k = 0; k < n; ++k) {
        if (V[j][k] == '1' && !(i & (1 << p))) {
          fail = true;
        } else if (V[j][k] == '0' && (i & (1 << p))) {
          ++cost;
          M[j][k] = 1;
        } else if (V[j][k] == '1') {
          M[j][k] = 1;
        } else {
          M[j][k] = 0;
        }
        ++p;
      }
    }
    fail |= !Valid(n);
    if (!fail) {
      ans = min(ans, cost);
      //cerr << i << endl;
    }
  }
  //cerr << endl;
  cout << ans << endl;
}

int main() {
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
