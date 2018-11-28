#include <iostream>
#include <vector>
using namespace std;

int incf[] = {0, 0, 1, -1};
int incc[] = {1, -1, 0, 0};

int direction(char c) {
  if (c == '>') return 0;
  if (c == '<') return 1;
  if (c == 'v') return 2;
  return 3;
}

bool check(int d, int i, int j, vector<string>& M) {
  int ni = i + incf[d], nj = j + incc[d];
  bool ok = false;
  while (ni < M.size() and ni >= 0 and nj < M[0].size() and nj >= 0 and not ok) {
    if (M[ni][nj] != '.') {
      ok = true;
    }
    ni += incf[d];
    nj += incc[d];
  }

  return ok;
}

void solve() {
  int n, m;
  cin >> n >> m;
  vector<string> M(n);
  for (int i = 0; i < n; ++i) cin >> M[i];

  int res = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (M[i][j] == '.') continue;

      int d = direction(M[i][j]);
      bool ok = check(d, i, j, M);

      if (not ok) {
        for (int d = 0; d < 4 and not ok; ++d) {
          if (check(d, i, j, M)) ok = true;
        }

        if (not ok) {
          cout << "IMPOSSIBLE" << endl;
          return;
        }
        else ++res;
      }
    }
  }

  cout << res << endl;
}

int main() {
  int casos;
  cin >> casos;
  for (int cas = 1; cas <= casos; ++cas) {
    cout << "Case #" << cas << ": ";
    solve();
  }
}
