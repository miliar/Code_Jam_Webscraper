#include <algorithm>
#include <functional>
#include <iostream>
#include <limits>
#include <numeric>
#include <queue>
#include <sstream>
#include <vector>
#include <map>
#include <set>

#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

int N, M;
int v[100][100];
int max_of_hol[100];
int max_of_ver[100];
int hol[100];
int ver[100];

bool f(int y, int x) {
  if (y == N) return true;
  int nx = x+1, ny = y;
  if (nx == M) { ny++; nx = 0; }

  if (v[y][x] == hol[y] || v[y][x] == ver[x]) {
    return f(ny, nx);
  }

  if (hol[y] == -1 && max_of_hol[y] == v[y][x]) {
    hol[y] = v[y][x];
    if (f(ny, nx)) return true;
    hol[y] = -1;
  }
  if (ver[x] == -1 && max_of_ver[x] == v[y][x]) {
    ver[x] = v[y][x];
    if (f(ny, nx)) return true;
    ver[x] = -1;
  }
  return false;
}

int main(void) {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    for (int k = 0; k < 100; k++) hol[k] = ver[k] = -1;

    cin >> N >> M;
    for (int y = 0; y < N; y++) for (int x = 0; x < M; x++) cin >> v[y][x];

    for (int y = 0; y < N; y++) {
      int m = -1;
      for (int x = 0; x < M; x++) m = max(m, v[y][x]);
      max_of_hol[y] = m;
    }
    for (int x = 0; x < M; x++) {
      int m = -1;
      for (int y = 0; y < N; y++) m = max(m, v[y][x]);
      max_of_ver[x] = m;
    }

    bool ans = f(0, 0);
    if (f(0, 0)) {
      cout << "Case #" << i << ": YES" << endl;
    } else {
      cout << "Case #" << i << ": NO" << endl;
    }
  }
  return 0;
}
