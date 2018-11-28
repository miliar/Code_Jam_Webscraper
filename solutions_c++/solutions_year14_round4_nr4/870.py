#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int n, m;

map<string, int> mp;

const int INF = 0x7fffffff;
char str[100][100];
int num[100];

pair<int,int> ret;

int comp(int i) {
  set<int> st;
  for (int j = 0; j < m; ++j) {
    if (num[j] != i) continue;
    for (int k = 0; str[j][k]; ++k) {
      st.insert(mp[string(str[j], k + 1)]);
    }
  }
  if (st.empty()) return 0;
  return st.size() + 1;
}

void comp() {
  int r = 0;
  for (int i = 0; i < n; ++i) {
    r += comp(i);
  }
  if (r > ret.first) {
    ret = make_pair(r, 1);
  } else if (r == ret.first) {
    ++ret.second;
  }
}

void go(int i) {
  if (i == m) {
    comp();
    return;
  }
  for (int j = 0; j < n; ++j) {
    num[i] = j;
    go(i + 1);
  }
}

void solve() {
  mp.clear();
  ret = make_pair(0, 0);
  scanf("%d%d", &m, &n);
  int t = 0;
  for (int i = 0; i < m; ++i) {
    scanf("%s", str[i]);
    for (int j = 0; str[i][j]; ++j) {
      mp[string(str[i], j + 1)] = ++t;
    }
  }
  go(0);
  printf("%d %d\n", ret.first, ret.second);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
