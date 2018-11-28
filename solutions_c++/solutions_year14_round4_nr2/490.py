#include <cassert>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <sstream>
#include <utility>

#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#include <memory.h>
using namespace std;

#define Pi 3.141592653589793
#define all(c) (c).begin(), (c).end()
typedef long long ll;

int solve(vector<int>& vi, int idx) {
  int res = 0;
  for (int i = 0; i < idx; ++i) {
    int pos = i;
    for (int j = i + 1; j < idx; ++j) {
      if (vi[pos] > vi[j]) {
        pos = j;
      }
    }
    while (pos != i) {
      swap(vi[pos], vi[pos - 1]);
      --pos;
      ++res;
    }
  }
  for (int i = idx + 1; i < vi.size(); ++i) {
    int pos = i;
    for (int j = i + 1; j < vi.size(); ++j) {
      if (vi[pos] < vi[j]) {
        pos = j;
      }
    }
    while (pos != i) {
      swap(vi[pos], vi[pos - 1]);
      --pos;
      ++res;
    }
  }
  return res;
}

bool is_valid(const vector<int>& perm) {
  int f = 0;
  while (f != perm.size() - 1 && perm[f] < perm[f + 1]) {
    ++f;
  }
  int l = perm.size() - 1;
  while (l != 0 && perm[l] < perm[l - 1]) {
    --l;
  }
  return f == l;
}

int find_diff(vector<int> from, vector<int> to) {
  int res = 0;
  for (int i = 0; i < to.size(); ++i) {
    int idx = i;
    while (from[idx] != to[i]) {
      ++idx;
    }
    while (idx != i) {
      swap(from[idx], from[idx - 1]);
      --idx;
      ++res;
    }
  }
  return res;
}

int brute_force(const vector<int>& vi) {
  vector<int> perm = vi;
  sort(all(perm));
  int res = 1000000000;
  do {
    if (is_valid(perm)) {
      res = min(res, find_diff(vi, perm));
    }
  } while (next_permutation(all(perm)));
  return res;
}

int vi[1024];

int main() {
#ifdef LOCAL_HOST
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int TT; cin >> TT;
  for (int tt = 1; tt <= TT; ++tt) {
    int n; cin >> n;
    vector<int> example(n);
    for (int i = 0; i < n; ++i) {
      cin >> vi[i];
      example[i] = vi[i];
    }

    int le = 0;
    int ri = n;
    int res = 0;
    for (int i = 0; i < n; ++i) {
      int idx = distance(vi, min_element(vi + le, vi + ri));
      if (idx - le < ri - 1 - idx) {
        while (idx != le) {
          swap(vi[idx], vi[idx - 1]);
          --idx;
          ++res;
        }
        ++le;
      } else {
        while (idx != ri - 1) {
          swap(vi[idx], vi[idx + 1]);
          ++idx;
          ++res;
        }
        --ri;
      }
    }

    printf("Case #%d: %d\n", tt, res);
  }

  return 0;
}
