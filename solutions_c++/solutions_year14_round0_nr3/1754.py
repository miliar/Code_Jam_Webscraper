#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int r, c, m; 
char arr[5][6];
int cc[5][5];
bool f[5][5];

int fill(int i, int j) {
  if (i < 0 || i >= r || j < 0 || j >= c) return 0;
  if (f[i][j]) return 0;
  if (arr[i][j] == '*') return 0;
  f[i][j] = true;
  int res = 1;
  if (cc[i][j] == 0) {
    for (int di = -1; di <= 1; di++) for (int dj = -1; dj <= 1; dj++) {
      res += fill(i+di, j+dj);
    }
  }
  return res;
}

void print() {
  for (int i = 0; i < r; i++) cout << arr[i] << endl;
}

bool analyze() {
  memset(cc, 0, sizeof(cc));
  for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) {
    if (arr[i][j] == '*') {
      cc[i][j] = -1;
      for (int di = -1; di <= 1; di++) for (int dj = -1; dj <= 1; dj++) {
        if (di == 0 && dj == 0) continue;
        int ii = i+di, jj = j+dj;
        if (ii < 0 || ii >= r || jj < 0 || jj >= c) continue;
        if (arr[ii][jj] == '*') continue;
        cc[ii][jj]++;
      }
    }
  }

  for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) if (cc[i][j] == 0) {
    memset(f, 0, sizeof(f));
    if (fill(i, j) == (r*c-m)) {
      arr[i][j] = 'c';
      print();
      return true;
    }
    return false;
  }

  if (m+1 == r*c) {
    for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) if (arr[i][j] != '*') {
      arr[i][j] = 'c';
      print();
      return true;
    }
  }
  return false;
}

bool go(int i, int j, int k) {
  if (i == r) return k == m && analyze();
  if (j == c) return go(i+1, 0, k);

  if (k < m) {
    arr[i][j] = '*';
    if (go(i, j+1, k+1)) return true;
  }

  arr[i][j] = '.';
  return go(i, j+1, k);
}

int main() {
  int testCases; cin >> testCases;
  for (int caseNo = 1; caseNo <= testCases; caseNo++) {
    cin >> r >> c >> m;
    for (int i = 0; i < r; i++) arr[i][c] = 0;
    cout << "Case #" << caseNo << ":" << endl;
    if (!go(0, 0, 0)) cout << "Impossible" << endl;
  }
  return 0;
}
