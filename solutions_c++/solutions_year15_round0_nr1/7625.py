#include <cstdio>
#include <cstring>

int N, Smax;
char sir[1200];

int main() {
  freopen("ovation.in", "r", stdin);
  freopen("ovation.out", "w", stdout);

  scanf("%d\n", &N);

  for (int test = 1; test <= N; ++test) {
    scanf("%d %s", &Smax, sir);

    int i = 0;
    int no = 0;
    int result = 0;
    for (int j = 0, l = Smax+1; j < l; ++i, ++j) {
      int v = sir[j] - '0';

      if (i-no > 0 && v > 0) {
        result += i-no;
        no += i-no;
      }

      no += v;
    }
    printf("Case #%d: %d\n", test, result);
  }

  return 0;
}
