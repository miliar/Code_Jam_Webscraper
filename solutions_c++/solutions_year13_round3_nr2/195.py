#include <cstdio>
#include <cstring>

const int MAX_COORD = 200 + 5;
const int MAX_JUMP = 500 + 5;

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, -1, 0, 1};
const char label[] = {'W', 'S', 'E', 'N'};
int pos[256];

int dp[MAX_COORD][MAX_COORD][MAX_JUMP];
char bp[MAX_COORD][MAX_COORD][MAX_JUMP];
int rec(int x, int y, int jump) {
//  printf("%d %d %d\n", x, y, jump);
  if (x == 100 && y == 100) {
    return 0;
  }
  if (x < 0 || x >= MAX_COORD || y < 0 || y >= MAX_COORD || jump >= MAX_JUMP) {
    return 10000;
  }
  int& ret = dp[x][y][jump];
  if (ret != -1) {
    return ret;
  }
  ret = 10000;
  char& next = bp[x][y][jump];
  for (int i = 0; i < 4; ++i) {
    int cur = rec(x + jump * dx[i], y + jump * dy[i], jump + 1) + 1;
    if (cur < ret) {
      ret = cur;
      next = label[i];
    }
  }
  return ret;
}

int main() {
  pos['W'] = 0;
  pos['S'] = 1;
  pos['E'] = 2;
  pos['N'] = 3;
  memset(dp, -1, sizeof(dp));
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    int x, y;
    scanf("%d %d", &x, &y);
    x += 100;
    y += 100;
    int res = rec(x, y, 1);
    if (res >= 10000) {
      fprintf(stderr, "This should not happen!! Test case %d\n", t + 1);
    } else {
      printf("Case #%d: ", t + 1);
      int jump = 1;
      while (x != 100 || y != 100) {
        char label = bp[x][y][jump];
        printf("%c", ::label[pos[label] + 2 & 3]);
        x += jump * dx[pos[label]];
        y += jump * dy[pos[label]];
        ++jump;
      }
      printf("\n");
    }
  }
}
