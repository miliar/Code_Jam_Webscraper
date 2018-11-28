#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

int W, H, M;
int empty;

void color(vector<vector<int> > &v, int x, int y) {
  if (!empty) return;
  if (x >= W || y >= H) return;
  if (v[y][x]) return;
  empty--;
  v[y][x] = true;
}

bool found = false;
vector<int> locw;

void rec(int y, int sum, int last) {
  if (sum + M > W*H) return;
  if (sum + M == W*H) {
    if (locw[0] != locw[1]) return;
    found = true;
    return;
  }
  if (y == H) return;
  for (int x = last; x >= 2; x--) {
    if (y == 1 && x != last) continue;
    locw[y] = x;
    rec(y + 1, sum + x, x);
    if (found) return;
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    scanf("%d%d%d", &H, &W, &M);

    empty = W*H - M;

    locw.clear();
    locw.assign(H, 0);

    found = false;

    if (empty == 1) {
      found = true;
      locw[0] = 1;
    } else if (H == 1) {
      found = true;
      locw[0] = empty;
    } else if (W == 1) {
      found = true;
      for (int y = 0; y < empty; y++) locw[y] = 1;
    } else {
      rec(0, 0, W);
    }

    printf("Case #%d:\n", tc);

    if (!found) {
      fprintf(stderr, "empty=%d %d,%d,%d\n", empty, H, W, M);
      printf("Impossible\n");
    } else {
      for (int y = 0; y < H; y++) {
        for (int x = 0; x < W; x++) printf("%c", x==0&&y==0 ? 'c' : x < locw[y] ? '.' : '*');
        printf("\n");
      }
    }
  }
}
