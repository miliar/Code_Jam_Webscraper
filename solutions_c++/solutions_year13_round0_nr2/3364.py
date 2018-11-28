#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 105;
int height[MaxN][MaxN];
int mx_row[MaxN], mx_col[MaxN];
int r, c;

bool sol() {
  for (int i = 0; i < r; ++i)
    for (int j = 0; j < c; ++j)
      if (min(mx_row[i], mx_col[j]) != height[i][j])
        return false;
  return true;
}

int main() {
  int T;

  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);
  
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    scanf("%d%d", &r, &c);
    fill(mx_row, mx_row + r, -1);
    fill(mx_col, mx_col + c, -1);
    for (int i = 0; i < r; ++i)
      for (int j = 0; j < c; ++j) {
        scanf("%d", &height[i][j]);
        mx_row[i] = max(mx_row[i], height[i][j]);
        mx_col[j] = max(mx_col[j], height[i][j]);
      }
    printf("Case #%d: %s\n", cas, sol() ? "YES" : "NO");
  }

  return 0;
}

