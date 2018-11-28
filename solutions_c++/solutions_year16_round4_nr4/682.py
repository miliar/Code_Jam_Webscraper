#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <cstdio>
#include <unordered_set>
using namespace std;

///////////////// macros and typedefs ///////////////////
#define rep(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define repd(i, n) for (int i = (n)-1; i >= 0; --i)
#define DEB(k) cerr << "debug: " #k << "=" << k << endl;
#define CLEAR(a) memset((a), 0, sizeof(a));
#define all(c) (c).begin(), (c).end()
#define mp(a, b) make_pair(a, b)
#define l(c) (int)((c).size())
#define sqr(a) ((a) * (a))
#define inf 0x7f7f7f7f
#define pb push_back
#define ppb pop_back
#define x first
#define y second
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;

using namespace std;

int n;
bool taken[4];
set<vector<string>> used;

bool dfs(const vector<string>& v, int i, int k) {
  if (i == n) {
    rep(j, n) if (v[k][j] == '1') {
      if (!taken[j]) return true;
    }
    return false;
  }
  if (i == k) return dfs(v, i+1, k);
  bool got = false;
  rep(j, n) if (!taken[j] && v[i][j] == '1') {
    taken[j] = true;
    if (!dfs(v, i+1, k)) {
      taken[j] = false;
      return false;
    }
    taken[j] = false;
    got = true;
  }
  return got;
}

bool isOk(const vector<string>& v) {
  rep(i, n) {
    if (!dfs(v, 0, i)) return false;
  }
  return true;
}

void print(const vector<string>& v) {
  cout << endl;
  rep(i, n) cout << v[i] << endl;
  cout << "========" << endl;
}

void solveCase() {
  used.clear();
  cin >> n;
  vector<string> v(n);
  rep(i, n) cin >> v[i];
  queue<vector<string>> q;
  q.push(v);
  used.insert(v);
  while (!q.empty()) {
    vector<string> cur = q.front();
    q.pop();
    //print(cur);
    int diff = 0;
    rep(i, n) rep(j, n) if (cur[i][j] == '1' && v[i][j] == '0') diff++;
    if (isOk(cur)) {
      cout << diff;
      return;
    }
    rep(i, n) rep(j, n) if (cur[i][j] == '0') {
      cur[i][j] = '1';
      if (used.find(cur) == used.end()) {
        q.push(cur);
        used.insert(cur);
      }
      cur[i][j] = '0';
    }
  }
}

//#define NAME "A-large"
#define NAME "D-small-attempt0"
//#define NAME "test"

int main() {
  freopen(NAME ".in", "rt", stdin);
  freopen(NAME ".out", "wt", stdout);
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    //cerr << "Case #" << i << ": ";
    solveCase();
    cout << endl;
    //cerr << endl;
  }
  return 0;
}
