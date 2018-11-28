#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <sstream>

using namespace std;

//#define NAME "my"
//#define NAME "A-small-attempt1"
#define NAME "A-large"
typedef pair<int, int> PI;

int n, m;
char g[101][101];
char color[101][101];
char cc[101][101];
vector<PI> conn[101][101];

PI findNext(int vi, int vj, int di, int dj) {
  if (vi == -1 || vj == -1 || vi == n || vj == m) return PI(-1, -1);
  if (g[vi][vj] != '.') return PI(vi, vj);
  return findNext(vi + di, vj + dj, di, dj);
}

// 1 - in loop
// 2 - not in loop
char go(int vi, int vj) {
  if (cc[vi][vj] != 0) return cc[vi][vj];
  if (color[vi][vj] != 0) throw 1;
  color[vi][vj] = 1;
  //cerr << vi << " " << vj << " " << g[0][0] << endl;
  char cell = g[vi][vj];

  PI nxt;
  int ni, nj;
  if (cell == '^') {
    nxt = findNext(vi - 1, vj, -1, 0);
  } else if (cell == 'v') {
    nxt = findNext(vi + 1, vj, +1, 0);
  } else if (cell == '<') {
    nxt = findNext(vi, vj - 1, 0, -1);
  } else if (cell == '>') {
    nxt = findNext(vi, vj + 1, 0, +1);
  } else {
    //cerr << "here" << endl;
    throw 1;
  }

  ni = nxt.first;
  nj = nxt.second;

  int ret = 2;
  if (ni != -1) {
    conn[vi][vj].push_back(nxt);
    conn[ni][nj].push_back(PI(vi, vj));
    if (color[ni][nj] == 0) {
      ret = go(ni, nj);
    } else if (color[ni][nj] == 1 || cc[ni][nj] == 1) {
      ret = 1;
    }
  }
  //if (ret == 2) cerr << vi << " " << vj << endl;

  color[vi][vj] = 2;
  return cc[vi][vj] = ret;
}

int dfs(int vi, int vj) {
  int ret = 1;
  cc[vi][vj] = 3;
  for (auto val : conn[vi][vj]) {
    int ni = val.first;
    int nj = val.second;
    if (cc[ni][nj] != 2 && cc[ni][nj] != 3) throw 1;
    if (cc[ni][nj] == 2) {
      ret += dfs(ni, nj);
    }
  }
  return ret;
}

int solve() {
  if (n == 1 && m == 1) return g[0][0] == '.' ? 0 : -1;
  memset(color, 0, sizeof(color));
  memset(cc, 0, sizeof(cc));
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      conn[i][j].clear();

  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      if (color[i][j] == 1) throw 1;
      if (g[i][j] == '.' || color[i][j] == 2) continue;
      go(i, j);
    }

  int ret = 0;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      if (cc[i][j] != 2) continue;
      int total = dfs(i, j);
      if (total == 1) {
        bool foundAny = false;
        for (int k = 0; k < n; k++) if (g[k][j] != '.' && k != i) { foundAny = true; break; }
        for (int k = 0; k < m; k++) if (g[i][k] != '.' && k != j) { foundAny = true; break; }
        if (!foundAny) return -1;
      }
      ret++;
    }

  return ret;
}

void solveCase(int tc) {
  memset(g, 0, sizeof(g));
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    for (int j = 0; j < m; j++) g[i][j] = s[j];
  }
  int answer = solve();
  if (answer == -1) {
    cerr << "Case #" << (tc + 1) << ": "
         << "IMPOSSIBLE" << endl;
    cout << "Case #" << (tc + 1) << ": "
         << "IMPOSSIBLE" << endl;
  } else {
    cerr << "Case #" << (tc + 1) << ": " << answer << endl;
    cout << "Case #" << (tc + 1) << ": " << answer << endl;
  }
}

void initialize() {}

int main() {
  freopen(NAME ".in", "rt", stdin);
  freopen(NAME ".out", "wt", stdout);
  int T;
  cin >> T;
  initialize();
  for (int i = 0; i < T; i++) {
    solveCase(i);
  }
  double totalTime = clock() * 1. / CLOCKS_PER_SEC;
  fprintf(stderr, "Time: %.2lf sec\n", totalTime);
  return 0;
}
