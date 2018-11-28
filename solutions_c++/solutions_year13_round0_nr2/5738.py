#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int n, m;
    cin >> n >> m;
    vector< vector<int> > lawn(n, vector<int> (m));
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j)
        cin >> lawn[i][j];
    vector<int> row(n, 0), col(m, 0);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        if (row[i] < lawn[i][j]) row[i] = lawn[i][j];
      }
    }
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (col[i] < lawn[j][i]) col[i] = lawn[j][i];
      }
    }
    bool fi = false;
    for (int i = 0; i < n and not fi; ++i) {
      for (int j = 0; j < m and not fi; ++j) {
        if (row[i] > lawn[i][j] and col[j] > lawn[i][j]) fi = true;
      }
    }
    cout << "Case #" << cas << ": ";
    if (fi) cout << "NO" << endl;
    else cout << "YES" << endl;
  }
}
