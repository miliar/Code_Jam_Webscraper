#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int main(void)
{
  int testcase;
  cin >> testcase;

  for (int tc = 1; tc <= testcase; tc++) {
    int n, m;
    cin >> n >> m;
    assert((0 < n) && (0 < m));
    vector<int> rowmax(n, 0);
    vector<int> colmax(m, 0);
    vector<vector<int> > grass;
    for (int i = 0; i < n; i++) {
      vector<int> row;
      for (int j = 0; j < m; j++) {
        int height;
        cin >> height;
        row.push_back(height);
        rowmax[i] = max(rowmax[i], height);
        colmax[j] = max(colmax[j], height);
      }
      grass.push_back(row);
    }

    bool found = false;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if ((grass[i][j] < rowmax[i]) && (grass[i][j] < colmax[j])) {
          cout << "Case #" << tc << ": NO" << endl;
          found = true;
          i = n;
          break;
        }
      }
    }

    if (! found) {
      cout << "Case #" << tc << ": YES" << endl;
    }
  }

  return 0;
}

