#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <vector>
using namespace std;

bool IsImpossible(int R, int C, const vector<string>& field) {
  for (int i = 0; i < R; ++i) {
    for (int j = 0; j < C; ++j) {
      const char ch = field[i][j];
      if (ch == '.') {
        continue;
      }

      bool fail = true;
      for (int k = 0; k < R; ++k) {
        if (k == i) {
          continue;
        }

        if (field[k][j] != '.') {
          fail = false;
          break;
        }
      }
      for (int k = 0; k < C; ++k) {
        if (k == j) {
          continue;
        }

        if (field[i][k] != '.') {
          fail = false;
          break;
        }
      }

      if (fail) {
        return true;
      }

    }
  }
  return false;
}

void Solve() {
  int R, C;
  cin >> R >> C;

  vector<string> field(R);
  for (string& line : field) {
    cin >> line;
  }

  if (IsImpossible(R, C, field)) {
    cout << "IMPOSSIBLE";
    return;
  }

  int result = 0;

  for (int i = 0; i < R; ++i) {
    bool bad = false;
    for (int j = 0; j < C; ++j) {
      if (field[i][j] != '>') {
        continue;
      }

      bool bad2 = true;
      for (int k = j + 1; k < C; ++k) {
        if (field[i][k] != '.') {
          bad2 = false;
          break;
        }
      }

      if (bad2) {
        bad = true;
      }
    }

    if (bad) {
      ++result;
    }
  }

  for (int i = 0; i < R; ++i) {
    bool bad = false;
    for (int j = 0; j < C; ++j) {
      if (field[i][j] != '<') {
        continue;
      }

      bool bad2 = true;
      for (int k = j - 1; k >= 0; --k) {
        if (field[i][k] != '.') {
          bad2 = false;
          break;
        }
      }

      if (bad2) {
        bad = true;
      }
    }

    if (bad) {
      ++result;
    }
  }

  for (int j = 0; j < C; ++j) {
    bool bad = false;
    for (int i = 0; i < R; ++i) {
      if (field[i][j] != '^') {
        continue;
      }

      bool bad2 = true;
      for (int k = i - 1; k >= 0; --k) {
        if (field[k][j] != '.') {
          bad2 = false;
          break;
        }
      }

      if (bad2) {
        bad = true;
      }
    }

    if (bad) {
      ++result;
    }
  }

  for (int j = 0; j < C; ++j) {
    bool bad = false;
    for (int i = 0; i < R; ++i) {
      if (field[i][j] != 'v') {
        continue;
      }

      bool bad2 = true;
      for (int k = i + 1; k < R; ++k) {
        if (field[k][j] != '.') {
          bad2 = false;
          break;
        }
      }

      if (bad2) {
        bad = true;
      }
    }

    if (bad) {
      ++result;
    }
  }

  cout << result;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/A-large.in", "rb", stdin);
  freopen("../Console/A-large.out", "wb", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    cout << "Case #" << tc + 1 << ": ";
    Solve();
    cout << endl;
  }

  return 0;
}
