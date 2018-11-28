#include <stdio.h>
#include <string.h>

int pos[101][101];
int mat[101][101];

int main()
{
  int t, T, i, j, k;
  scanf("%d", &T);
  for (t = 0; t < T; t++)
  {
    int n, m;
    scanf("%d %d", &n, &m);
    memset(pos, 0, sizeof pos);
    for (i = 0; i < n; i++)
      for (j = 0; j < m; j++)
        scanf("%d", &mat[i][j]);
    for (k = 1; k <= 100; k++)
    {
      for (i = 0; i < n; i++)
      {
        int fl = 1;
        for (j = 0; fl && j < m; j++)
          if (mat[i][j] > k)
            fl = 0;
        for (j = 0; fl && j < m; j++)
          if (mat[i][j] == k)
            pos[i][j] = 1;
      }
      for (j = 0; j < m; j++)
      {
        int fl = 1;
        for (i = 0; fl && i < n; i++)
          if (mat[i][j] > k)
            fl = 0;
        for (i = 0; fl && i < n; i++)
          if (mat[i][j] == k)
            pos[i][j] = 1;
      }
    }

    int fl = 1;
    for (i = 0; i < n; i++)
      for (j = 0; j < m; j++)
        if (!pos[i][j])
          fl = 0;
    if (fl)
      printf("Case #%d: YES\n", t + 1);
    else
      printf("Case #%d: NO\n", t + 1);
  }
  return 0;
}
