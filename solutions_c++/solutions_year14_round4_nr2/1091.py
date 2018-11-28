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

const int N = 10000;
int tab[N];

set<pair<int,int> > st;

bool check(int *a, int *b) {
  bool up = true;
  for (; a + 1 < b; ++a) {
    if (a[1] > a[0] && !up) return false;
    if (a[1] < a[0]) up = false;
  }
  return true;
}

int swaps(int *a, int *b) {
  int ret = 0;
  for (; a != b; ++a) {
    for (int *c = a + 1; c != b; ++c) {
      ret += st.count(make_pair(*c, *a));
    }
  }
  return ret;
}

void solve() { 
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", tab + i);
  }
  st.clear();
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) 
      st.insert(make_pair(tab[i], tab[j]));
  }
  sort (tab, tab + n);
  int ret = n * n;
  do {
    if (!check(tab, tab + n)) continue;
    ret = min(ret, swaps(tab, tab + n));
  } while (next_permutation(tab, tab + n));
  printf("%d\n", ret);
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
