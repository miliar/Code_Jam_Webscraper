#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <iostream>
#include <cassert>
using namespace std;

int n, m;
bool row[200];
int used[200][2];
int x[100][100];
int in[200][100];
int mark[200];

inline bool checkrow(int r, int t, int N) {
  if (r == 0) return true;
  for (int j = 0; j < r; ++j) {
    if (x[r][j] != -2 && x[r][j] != in[t][j]) {
      return false;
    }
  }
  for (int j = 0; j < N; ++j) {
    if (x[r-1][j] != -2 && x[r-1][j] >= in[t][j]) {
      return false;
    }
  }
  return true;
}

inline bool checkrow2(int r, int t, int N) {
  for (int j = 0; j <= r; ++j) {
    if (x[r][j] != -2 && x[r][j] != in[t][j]) {
      return false;
    }
  }
  if (r == 0) return true;
  for (int j = 0; j < N; ++j) {
    if (x[r-1][j] != -2 && x[r-1][j] >= in[t][j]) {
      return false;
    }
  }
  return true;
}

inline bool checkcol2(int c, int t, int N) {
  for (int j = 0; j <= c; ++j) {
    if (x[j][c] != -2 && x[j][c] != in[t][j]) {
      return false;
    }
  }
  if (c == 0) return true;
  for (int j = 0; j < N; ++j) {
    if (x[j][c-1] != -2 && x[j][c-1] >= in[t][j]) {
      return false;
    }
  }
  return true;
}

inline bool checkcol(int c, int t, int N) {
  if (c == 0) return true;
  for (int j = 0; j < c; ++j) {
    if (x[j][c] != -2 && x[j][c] != in[t][j]) {
      return false;
    }
  }
  for (int j = 0; j < N; ++j) {
    if (x[j][c-1] != -2 && x[j][c-1] >= in[t][j]) {
      return false;
    }
  }
  return true;
}

bool dfs(int cur, int N) {
  if (cur == N) return true;
  row[cur] = true;
  
  if (checkrow(cur, used[cur][0], N)) {
    for (int j = 0; j < N; ++j) {
        x[cur][j] = in[used[cur][0]][j];
        // printf("%d %d %d\n", cur, j, x[cur][j]);
      }
    if (used[cur][1] == 2*N-1 || checkcol2(cur, used[cur][1], N)) {
      // printf("Set Row %d Col %d\n", used[cur][0], used[cur][1]);
      
      if (used[cur][1] != 2*N-1)
      for (int j = 0; j < N; ++j) {
        x[j][cur] = in[used[cur][1]][j];
      }
      if (dfs(cur+1, N)) return true;
      for (int j = cur; j < N; ++j) {
        x[j][cur] = -2;
        // printf("%d %d %d\n", cur, j, x[cur][j]);
      }
    }
    for (int j = cur; j < N; ++j) {
        x[cur][j] = -2;
        // printf("%d %d %d\n", cur, j, x[cur][j]);
      }
  }

  row[cur] = false;

  if (checkcol(cur, used[cur][0], N)) {
    for (int j = 0; j < N; ++j) {
        x[j][cur] = in[used[cur][0]][j];
      }
    if (used[cur][1] == 2*N-1 || checkrow2(cur, used[cur][1], N)) {
      // printf("Set Col %d Row %d\n", used[cur][0], used[cur][1]);
      
      if (used[cur][1] != 2*N-1)
      for (int j = 0; j < N; ++j) {
        x[cur][j] = in[used[cur][1]][j];
      }
      if (dfs(cur+1, N)) return true;
      for (int j = cur; j < N; ++j) {
        x[cur][j] = -2;
        // printf("%d %d %d\n", cur, j, x[cur][j]);
      }
    }
    for (int j = cur; j < N; ++j) {
        x[j][cur] = -2;
        // printf("%d %d %d\n", cur, j, x[cur][j]);
      }
  }
  return false;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int I = 1; I <= T; ++I) {
    scanf("%d", &n);
    for (int i = 0; i < 2 * n - 1; ++i) {
      for (int j = 0; j < n; ++j) {
        scanf("%d", &in[i][j]);
        mark[i] = -1;
      }
    }
    mark[2 * n - 1] = -1;
    for (int i = 0; i < n ; ++i) {
      int mi1 = 5000, mi2 = 5000;
      int index1 = -1, index2 = -1;  
      for (int j = 0; j < 2 * n -1; ++j) {
        if (mark[j] != -1) continue;
        if (index2 == -1 || in[j][i] <= mi2) {
          if (index1 == -1 || in[j][i] <= mi1) {
            mi2 = mi1;
            index2 = index1;
            mi1 = in[j][i];
            index1 = j;
          } else {
            mi2 = in[j][i];
            index2 = j;
          }
        }
      }
      assert(index1 != -1);
        mark[index1] = i;
        // printf("$ %d %d\n", index1, i);
        if (index2 == -1 || mi1 != mi2) {
          mark[2 * n - 1] = i;
          // printf("$ %d %d\n", 2 * n - 1, i);
        } else {
          mark[index2] = i;
          // printf("$ %d %d\n", index2, i);
        }
    }
    for (int i = 0; i < n ; ++i) {
      int t;
      for (t = 0; t < 2 * n -1; ++t) if (mark[t] == i) break;
      used[i][0] = t;
      for (++t; t < 2 * n -1; ++t) if (mark[t] == i) break;
      used[i][1] = t;
      
      for (int j = 0; j < n ; ++j) {
        x[i][j] = -2;
      }
    }
    assert(dfs(0, n));

    // for (int i = 0; i < n ; ++i) {
    //   for (int j = 0; j < n ; ++j) {
    //     printf(" %d", x[i][j]);
    //   }
    //   printf("\n");
    // }

    printf("Case #%d:", I);
    // for (int i = 0; i < 2 * n -1 ; ++i) {
    //   for (int j = 0; j < n ; ++j) {
    //     printf(" %d", in[i][j]);
    //   }
    //   printf("\n");
    // }

    if (!row[mark[2*n - 1]]) for (int j = 0; j < n; ++j) printf(" %d", x[mark[2*n - 1]][j]);
    else for (int j = 0; j < n; ++j) printf(" %d", x[j][mark[2*n - 1]]);
    printf("\n");
  }
}