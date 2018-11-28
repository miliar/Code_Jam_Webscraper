#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <vector>
using namespace std;

vector<vector<int> > vec;
int grid[100][100];
int n;
bool done;

// miss 0, 1:row 2:col
void dfs(int now, int nxt_row, int nxt_col, int miss, int miss_id) {
  if (done) return;

  // printf("===\n");
  // printf("%d %d %d %d %d\n", now, nxt_row, nxt_col, miss, miss_id);
  // for (int i = 0; i < n; i++) {
  //   for (int j = 0; j < n; j++) {
  //     printf("%d ", grid[i][j]);
  //   }
  //   printf("\n");
  // }
  // printf("===\n");

  if (now == 2 * n - 1) {
    done = true;
    if (miss == 0) {
      if (nxt_row == n) {
        miss = 2;
        miss_id = nxt_col;
      }
      if (nxt_col == n) {
        miss = 1;
        miss_id = nxt_row;
      }
    }
    if (miss == 1) {
      // miss row
      for (int i = 0; i < n; i++) {
        printf("%d ", grid[miss_id][i]);
      }
    }
    if (miss == 2) {
      // miss row
      for (int i = 0; i < n; i++) {
        printf("%d ", grid[i][miss_id]);
      }
    }
    printf("\n");
    return;
  }
  bool flag;
  // put new row
  // check row
  flag = true;
  if (nxt_row != n) {
    int last_row = nxt_row - 1;
    if (miss == 1 && miss_id == last_row) {
      last_row--;
    }
    if (last_row >= 0) {
      for (int i = 0; i < n; i++) {
        if (vec[now][i] <= grid[last_row][i]) {
          flag = false;
          break;
        }
      }
    }
    if (flag) {
      for (int i = 0; i < nxt_col ; i++) {
        if ((miss != 2 || miss_id != i) && vec[now][i] != grid[nxt_row][i]) {
          flag = false;
          break;
        }
      }
    }
    if (flag) {
      // printf("a===\n");
      // printf("%d %d %d %d %d\n", now, nxt_row, nxt_col, miss, miss_id);
      // for (int i = 0; i < n; i++) {
      //   for (int j = 0; j < n; j++) {
      //     printf("%d ", grid[i][j]);
      //   }
      //   printf("\n");
      // }
      // printf("===\n");
      for (int i = 0; i < n; i++) {
        grid[nxt_row][i] = vec[now][i];
      }

      dfs(now + 1, nxt_row + 1, nxt_col, miss, miss_id);
    }
  }
  // put new row (skip one)
  // check row
  flag = true;
  if (miss == 0 && nxt_row + 1 != n) {
    int last_row = nxt_row - 1;
    if (last_row >= 0) {
      for (int i = 0; i < n; i++) {
        if (vec[now][i] <= grid[last_row][i]) {
          flag = false;
          break;
        }
      }
    }
    if (flag) {
      for (int i = 0; i < nxt_col; i++) {
        if ((miss != 2 || miss_id != i) &&
            vec[now][i] != grid[nxt_row + 1][i]) {
          flag = false;
          break;
        }
      }
    }
    if (flag) {
      // printf("a===\n");
      // printf("%d %d %d %d %d\n", now, nxt_row, nxt_col, miss, miss_id);
      // for (int i = 0; i < n; i++) {
      //   for (int j = 0; j < n; j++) {
      //     printf("%d ", grid[i][j]);
      //   }
      //   printf("\n");
      // }
      // printf("===\n");
      for (int i = 0; i < n; i++) {
        grid[nxt_row + 1][i] = vec[now][i];
      }
      dfs(now + 1, nxt_row + 2, nxt_col, 1, nxt_row);
    }
  }
  // put new column
  // check column
  flag = true;
  if (nxt_col != n) {
    int last_col = nxt_col - 1;
    if (miss == 2 && miss_id == last_col) {
      last_col--;
    }
    if (last_col >= 0) {
      for (int i = 0; i < n; i++) {
        if (vec[now][i] <= grid[i][last_col]) {
          flag = false;
          break;
        }
      }
    }
    if (flag) {
      for (int i = 0; i < nxt_row; i++) {
        if ((miss != 1 || miss_id != i) && vec[now][i] != grid[i][nxt_col]) {
          flag = false;
          break;
        }
      }
    }
    if (flag) {
      // printf("a===\n");
      // printf("%d %d %d %d %d\n", now, nxt_row, nxt_col, miss, miss_id);
      // for (int i = 0; i < n; i++) {
      //   for (int j = 0; j < n; j++) {
      //     printf("%d ", grid[i][j]);
      //   }
      //   printf("\n");
      // }
      // printf("===\n");
      for (int i = 0; i < n; i++) {
        grid[i][nxt_col] = vec[now][i];
      }
      dfs(now + 1, nxt_row, nxt_col + 1, miss, miss_id);
    }
  }
  // put new col (skip one)
  // check col
  flag = true;
  if (miss == 0 && nxt_col + 1 != n) {
    int last_col = nxt_col - 1;
    if (last_col >= 0) {
      for (int i = 0; i < n; i++) {
        if (vec[now][i] <= grid[i][last_col]) {
          flag = false;
          break;
        }
      }
    }
    if (flag) {
      for (int i = 0; i < nxt_row ; i++) {
        if ((miss != 1 || miss_id != i) &&
            vec[now][i] != grid[i][nxt_col + 1]) {
          flag = false;
          break;
        }
      }
    }
    if (flag) {
      for (int i = 0; i < n; i++) {
        grid[i][nxt_col + 1] = vec[now][i];
      }
      dfs(now + 1, nxt_row, nxt_col + 2, 2, nxt_col);
    }
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int cs = 1; cs <= T; cs++) {
    scanf("%d", &n);
    vec.resize(2 * n - 1);
    for (int i = 0; i < 2 * n - 1; i++) {
      vec[i].resize(n);
      for (int j = 0; j < n; j++) {
        scanf("%d", &(vec[i][j]));
      }
    }
    // if (cs!=49) continue;

    sort(vec.begin(), vec.end(),
         [](const vector<int> &a, const vector<int> &b) {
      // for (size_t i = 0; i < a.size(); i++) {
      //   if (a[i] < b[i]) return true;
      // }
           if (a[0]<b[0])return true;
      return false;
    });

    // printf("===\n");
    // for (int i = 0; i < 2*n-1; i++) {
    //   for (int j = 0; j < n; j++) {
    //     printf("%d ", vec[i][j]);
    //   }
    //   printf("\n");
    // }
    // printf("===\n");

    printf("Case #%d: ", cs);

    for (int i = 0; i < n; i++) {
      grid[0][i] = vec[0][i];
    }
    done = false;
    dfs(1, 1, 0, 0, -1);
    if (!done) {
      for (int i = 0; i < n; i++) {
        grid[1][i] = vec[0][i];
      }
      dfs(1, 2, 0, 1, 0);
    }
    if (!done) {
      for (int i = 0; i < n; i++) {
        grid[i][0] = vec[0][i];
      }
      dfs(1, 0, 1, 0, -1);
      if (!done) {
        for (int i = 0; i < n; i++) {
          grid[i][1] = vec[0][i];
        }
        dfs(1, 0, 2, 2, 0);
      }
    }
  }
  return 0;
}
