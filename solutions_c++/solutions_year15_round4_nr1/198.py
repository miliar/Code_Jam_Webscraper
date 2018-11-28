#include <cstdio>
#include <cstring>
using namespace std;

const int N = 110;
char board[N][N];
int t, r, c, cnt[N][N][4]; // < ^ > v

int main() {
  scanf("%d", &t);
  for (int _ = 1; _ <= t; _++) {
    scanf("%d%d", &r, &c);
    for (int i = 0; i < r; i++)
      scanf("%s", board[i]);
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++) {
        if (j) cnt[i][j][0] = cnt[i][j - 1][0] + (board[i][j - 1] == '.');
        if (i) cnt[i][j][1] = cnt[i - 1][j][1] + (board[i - 1][j] == '.');
      }
    for (int i = r - 1; i >= 0; i--)
      for (int j = c - 1; j >= 0; j--) {
        if (i < r - 1) cnt[i][j][3] = cnt[i + 1][j][3] + (board[i + 1][j] == '.');
        if (j < c - 1) cnt[i][j][2] = cnt[i][j + 1][2] + (board[i][j + 1] == '.');
      }
    bool fg = false;
    for (int i = 0; i < r && !fg; i++)
      for (int j = 0; j < c && !fg; j++)
        if (board[i][j] != '.' && cnt[i][j][0] + cnt[i][j][2] == c - 1 && cnt[i][j][1] + cnt[i][j][3] == r - 1) fg = true;
    printf("Case #%d: ", _);
    if (fg) {
      puts("IMPOSSIBLE");
      continue;
    }
    int ans = 0;
    for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++) {
        switch (board[i][j]) {
        case '<' : if (cnt[i][j][0] == j) ans++; break;
        case '^' : if (cnt[i][j][1] == i) ans++; break;
        case '>' : if (cnt[i][j][2] == c - j - 1) ans++; break;
        case 'v' : if (cnt[i][j][3] == r - i - 1) ans++; break;
        case '.' : break;
        }
      }
    printf("%d\n", ans);
  }
  return 0;
}
