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

static const long long M = 1000000007LL;

  int r, c;

bool compare(const vector<int> &a, const vector<int> &b) {
  for (size_t i = 0; i < a.size(); ++i) {
    if (a[i] < b[i]) return true;
    if (b[i] < a[i]) return false;
  }
  return false;
}

inline bool nextVector(vector<int> &a) {
  for (int i = (int)a.size() - 1; i >= 0; --i) {
    if (a[i] < 3) {
      ++a[i];
      return true;
    }
    a[i] = 1;
  }
  return false;
}

bool checkOne(const vector<int> &a) {
  if (a[0] == 3 && a[1] != 3) return false;
  if (a.back() == 3 && a[a.size() - 2] != 3) return false;
  if (a.size() == 2) {
    return true;
  }
  for (size_t i = 1; i < a.size() - 1; ++i) {
    switch (a[i]) {
      case 1:
      if (a[i-1] == 1 && a[i+1] == 1) return false;
      break;
      case 2:
      break;
      case 3:
      if (a[i-1] != 3 && a[i+1] != 3) return false;
      break;
    }
  }
  return true;
}

bool checkT(const vector<int> &x, const vector<int> &y, const vector<int> &z) {
  int cnt = 0;
  cnt += x[0] == y[0];
  cnt += y[1] == y[0];
  cnt += z[0] == y[0];
  if (cnt != y[0]) return false;
  cnt = 0;
  const int n = x.size() - 1;
  cnt += x[n] == y[n];
  cnt += y[n - 1] == y[n];
  cnt += z[n] == y[n];
  if (cnt != y[n]) return false;
  for (int i = 1; i < n; ++i) {
    cnt = 0;
    cnt += x[i] == y[i];
    cnt += y[i - 1] == y[i];
    cnt += y[i + 1] == y[i];
    cnt += z[i] == y[i];
    if (cnt != y[i]) return false;
  }
  return true;
}

void print(vector<vector<int> > &v) {
    printf("\n");
  for (size_t i = 0; i < v.size(); ++i) {
    for (size_t j = 0; j < v[0].size(); ++j) {
      printf("%d ", v[i][j]);
    }
    printf("\n");
  }
    printf("\n");
}

bool checkC(vector<vector<int>> &drum) {
  for (size_t i = 1; i < drum.size(); ++i) {
    if (compare(drum[0], drum[i])) continue;
    for (size_t j = 1; j < drum.size(); ++j) {
      if (i + j >= drum.size()) break;
      if (compare(drum[i+j], drum[j])) return false;
    }
  }
  return true;
}

long long solve(vector<vector<int>> &drum, int i) {
  if (i == c) {
    if (!checkT(drum[c-1], drum[0], drum[1])) return 0;
    if (!checkT(drum[c-2], drum[c-1], drum[0])) return 0;
    if (!checkC(drum)) return 0;
    //print(drum);
    return 1;
  }
  long long ret = 0;
  drum[i].clear();
  drum[i].resize(r, 1);
  do {
    if (compare(drum[i], drum[0])) continue;
    if (!checkOne(drum[i])) continue;
    if (!checkT(drum[i-2], drum[i-1], drum[i])) continue;
    ret += solve(drum, i + 1);
  } while (nextVector(drum[i]));
  return ret;
}

long long solve(const vector<int> &v) {
  vector<vector<int> > drum(c);
  if (!checkOne(v)) return 0;
  drum[0] = v;
  drum[1].clear();
  drum[1].resize(r, 1);
  long long ret = 0;
  do {
    if (compare(drum[1], drum[0])) continue;
    if (!checkOne(drum[1])) continue;

    ret += solve(drum, 2);
  } while (nextVector(drum[1]));
  return ret;
}

void solve() {
  scanf("%d%d", &r, &c);
  vector<int> v(r, 1);
  long long ret = 0;
  do {
    ret += solve(v);
    ret %= M;
  } while (nextVector(v));
  printf("%lld\n", ret);
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
