#pragma comment(linker, "/STACK:256000000")
#include <stdio.h>
#include <iostream>
#include <cmath>
#include <math.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

char tab[102][102];

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  std::ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) { 
    int r, c;
    cin >> r >> c;
    vector<int> sum_r, sum_c;
    sum_r.resize(r);
    sum_c.resize(c);
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        cin >> tab[i][j];
        if (tab[i][j] != '.') {
          sum_r[i]++;
          sum_c[j]++;
        }
      }
    }
    bool can = true;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (tab[i][j] != '.') {
          if (sum_r[i] == 1 && sum_c[j] == 1) {
            can = false;
          }
        }
      }
    }
    if (can) {
      int res = 0;
      sum_r.clear();
      sum_r.resize(r);
      sum_c.clear();
      sum_c.resize(c);
      for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
          if (tab[i][j] == '<' && sum_r[i] == 0) {
            res++;
          }
          if (tab[i][j] == '^' && sum_c[j] == 0) {
            res++;
          }
          if (tab[i][j] != '.') {
            sum_r[i]++;
            sum_c[j]++;
          }
        }
      }
      sum_r.clear();
      sum_r.resize(r);
      sum_c.clear();
      sum_c.resize(c);
      for (int i = r-1; i >= 0; --i) {
        for (int j = c-1; j >= 0; --j) {
          if (tab[i][j] == '>' && sum_r[i] == 0) {
            res++;
          }
          if (tab[i][j] == 'v' && sum_c[j] == 0) {
            res++;
          }
          if (tab[i][j] != '.') {
            sum_r[i]++;
            sum_c[j]++;
          }
        }
      }

      cout << "Case #" << t << ": ";
      cout << res << "\n";
    } else {
      cout << "Case #" << t << ": ";
      cout << "IMPOSSIBLE" << "\n";
    }
  }
}
/*
5
4 4
>>v<
..v.
..v.
^<<.
*/