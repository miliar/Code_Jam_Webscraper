#include <cstdio>
#include <algorithm>

using namespace std;

int cfg(int r, int c, int i, int j) {
  return i * c + j;
}

int set_bit(int x, int c) {
  return x & (1<<c);
}

int xx[] = {-1, 0, 1, 0};
int yy[] = {0, 1, 0, -1};

bool ok(int r, int c, int i, int j) {
  return i >= 0 && j >= 0 && i < r && j < c;
}

int compute(int x, int r, int c, int n) {
  int cnt = 0;
  int unhappy = 0;
  
  for (int i = 0; i < r; ++i)
  for (int j = 0; j < c; ++j) {
    int pos = cfg(r, c, i, j);    
    //printf ("%d %d %d %d %d\n", i, j, r, c, pos);

    if (set_bit(x, pos)) {
      //printf ("for %d place %d\n", x, pos);
      ++cnt;
    } else {
      continue;
    }

    for (int k = 0; k < 4; ++k) {
      int ii = i + xx[k];
      int jj = j + yy[k];

      if (!ok(r, c, ii, jj))
        continue;

      int pos2 = cfg(r, c, ii, jj);
      //printf ("ask %d\n", pos2);
      if (set_bit(x, pos2))
        ++unhappy;
    }
  }

  if (cnt != n)
    return 9999999;
  return unhappy / 2;
}

int main() {
  int t, r, c, n;
  scanf("%d", &t);

  for (int i = 1; i <= t; ++i) {
    scanf("%d %d %d", &r, &c, &n);
    
    int res = 999999;
    for (int i = 0; i < (1<<(r * c)); ++i) {
      res = min(res, compute(i, r, c, n));
    }

    printf("Case #%d: %d\n", i, res);
  }
}
