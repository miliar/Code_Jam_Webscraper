#include <cstdio>
#include <cstring>

int res[1024];
int q[1024];

int rev(int x, int k) {
  int r = 0;
  while (k--) {
    r <<= 1;
    r |= !(x & (1 << k));
  }
  return r;
}

int main() {

  res[0] = 1;
  int t = 1;
  for (int i = 0; i < 1024; i++) {
    const int v = q[i];
    int w = v;
    int z = 0;
    for (int k = 0; k < 10; k++) {
      w >>= 1;
      z |= v & (1 << k);
      int x = (w << (k + 1)) | rev(z, k+1);
      //printf("i %d, v %d, k %d, x %d, r %d\n", i, v, k, x, res[x]);
      if (res[x])
        continue;
      res[x] = res[v] + 1;
      q[t++] = x;
    }
  }

  int T;
  scanf("%d\n", &T);
  char lin[15];

  for (int t = 1; t <= T; t++) {
    scanf("%s", lin);
    int n = 0;
    for (int i = strlen(lin) - 1; i >= 0; i--) {
      n <<= 1;
      if (lin[i] == '-')
        n |= 1;
    }
    printf("Case #%d: %d\n", t, res[n] - 1);
  }

  return 0;
}
