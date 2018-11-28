#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <set>
#include <queue>
#include <cmath>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <ctime>
#include <algorithm>

using namespace std;

const int MAX_N = 110;

char board[MAX_N][MAX_N];

typedef pair<int, int> Point;

vector<int> graph[MAX_N * MAX_N];

int flags[MAX_N][MAX_N];
int r, c;

int Dfs(int i, int j, bool& close) {
  if (flags[i][j] == 1) {
    close = true;
    return 0;
  }
  flags[i][j] = 1;
  if (board[i][j] == '^') {
    for (int m = i - 1; m >= 0; --m) {
      if (board[m][j] == '^' || board[m][j] == 'v'
          || board[m][j] == '<' || board[m][j] == '>') {
        return Dfs(m, j, close) + 1;
      }
    }
    return 1;
  }
  
  if (board[i][j] == 'v') {
    for (int m = i + 1; m < r; ++m) {
      if (board[m][j] == '^' || board[m][j] == 'v'
          || board[m][j] == '<' || board[m][j] == '>') {
        return Dfs(m, j, close) + 1;
        break;
      }
    }
    return 1;
  }
  
  if (board[i][j] == '>') {
    for (int m = j + 1; m < c; ++m) {
      if (board[i][m] == '^' || board[i][m] == 'v'
          || board[i][m] == '<' || board[i][m] == '>') {
        return Dfs(i, m, close) + 1;
        break;
      }
    }
    return 1;
  }
  
  if (board[i][j] == '<') {
    for (int m = j - 1; m >= 0; --m) {
      if (board[i][m] == '^' || board[i][m] == 'v'
          || board[i][m] == '<' || board[i][m] == '>') {
        return Dfs(i, m, close) + 1;
        break;
      }
    }
    return 1;
  }
  return 1;
}

char dire[4] = {'^', 'v', '<', '>'};

int Process() {
  memset(flags, 0, sizeof(flags));
  int res = 0;
  for (int j = 0; j < r; ++j) {
    for (int k = 0; k < c; ++k) {
      if (board[j][k] == '^' || board[j][k] == 'v'
          || board[j][k] == '<' || board[j][k] == '>') {
 //       cout << j << "===" << k << endl;
        if (flags[j][k] == 1) {
          continue;
        }
        bool closed = false;
        int size = Dfs(j, k, closed);
     //   cout << size << "===" << closed << endl;
        if (closed) {
          continue;
        }
        if (!closed && size > 1) {
          ++res;
          continue;
        }
     //   cout << "====" << endl;
        if (!closed && size == 1) {
          for (int p = 0; p < 4; ++p) {
            flags[j][k] = 0;
            board[j][k] = dire[p];
            closed = false;
            int size = Dfs(j, k, closed);
            if (closed) {
              ++res;
              break;
            }
            if (!closed && size > 1) {
              res += 2;
              break;
            }
            if (p == 3) {
              return -1;
            }
          }
        }
      }
    }
  }
  return res;
}

int main() {
  freopen("//Users//zxj//Desktop//poj_input.txt", "r", stdin);
  int cases;
  scanf("%d", &cases);
  for (int i = 0; i < cases; ++i) {
    scanf("%d %d", &r, &c);
    for (int j = 0; j < r; ++j) {
      scanf("%s", board[j]);
    }
   // cout << "===="  << endl;
    int res = Process();
    if (res == -1) {
      printf("Case #%d: IMPOSSIBLE\n", i + 1);
    } else {
      printf("Case #%d: %d\n", i + 1, res);
    }
  }
}
