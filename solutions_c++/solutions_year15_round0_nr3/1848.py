#include <cstdio>
#include <algorithm>

const int N = 50000 + 10;

const int mul[5][5] = {{0, 0, 0, 0, 0},
                       {0, 1, 2, 3, 4},
                       {0, 2, -1, 4, -3},
                       {0, 3, -4, -1, 2},
                       {0, 4, 3, -2, -1}};

int MUL(int a, int b) {
  int sgn = (a * b > 0 ? 1 : -1);
  return sgn * mul[std::abs(a)][std::abs(b)];
}

int main() {
  int tcase;
  scanf("%d", &tcase);
  static int trans[N];
  trans['1'] = 1;
  trans['i'] = 2;
  trans['j'] = 3;
  trans['k'] = 4;
  for (int no = 1; no <= tcase; ++no) {
    int l, x;
    static char s[N];
    scanf("%d%d %s", &l, &x, s);
    static int pre[N], suf[N];
    pre[0] = trans[s[0]];
    suf[x * l] = 1;
    for (int i = 1; i < x * l; ++i) pre[i] = MUL(pre[i - 1], trans[s[i % l]]);
    for (int i = x * l - 1; i >= 0; --i) suf[i] = MUL(trans[s[i % l]], suf[i + 1]);
    bool ans = false;
    for (int i = 0; !ans && i < x * l; ++i) {
      if (pre[i] != 2) continue;
      int mid = trans[s[(i + 1) % l]];
      for (int j = i + 2; !ans && j < x * l; ++j) {
        ans |= (mid == 3 && suf[j] == 4);
        mid = MUL(mid, trans[s[j % l]]);
      }
    }
    printf("Case #%d: %s\n", no, ans ? "YES" : "NO");
  }
  return 0;
}
