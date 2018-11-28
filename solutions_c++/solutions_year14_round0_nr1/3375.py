#include <cstdio>
#include <cstring>

bool once[32];

int main()
{
  int T, t = 1, r, i, j, x;
  int res;

  for(scanf("%d", &T); T; --T) {
    res = 0;
    memset(once, 0, sizeof(once));
    scanf("%d", &r);
    --r;
    for (i = 0; i < 4; ++i)
    for (j = 0; j < 4; ++j) {
      scanf("%d", &x);
      --x;
      if (i == r)
        once[x] = true;
    }
    scanf("%d", &r);
    --r;
    for (i = 0; i < 4; ++i)
    for (j = 0; j < 4; ++j) {
      scanf("%d", &x);
      --x;
      if ((i == r) && once[x]) {
        if (res)
          res = -1;
        else
          res = x+1;
      }
    }

    printf("Case #%d: ", t++);
    if (res > 0)
      printf("%d\n", res);
    else if (res == -1)
      printf("Bad magician!\n");
    else
      printf("Volunteer cheated!\n");
  }

  return 0;
}
