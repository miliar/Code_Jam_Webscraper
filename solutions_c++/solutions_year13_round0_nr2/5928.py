#include <iostream>

using namespace std;

const int MAXN = 105;

int n, m;

int a[MAXN][MAXN];

void Solve() {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> a[i][j];
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      bool good = true;
      for (int k = 0; k < n; k++) {
        good &= a[i][j] >= a[k][j];
      }

      if (!good) {
        good = true;
        for (int k = 0; k < m; k++) {
          good &= a[i][j] >= a[i][k];
        }

        if (!good) {
          cout << " NO\n";
          return;
        }
      }
    }
  }

  cout << " YES\n";
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cout << "Case #" << i << ":";
    Solve();
  }
}


