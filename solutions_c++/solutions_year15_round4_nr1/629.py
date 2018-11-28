#include <bits/stdc++.h>

using namespace std;

#define MAXN 110
int r, c;
char T[MAXN][MAXN];

typedef pair<int, int> pii;
map<char, pii> mv = {
  {'^', {-1, 0}},
  {'v', {1, 0}},
  {'>', {0, 1}},
  {'<', {0, -1}},
};

bool valid(int x, int y) {
  return x >= 0 and x < r and y >= 0 and y < c;
}

bool move(int x, int y, char s) {
  pii m = mv[s];
  do {
    x += m.first;
    y += m.second;
  } while (valid(x, y) and T[x][y] == '.');
  return valid(x, y);
}

int solve() {
  cin >> r >> c;
  for (int i = 0; i < r; ++i)
    cin >> T[i];
  int ans = 0;
  char s[] = "^v<>";
  for (int i = 0; i < r; ++i)
    for (int j = 0; j < c; ++j)
      if (T[i][j] != '.' and not move(i, j, T[i][j])) {
        ++ans;
        bool found = false;
        for (int k = 0; k < 4; ++k)
          found |= move(i, j, s[k]);
        if (not found)
          return -1;
      }
  return ans;
}

int main() {
  ios::sync_with_stdio(0);
  int tc;
  cin >> tc;
  for (int cs = 1; cs <= tc; ++cs) {
    cout << "Case #" << cs << ": ";
    int ans = solve();
    if (ans >= 0)
      cout << ans;
    else
      cout << "IMPOSSIBLE";
    cout << endl;
  }
  return 0;
}

