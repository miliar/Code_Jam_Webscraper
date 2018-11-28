#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int dx[8] = {1, 1, 0, -1, -1, -1, 0, 1};
const int dy[8] = {0, -1, -1, -1, 0, 1, 1, 1};

map<pair<pair<int, int>, int>, vector<string> > ans;

void subsolve(int r, int c, int R, int C, vector<string>& ff)
{
  if (ff[r][c] != '.')
    return;

  int mine = 0;
  for (int d = 0; d < 8; ++d) {
    int rr = r + dy[d];
    int cc = c + dx[d];
    if (rr < 0 || rr >= R || cc < 0 || cc >= C)
      continue;
    if (ff[rr][cc] == '*')
      ++mine;
  }
  
  ff[r][c] = ('0' + mine);

  if (mine == 0) {
    for (int d = 0; d < 8; ++d) {
      int rr = r + dy[d];
      int cc = c + dx[d];
      if (rr < 0 || rr >= R || cc < 0 || cc >= C)
        continue;
      if (ff[rr][cc] == '.')
        subsolve(rr, cc, R, C, ff);
    }
  }
}

void solve(int R, int C, int M)
{
  for (int bit = 0; bit < (1 << (R*C)); ++bit) {
    if (__builtin_popcount(bit) != M)
      continue;

    vector<string> f(R, string(C, '.'));
    for (int i = 0; i < R*C; ++i) {
      if (bit & (1 << i)) {
        f[i/C][i%C] = '*';
      }
    }

    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        if (f[i][j] != '.')
          continue;
        vector<string> ff = f;
        subsolve(i, j, R, C, ff);
        int cnt = 0;
        for (int k = 0; k < R; ++k)
          cnt += count(ff[k].begin(), ff[k].end(), '.');
        if (cnt == 0) {
          f[i][j] = 'c';
          ans[make_pair(make_pair(R, C), M)] = f;
          return;
        }
      }
    }
  }
}

int main()
{
  for (int R = 1; R <= 5; ++R) {
    for (int C = 1; C <= 5; ++C) {
      for (int M = 0; M < R*C; ++M) {
        solve(R, C, M);
      }
    }
  }

  int T;
  cin >> T;
  for (int testcase = 1; testcase <= T; ++testcase) {
    int R, C, M;
    cin >> R >> C >> M;

    cout << "Case #" << testcase << ":" << endl;
    if (ans.find(make_pair(make_pair(R, C), M)) != ans.end()) {
      for (int i = 0; i < R; ++i)
        cout << ans[make_pair(make_pair(R, C), M)][i] << endl;
    } else {
      cout << "Impossible" << endl;
    }
  }

  return 0;
}
