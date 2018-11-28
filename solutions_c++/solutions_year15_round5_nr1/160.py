/* 
  2014.03.26 15:10
  http://codeforces.ru/gym/100289/
*/


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <cmath>
#include <string> 
#include <ctime>

using namespace std;

// #undef Fdg_Home

int s[1000006], m[1000006], n, d;

vector<int> g[1000006];

vector<pair<int, int>> v;

int mn[1000006], mx[1000006];

inline void go(int x, int mn = 1e+9, int mx = -1e+9) {
  mn = min(s[x], mn);
  mx = max(s[x], mx);
  if (mx - d <= mn) {
    v.push_back({mx - d, -1});
    v.push_back({mn, 1});
  }
  // cout << x << "  " << mx - d << "  " << mn << endl;
  for (int u : g[x])
    go(u, mn, mx);
}

void solveTest(int CS) {
  printf("Case #%d: ", CS);
  scanf("%d%d", &n, &d);

  int s0, a, c, r;
  scanf("%d%d%d%d", &s0, &a, &c, &r);
  s[0] = s0;
  mn[0] = mx[0] = s[0];
  for (int i = 1; i < n; ++i) {
    s[i] = (1LL * s[i - 1] * a + c) % r;
    mn[i] = mx[i] = s[i];
  }

  scanf("%d%d%d%d", &s0, &a, &c, &r);
  m[0] = s0;
  for (int i = 1; i < n; ++i) {
    m[i] = (1LL * m[i - 1] * a + c) % r;
    mn[i] = min(mn[i], mn[m[i] % i]);
    mx[i] = max(mx[i], mx[m[i] % i]);
    // cout << i << "  " << m[i] << "  " << s[i] << endl;
  }
  m[0] = -1;

  for (int i = 0; i < n; ++i)
    g[i].clear();
  for (int i = 1; i < n; ++i) {
    g[m[i] % i].push_back(i);
  }

  v.clear();
  // go(0);
  for (int i = 0; i < n; ++i) {
    if (mx[i] - d <= mn[i]) {
      v.push_back({mx[i] - d, -1});
      v.push_back({mn[i], 1});
    }
  }
  sort(v.begin(), v.end());
  int ans = 0, cur = 0;
  for (int i = 0; i < v.size(); ++i) {
    cur -= v[i].second;
    ans = max(ans, cur);
  }
  printf("%d\n", ans);
}

int main() {
  freopen("output.txt", "w", stdout);
  int T;
  scanf("%d\n", &T);
  for (int test = 1; test <= T; ++test) {
    solveTest(test);
  }
  return 0;
}

