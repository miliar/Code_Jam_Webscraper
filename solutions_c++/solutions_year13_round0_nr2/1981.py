#include <iostream>

using namespace std;

int lawn[100][100];

int n, m;

bool getout(int x, int y) {
  int v = lawn[x][y];
  
  bool ok = true;
  for (int i = 0; i < n; i++) {
    if (lawn[i][y] > v) {
      ok = false;
      break;
    }
  }
  if (ok) return true;
  
  ok = true;
  for (int i = 0; i < m; i++) {
    if (lawn[x][i] > v) {
      ok = false;
      break;
    }
  } 
  if (ok) return true;
  
  return false;
}

bool check() {
  for (int i = 0; i < n; i++) {
    for (int k = 0; k < m; k++) {
      if (!getout(i, k))
        return false;
    }
  }
  return true;
}

int main() {
  int tc; cin >> tc;
  for (int t = 1; t <= tc; t++) {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
      for (int k = 0; k < m; k++) {
        cin >> lawn[i][k];
      }
    }
    cout << "Case #" << t << ": " << (check() ? "YES" : "NO") << endl;
  }
  
  return 0;
}
