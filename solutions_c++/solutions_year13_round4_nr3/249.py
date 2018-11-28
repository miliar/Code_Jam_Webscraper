#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
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

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

#define PROBLEM_ID "C"

ostream& operator<<(ostream& out, const vector<int>& a) {
  for (int i = 0; i < a.size(); ++i) {
    out << a[i] << ' ';
  }
  out << endl;
  return out;
}

pair<vi, vi> GetAB(const vi& perm) {
  int n = perm.size();
  vector<int> a(n, 1);
  for (int i = 1; i < n; ++i) {
    for (int j = 0; j < i; ++j) {
      if (perm[j] < perm[i]) {
        a[i] = max(a[i], a[j] + 1);
      }
    }
  }
  vector<int> b(n, 1);
  for (int i = n - 2; i >= 0; --i) {
    for (int j = i + 1; j < n; ++j) {
      if (perm[j] < perm[i]) {
        b[i] = max(b[i], b[j] + 1);
      }
    }
  }
  return MP(a, b);
}

bool go(int depth, const vi& a, const vi& b, vb& used, vi& smallest, vi& value) {
  int n = value.size();
  if (depth == n) {
    return true;
  }
  for (int i = 0; i < depth; ++i) {
    smallest[i] = value[i];
  }
  bool changed;
  do {
    changed = false;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        if (a[j] <= a[i] && smallest[j] + 1 > smallest[i]) {
          smallest[i] = smallest[j] + 1;
          changed = true;
          if (i < depth) {
            return false;
          }
        }
        if (b[i] <= b[j] && smallest[i] + 1 > smallest[j]) {
          smallest[j] = smallest[i] + 1;
          changed = true;
          if (j < depth) {
            return false;
          }
        }
      }
    }          
  } while (changed);
  for (int v = smallest[depth]; v <= n; ++v) {
    if (!used[v]) {
      used[v] = true;
      value[depth] = v;
      vi smallest_copy = smallest;
      for (int i = depth + 1; i < n; ++i) {
        while (smallest[i] < n && used[smallest[i]]) {
          ++smallest[i];
        }
      }
      if (go(depth + 1, a, b, used, smallest, value)) {
        return true;
      } else {
        used[v] = false;
        smallest = smallest_copy;
      }
    }
  }
}

vi GetSmallestX(const vi& a, const vi& b) {
  int n = a.size();
  /*vector<bool> used(n + 1, false);
  vector<int> smallest(n, 0), value(n);
  for (int i = 0; i < n; ++i) {
    smallest[i] = a[i] + b[i] - 1;
  }
  go(0, a, b, used, smallest, value);*/
  vector< vector<bool> > less(n, vector<bool>(n, false));
  vector<vector<int> > layers(n + 1);
  for (int i = 0; i < n; ++i) {
    if (!layers[a[i] - 1].empty()) {
      less[i][layers[a[i] - 1].back()] = true;
    }
    if (a[i] - 2 >= 0) {
      if (!layers[a[i] - 2].empty()) {
        less[layers[a[i] - 2].back()][i] = true;
      }
    }
    if (!layers[a[i]].empty()) {
      less[i][layers[a[i]].back()] = true;
    }
    layers[a[i] - 1].push_back(i);
  }
  vvi layers2(n + 1);
  for (int i = n - 1; i >= 0; --i) {
    if (!layers2[b[i] - 1].empty()) {
      less[i][layers2[b[i] - 1].back()] = true;
    }
    if (b[i] - 2 >= 0) {
      if (!layers2[b[i] - 2].empty()) {
        less[layers2[b[i] - 2].back()][i] = true;
      }
    }
    if (!layers2[b[i]].empty()) {
      less[i][layers2[b[i]].back()] = true;
    }
    layers2[b[i] - 1].push_back(i);
  }
  vi smallest(n, 1);
  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (less[i][k] && less[k][j]) {
          less[i][j] = true;
        }
      }
    }
  }
  for (int i = 0; i < n; ++i) {
    int cnt = 0;
    for (int j = 0; j < n; ++j) {
      if (less[j][i]) {
        ++cnt;
      }
    }
    smallest[i] = max(smallest[i], cnt + 1);
  }
  vi value(n);
  vb used(n + 1, false);
  for (int step = 0; step < n; ++step) {
    for (int k = 0; k < n; ++k) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (less[i][j] && smallest[j] < smallest[i] + 1) {
            smallest[j] = smallest[i] + 1;
          }
        }
      }
    }
    value[step] = smallest[step];
    used[smallest[step]] = true;
    for (int i = step + 1; i < n; ++i) {
      while (smallest[i] < n && used[smallest[i]]) {
        ++smallest[i];
      }
    }
    vi less_cnt(n);
    for (int i = step + 1; i < n; ++i) {
      for (int j = step + 1; j < n; ++j) {
        if (less[j][i]) {
          less_cnt[i]++;
        }
      }
    }
    vi less_cnt2(n + 1);
    for (int i = 1; i <= n; ++i) {
      if (!used[i]) {
        for (int j = i + 1; j <= n; ++j) {
          less_cnt2[j]++;
        }
      }
    }
    for (int i = step + 1; i < n; ++i) {
      while (smallest[i] < n && less_cnt2[smallest[i]] < less_cnt[i]) {
        ++smallest[i];
      }
    }
  }
  return value;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int n = 8;
  vector<int> perm;
  for (int i = 1; i <= n; ++i) {
    perm.push_back(i);
  }
  /*perm.push_back(3);
  perm.push_back(5);
  perm.push_back(2);
  perm.push_back(1);
  perm.push_back(4);*/
  /*map<pair<vi, vi>, set<vi> > cnt;
  do {
    pair<vi, vi> p = GetAB(perm);
    vi a = p.first;
    vi b = p.second;
    cerr << perm << a << b;
    vi best = GetSmallestX(a, b);
    pair<vi, vi> p2 = GetAB(best);
    cout << perm << a << b << best;
    cerr << best << endl;
    if (a != p2.first || b != p2.second) {
      cerr << p2.first << p2.second << endl;
      cerr << "Wrong answer" << endl;
      break;
    }
    cerr << "OK" << endl;
  } while (next_permutation(perm.begin(), perm.end()));
  return 0;*/
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int n;
    cin >> n;
    vi a(n), b(n);
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
      cin >> b[i];
    }
    vi best = GetSmallestX(a, b);
    cout << "Case #" << test_index + 1 << ": " << best;
  }
  return 0;
}
