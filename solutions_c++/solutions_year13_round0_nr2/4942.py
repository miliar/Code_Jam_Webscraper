#include <iostream>
using namespace std;

const int MAX = 1000; // TODO

int arr[MAX][MAX];
int rowmax[MAX];
int colmax[MAX];

bool solve() {
  int n, m;
  cin >> n >> m; // Num rows then num columns
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      cin >> arr[i][j];
  for (int j = 0; j < m; ++j)
    colmax[j] = 0;
  for (int i = 0; i < n; ++i) {
    rowmax[i] = 0;
    for (int j = 0; j < m; ++j) {
      if (arr[i][j] > rowmax[i])
        rowmax[i] = arr[i][j];
      if (arr[i][j] > colmax[j])
        colmax[j] = arr[i][j];
    }
  }
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < m; ++j)
      if (arr[i][j] != rowmax[i] && arr[i][j] != colmax[j])
        return false;
  return true;
}

int main() {
  int t;
  cin >> t;
  for (int c = 1; c <= t; ++c) {
    cout << "Case #" << c << ": ";
    if (solve())
      cout << "YES";
    else
      cout << "NO";
    cout << endl;
  }
}
