#include <bits/stdc++.h>

using namespace std;

template<class T> inline T sqr(const T& a) {
  return a * a;
}

template<class T> inline T middle(const T &a, const T &b) {
  return (a + b) / 2;
}

template<class T> inline int len(const T &c) {
  return static_cast<int>(c.size());
}

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef vector<int> vi;

const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 100;

bool hset[N];
bool vset[N];
int ha[N][N];
int va[N][N];

bool PutH(const vi &v, int i) {
  for (int j = 0; j < len(v); ++j) {
    if (vset[j] && va[i][j] != v[j]) {
      return false;
    }
    ha[i][j] = v[j];  
  }
#if 0
  printf("add h #%d:", i);
  for (int j = 0; j < len(v); ++j) {
    printf(" %d", v[j]);  
  }
  puts("");
#endif
  hset[i] = true;
  return true;
}

bool PutV(const vi &v, int j) {
  for (int i = 0; i < len(v); ++i) {
    if (hset[i] && ha[i][j] != v[i]) {
      return false;
    }
    va[i][j] = v[i];  
  }
#if 0
  printf("add v #%d:", j);
  for (int i = 0; i < len(v); ++i) {
    printf(" %d", v[i]);  
  }
  puts("");
#endif
  vset[j] = true;
  return true;
}

bool Rec(const vector<vi> &cs, int n, int ci, int ni, int nj) {
  if (ci >= len(cs)) {
    return true;
  }
  const vi &cur = cs[ci];
  for (int j = nj; j < min(n, nj + 2); ++j) {
    if (cur[0] == ha[0][j] && PutV(cur, j)) {
      if (Rec(cs, n, ci + 1, ni, j + 1)) {
        return true;
      }
      vset[j] = false;
    }
  }
  for (int i = ni; i < min(n, ni + 2); ++i) {
    if (PutH(cur, i)) {
      if (Rec(cs, n, ci + 1, i + 1, nj)) {
        return true;
      }
      hset[i] = false;
    }
  }
  return false;
}

void HandleCase() {
  int n;
  scanf("%d", &n);
  vector<vi> cs;
  int m = 2 * n - 1;
  for (int i = 0; i < m; ++i) {
    vi cur(n);
    for (int j = 0; j < n; ++j) {
      scanf("%d", &cur[j]);  
    }
    cs.push_back(cur);
  }
  sort(cs.begin(), cs.end());
  /*
  vi single;
  int j = 0;
  for (int i = 1; i < m; ++i) {
    int t = cs[i][0];
    while (j < n && cs[0][j] < t) {
      ++j;
    }
    if (j >= n) {
      break;
    }
    if (cs[0][j] > t) {
      continue;
    }
    if (t != cs[i - 1][0] && (i + 1 >= m || cs[i + 1][0] != t)) {
      single.push_back(i);
    }
  }
  assert(single.size());
  */
  memset(hset, 0, sizeof hset);
  memset(vset, 0, sizeof vset);
  PutH(cs[0], 0);
  assert(Rec(cs, n, 1, 1, 0));
  vector<int> ans;
  for (int i = 0; i < n; ++i) {
    if (!hset[i]) {
      assert(ans.size() == 0);
      for (int j = 0; j < n; ++j) {
        ans.push_back(va[i][j]);  
      }
    }
  }
  for (int j = 0; j < n; ++j) {
    if (!vset[j]) {
      assert(ans.size() == 0);
      for (int i = 0; i < n; ++i) {
        ans.push_back(ha[i][j]);  
      }
    }
  }
  assert(ans.size() > 0);
  for (int i = 0; i < n; ++i) {
    printf(" %d", ans[i]);  
  }
  puts("");
}

int main() {
  int tests;
  scanf("%d", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d:", test);
    HandleCase();
  }
  return 0;
}
