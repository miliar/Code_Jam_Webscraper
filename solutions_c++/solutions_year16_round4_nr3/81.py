#include <iostream>
using namespace std;

int R, C;
int pairing[100];
char grid[100][100];
bool visited[100][100][4];

/*
  0
3 \/ 1
  /\
  2
*/

bool tooMany, found;
int req;

#define dprintf(...) 0;

void dfs(int r, int c, int q, bool first = false) {
  if (visited[r][c][q] || tooMany) {
    return;
  }
  dprintf("f:%d r:%d c:%d q:%d\n", first, r, c, q);
  visited[r][c][q] = true;
  #define REG(x) \
    dprintf("reg: %d\n", x);\
    if ((x) == req) {\
      found = true;\
    } else {\
      tooMany = true;\
    }\
    dprintf("found:%d tooMany:%d\n", found, tooMany);\
    return;\

  if (!first) {
    if (q == 0 && r == 0) {
      REG(c);
    } else if (q == 1 && c == C-1) {
      REG(r+C);
    } else if (q == 2 && r == R-1) {
      REG(2*C+R-1-c);
    } else if (q == 3 && c == 0) {
      REG(2*R+2*C-1-r);
    }
  }

  #define SWITCH(a,b) \
    if (q == a) dfs(r, c, b);\
    else if (q == b) dfs(r, c, a);

  if (grid[r][c] == '/') {
    SWITCH(1, 2);
    SWITCH(0, 3);
  } else {
    SWITCH(0, 1);
    SWITCH(2, 3);
  }

  if (q == 0 && r > 0) dfs(r-1, c, 2);
  else if (q == 1 && c+1 < C) dfs(r, c+1, 3);
  else if (q == 2 && r+1 < R) dfs(r+1, c, 0);
  else if (q == 3 && c > 0) dfs(r, c-1, 1);
}

bool explore(int r, int c, int q, int _req) {
  dprintf("seeking:%d\n", _req);
  tooMany = false; found = false;
  req = _req;
  dfs(r, c, q, true);
  return !tooMany && found;
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> R >> C;
    for (int i = 0; i < R+C; i++) {
      int a, b; cin >> a >> b;
      pairing[a-1] = b-1;
      pairing[b-1] = a-1;
    }

    printf("Case #%d:\n", t);
    bool done = false;
    memset(grid, 0, sizeof grid);
    for (int mask = 0; mask < (1<<(R*C)); mask++) {
      for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
          if (mask & (1<<(i*C+j))) {
            grid[i][j] = '/';
          } else {
            grid[i][j] = '\\';
          }

      memset(visited, 0, sizeof visited);
      for (int i = 0; i < C; i++) {
        if (!visited[0][i][0]) {
          if (!explore(0, i, 0, pairing[i])) {
            goto fail;
          }
        }
        if (!visited[R-1][i][2]) {
          if (!explore(R-1, i, 2, pairing[2*C+R-1-i])) {
            goto fail;
          }
        }
      }
      for (int i = 0; i < R; i++) {
        if (!visited[i][0][3]) {
          if (!explore(i, 0, 3, pairing[2*R+2*C-1-i])) {
            goto fail;
          }
        }
        if (!visited[i][C-1][1]) {
          if (!explore(i, C-1, 1, pairing[C+i])) {
            goto fail;
          }
        }
      }

      for (int i = 0; i < R; i++) {
        cout << grid[i] << endl;
      }

      done = true;
      break;
      fail:;
    }

    if (!done) {
      puts("IMPOSSIBLE");
    }
  }
}
