#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
char const eol = '\n';
using namespace std;
typedef long long int64;
typedef pair<int,int> pii;

map<char,pii> dir = {
  {'>', pii{0, 1}},
  {'<', pii{0, -1}},
  {'v', pii{1, 0}},
  {'^', pii{-1, 0}},
};

int n, m;
vec<string> a;

int go(int i, int j, int di, int dj) {
  if (i < 0 || j < 0 || i == n || j == m) return 0;
  if (a[i][j] != '.') return 1;
  return go(i + di, j + dj, di, dj);
}

int sol() {
  int res = 0;
  FOR(i, 0, n) {
    FOR(j, 0, m) {
      if (a[i][j] != '.') {
        assert(dir.count(a[i][j]));
        int di = dir[a[i][j]].first;
        int dj = dir[a[i][j]].second;
        if (!go(i + di, j + dj, di , dj )) {
          bool ok = false;
          for (auto p : dir) {
            di = p.second.first;
            dj = p.second.second;
            if (go(i + di, j + dj, di, dj)) {
              ok = true;
              break;
            }
          }
          if (!ok) return -1;
          res += 1;
        }
      }
    }
  }

  return res;
}

void solve(int testcase) {
  cout << "Case #" << testcase << ": ";

  cin >> n >> m;
  a = vec<string>(n);
  FOR(i, 0, n) cin >> a[i];

  int res = sol();
  if (res == -1) {
    cout << "IMPOSSIBLE" << eol;
  } else {
    cout << res << eol;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int testcases;
  cin >> testcases;
  FOR(testcase, 1, testcases + 1) {
    cerr << "Case " << testcase << "/" << testcases << endl;
    solve(testcase);
  }

  return 0;
}
