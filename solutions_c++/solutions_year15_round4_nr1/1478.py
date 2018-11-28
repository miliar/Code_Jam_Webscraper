#include <bits/stdc++.h>

#define MOD 1000000007

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;
typedef pair<pii, pii> line;

#define F first
#define S second

char pos[] = {'^', '<', '>', 'v'};
char pegs[105][105];
int h, w;
int ans;

int testpeg(int x, int y, char cdir)
{
  int dx = 0, dy = 0;
  if (cdir == 'v')
    dy = 1;
  else if (cdir == '^')
    dy = -1;
  else if (cdir == '<')
    dx = -1;
  else if (cdir == '>')
    dx = 1;

  x += dx;
  y += dy;
  int i = 0;
  while (x >= 0 && x < w && y >= 0 && y < h && pegs[y][x] == '.')
  {
    x += dx;
    y += dy;
  }

  if (!((x >= 0 && x < w && y >= 0 && y < h)))
    return 1;
  return 0;
}

int main()
{
  int i, j, k;
  int t, T, n;
  scanf("%d", &T);

  for (t = 1; t <= T; t++)
  {
    ans = 0;
    int fl = 1;
    scanf("%d %d", &h, &w);

    for (i = 0; i < h; i++)
      scanf(" %s", pegs[i]);

    for (i = 0; i < h; i++)
      for (j = 0; j < w; j++)
        if (pegs[i][j] != '.' && testpeg(j, i, pegs[i][j]))
        {
          ans++;
          int fl2 = 0;
          for (k = 0; k < 4 && !fl2; k++)
            if (!testpeg(j, i, pos[k]))
              fl2 = 1;
          fl = (fl && fl2);
        }

    if (fl)
      printf("Case #%d: %d\n", t, ans);
    else
      printf("Case #%d: IMPOSSIBLE\n", t);
  }
  
  return 0;
}
