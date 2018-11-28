#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "D"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

bool IsGood(int n, int mask) {
  vvi G(2 * n, vi(2 * n));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if ((mask >> (i * n + j)) & 1) {
        G[i][n + j] = G[n + j][i] = 1;
      }
    }
  }
  vb done(2 * n, false);
  for (int i = 0; i < n; ++i) {
    if (done[i]) {
      continue;
    }
    done[i] = true;
    queue<int> q;
    vi comp;
    q.push(i);
    comp.push_back(i);
    while (!q.empty()) {
      int cur = q.front();
      q.pop();
      for (int i = 0; i < 2 * n; ++i) {
        if (G[cur][i]) {
          if (!done[i]) {
            done[i] = true;
            q.push(i);
            comp.push_back(i);
          }
        }
      }
    }
    int left = 0;
    int right = 0;
    for (int a = 0; a < comp.size(); ++a) {
      if (comp[a] < n) {
        ++left;
      } else {
        ++right;
      }
    }
    if (left != right) {
      return false;
    }
    for (int a = 0; a < comp.size(); ++a) {
      for (int b = 0; b < comp.size(); ++b) {
        if (comp[a] < n && comp[b] >= n && !G[comp[a]][comp[b]]) {
          return false;
        }
      }
    }
  }
  return true;
}

int FreeformSlow(int n, const vector<string>& field) {
  int mask = 0;
  int res = n * n;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (field[i][j] == '1') {
        mask |= (1 << (i * n + j));
      }
    }
  }
  for (int full_mask = mask; full_mask < (1 << (n * n)); ++full_mask) {
    if ((full_mask & mask) != mask) {
      continue;
    }
    if (IsGood(n, full_mask)) {
      int curres = 0;
      for (int i = 0; i < (n * n); ++i) {
        if (((full_mask >> i) & 1) && !((mask >> i) & 1)) {
          ++curres;
        }
      }
      if (curres < res) {
        res = curres;
      }
    }
  }
  return res;
}

int INF;

int Go(int mask, int a, int b, int C, const vector<pii>& sum_size, vvvi& cache) {
  if (mask == 0) {
    if (a != b) {
      cerr << "a = " << a << ", b = " << b << endl;
      abort();
    }
    return a;
  }
  if (cache[mask][a][b] != INF) {
    return cache[mask][a][b];
  }
  int& res = cache[mask][a][b];
  for (int nmask = mask; nmask > 0; nmask = (nmask - 1) & mask) {
    pii p = sum_size[nmask];
    if (p.first >= p.second && p.first - p.second <= b) {
      res = min(res, p.first * p.first + Go(mask ^ nmask, a, b - (p.first - p.second), C, sum_size, cache));
    }
    if (p.first < p.second && p.second - p.first <= a) {
      res = min(res, p.second * p.second + Go(mask ^ nmask, a - (p.second - p.first), b, C, sum_size, cache));
    }
  }
  return res;
}

int Freeform(int n, const vector<string>& field) {
  int init_size = 0;
  vvi G(2 * n, vi(2 * n));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (field[i][j] == '1') {
        G[i][j + n] = G[j + n][i] = 1;
        ++init_size;
      }
    }
  }
  vb done(2 * n, false);
  vector<pii> comps;
  for (int i = 0; i < 2 * n; ++i) {
    if (done[i]) {
      continue;
    }
    done[i] = true;
    queue<int> q;
    q.push(i);
    vi comp;
    comp.push_back(i);
    while (!q.empty()) {
      int cur = q.front();
      q.pop();
      for (int j = 0; j < 2 * n; ++j) {
        if (G[cur][j] && !done[j]) {
          done[j] = true;
          q.push(j);
          comp.push_back(j);
        }
      }
    }
    pii x(0, 0);
    for (int a = 0; a < comp.size(); ++a) {
      if (comp[a] < n) {
        ++x.first;
      } else {
        ++x.second;
      }
    }
    comps.push_back(x);
  }
  int add = 0;
  int a = 0;
  int b = 0;
  vector<pii> filtered_comps;
  for (int i = 0; i < comps.size(); ++i) {
    if (comps[i].first == comps[i].second) {
      add += comps[i].first * comps[i].first;
      continue;
    }
    if (comps[i].first == 0 || comps[i].second == 0) {
      if (comps[i].first + comps[i].second != 1) {
        cerr << "Strange component : " << comps[i].first << comps[i].second << endl;
        abort();
      }
      a += comps[i].first;
      b += comps[i].second;
      continue;
    }
    filtered_comps.push_back(comps[i]);
  }
  comps = filtered_comps;
  int C = comps.size();
  vector<pii> sum_size(1 << C, pii(0, 0));
  for (int mask = 0; mask < (1 << C); ++mask) {
    for (int i = C - 1; i >= 0; --i) {
      if ((mask >> i) & 1) {
        sum_size[mask] = sum_size[mask ^ (1 << i)];
        sum_size[mask].first += comps[i].first;
        sum_size[mask].second += comps[i].second;
        break;
      }
    }
  }
  INF = n * n + 10;
  vector< vector< vector<int> > > cache((1 << C), vvi(a + 1, vi(b + 1, INF)));
  int res = Go((1 << C) - 1, a, b, C, sum_size, cache);
  return res + add - init_size;
}

int main() {
  /*while (true) {
    int n = rand() % 5 + 1;
    cerr << n << endl;
    vector<string> field(n);
    for (int i = 0; i < n; ++i) {
      field[i] = "";
      for (int j = 0; j < n; ++j) {
        field[i] += ('0' + rand() % 2);
      }
      cerr << field[i] << endl;
    }
    int res1 = FreeformSlow(n, field);
    int res2 = Freeform(n, field);
    if (res1 != res2) {
      cerr << "WA " << res1 << ' ' << res2 << endl;
      break;
    } else {
      cerr << "OK " << res1 << endl;
    }
  }*/
  /*while (true) {
    int n = 25;
    cerr << n << endl;
    vector<string> field(n);
    for (int i = 0; i < n; ++i) {
      field[i] = "";
      for (int j = 0; j < n; ++j) {
        field[i] += '0';
      }
      //cerr << field[i] << endl;
    }
    for (int i = 0; i + 2 < 22; i += 3) {
      field[i][i] = '1';
      field[i][i + 1] = '1';
      field[i + 1][i + 2] = '1';
      field[i + 2][i + 2] = '1';
    }
    int res = Freeform(n, field);
    cerr << res << endl;
  }*/
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    int n;
    cin >> n;
    vector<string> field(n);
    for (int i = 0; i < n; ++i) {
      cin >> field[i];
    }
    int res = Freeform(n, field);
    cout << "Case #" << (test_index + 1) << ": " << res << endl;
    cerr << "Case #" << (test_index + 1) << ": " << res << endl;
    
  }
  return 0;
}
