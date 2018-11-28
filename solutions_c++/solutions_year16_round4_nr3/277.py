#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

#define MAX 35

int f[MAX][MAX];
int perm[MAX];
int pp[MAX];
bool vis[MAX][4];

int r, c;

int numdir = 4;
int dirx[] = {-1, 0, +1, 0};
int diry[] = {0, +1, 0, -1};

void print() {
  for (int i = 0; i < r; ++i) {
    for (int j = 0; j < c; ++j) {
      printf("%c", f[i][j]);
    }
    printf("\n");
  }
}

bool check() {
  for (int i = 1; i <= 2 * (r + c); ++i) {
    int curposx;
    int curposy;
    int curdir;

    if (0 < i && i <= c) {
      curdir = 2;
      curposx = 0;
      curposy = i - 1;
    } else if (c < i && i <= c + r) {
      curdir = 3;
      curposy = c - 1;
      curposx = i - c - 1;
    } else if (c + r < i && i <= c + r + c) {
      curdir = 0;
      curposx = r - 1;
      curposy = c - 1 - (i - (c + r) - 1);
    } else {
      curdir = 1;
      curposy = 0;
      curposx = r - 1 - (i - (c + r + c) - 1);
    }
    memset(vis, false, sizeof(vis));

    do {
      //printf("at (%d, %d) %d\n", curposx, curposy, curdir);
      if (vis[curposx * c + curposy][curdir]) break;
      vis[curposx * c + curposy][curdir] = true;
      if (f[curposx][curposy] == '\\') {
        if (curdir == 1 || curdir == 3) {
          curdir = (curdir + 1) % 4;
        } else {
          curdir = (curdir + 3) % 4;
        }
      } else {
        if (curdir == 0 || curdir == 2) {
          curdir = (curdir + 1) % 4;
        } else {
          curdir = (curdir + 3) % 4;
        }
      }
      curposx += dirx[curdir];
      curposy += diry[curdir];
    } while (0 <= curposx && curposx < r && 0 <= curposy && curposy < c);

    int p = -1;
    if (curposx < 0) {
      p = curposy + 1;
    } else if (curposy >= c) {
      p = curposx + 1 + c;
    } else if (curposx >= r) {
      p = (c - curposy) + c + r;
    } else if (curposy < 0) {
      p = (r - curposx) + c + r + c;
    }
    if (p != pp[i]) {
      //printf("%d != pp[%d] = %d\n", p, i, pp[i]);
      //printf("(%d, %d)\n", curposx, curposy);
      //print();
      return false;
    }
  }
  return true;
}

bool solve() {
  for (int i = 0; i < (1 << (r * c)); ++i) {
    for (int j = 0; j < r * c; ++j) {
      if (i & (1 << j)) {
        f[j / c][j % c] = '\\';
      } else {
        f[j / c][j % c] = '/';
      }
    }
    if (check()) {
      return true;
    }
  }
  return false;
}

int main() {
  ios::sync_with_stdio(0);
  int t;
  cin >> t;
  for (int cn = 1; cn <= t; cn++) {
    cin >> r >> c;

    for (int i = 0; i < 2 * (r + c); ++i) {
      cin >> perm[i];
    }

    for (int i = 0; i < 2 * (r + c); i += 2) {
      pp[perm[i]] = perm[i + 1];
      pp[perm[i + 1]] = perm[i];
    }

    printf("Case #%d:\n", cn);
    if (!solve()) {
      printf("IMPOSSIBLE\n");
    } else {
      print();
    }
  }
  return 0;
}
