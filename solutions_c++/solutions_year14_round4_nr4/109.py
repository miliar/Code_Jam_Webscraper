#include <algorithm>
#include <iostream>
#include <sstream>
#include <cassert>
#include <cstdarg>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <ctime>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(c) (c).begin(), (c).end()
#define mp make_pair
#define pb push_back
#define sz(c) (int)(c).size()
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

char str[200];

void solve(int test) {
  int n, m;
  scanf("%d%d", &m, &n);
  vector<string> s;
  for (int i = 0; i < m; i++) {
    scanf("%s", str);
    s.push_back(string(str));
  }
  int M = 1;
  int res = n;
  int ans = 0;
  eprintf("test = %d\n", test);
  for (int i = 0; i < m; i++) M *= n;
  eprintf("M = %d\n", M);
  for (int mask = 0; mask < M; mask++) {
    map<int, set<string> > h;
    int tmask = mask;
    for (int i = 0; i < m; i++) {
      int id = tmask % n;
      for (int j = 0; j <= sz(s[i]); j++) {
        h[id].insert(s[i].substr(0, j));
      }
      tmask /= n;
    }
    int total = 0;
    for (int i = 0; i < n; i++) {
      total += sz(h[i]);
      if (sz(h[i]) == 0) {
        total = 0;
        break;
      }
    }
    if (total > res) {
      res = total;
      ans = 0;
    }
    if (total == res) {
      ans++;
    }
  }
  printf("Case #%d: %d %d\n", test, res, ans);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    solve(test);
  }
}
