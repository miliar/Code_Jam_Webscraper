#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <cstring>
using namespace std;

const int MAXM = 8;
const int MAXN = 4;

string s[MAXM];
int m, n;
int a[MAXM];
int best = -1;
int cnt = -1;
int used[MAXN];

int pref[MAXM][MAXM];

int getPref(int i, int j) {
  if (pref[i][j] != -1) {
    return pref[i][j];
  }
  int k = 0;
  while (k < int(s[i].size())) {
    if (s[i][k] != s[j][k]) {
      pref[i][j] = k;
      return k;
    }
    ++k;
  }
  pref[i][j] = k;
  return k;
}

void rec(int i) {
  if (i < m) {
    for (int val = 0; val < n; ++val) {
      a[i] = val;
      rec(i + 1);
    }
  } else {
    memset(used, 0, sizeof used);
    int res = 0;
    for (int j = 0; j < m; ++j) {
      res += int(s[j].size());
      used[a[j]] = 1;
      int maxx = 0;
      for (int k = 0; k < j; ++k) {
        if (a[k] == a[j]) {
          int temp = getPref(j, k);
          if (temp > maxx) {
            maxx = temp;
          }
        }
      }
      res -= maxx;
    }
    res += n;
    bool failed = false;
    for (int j = 0; j < n; ++j) {
      if (!used[j]) {
        failed = true;
        break;
      }
    }
    if (failed) return;
    if (res > best) {
      best = res;
      cnt = 1;
    } else if (best == res) {
      ++cnt;
    }
  }
}

void solve(int test) {
  cin >> m >> n;
  for (int i = 0; i < m; ++i) {
    cin >> s[i];
  }
  best = -1;
  cnt = 0;
  memset(a, 0, sizeof a);
  memset(pref, -1, sizeof pref);
  rec(0);
  cout << "Case #" << test << ": " << best << " " << cnt << "\n";
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
