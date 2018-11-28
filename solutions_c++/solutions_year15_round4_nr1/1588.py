#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int r, c;
char map[400][400];

int id[400][400];
int px[400], py[400];
void init()
{
  cin >> r >> c;
  for(int i=1; i<=r; ++i)
    scanf("%s", &map[i][1]);
  for(int i=0; i<=c+1; ++i)
    map[0][i] = map[r+1][i] = '.';
  for(int i=0; i<=r+1; ++i)
    map[i][0] = map[i][c+1] = '.';
}

int sr[400], sc[400];
void work()
{
  memset(id, 0, sizeof(id));
  int tot = 0;
  for(int j=0; j<=c+1; ++j)
  {
    int i;
    for(i=1; i<=r; ++i)
      if (map[i][j] != '.')
        break;
    if (i <= r && map[i][j] == '^')
    {
      id[i][j] = ++tot;
      px[tot] = i;
      py[tot] = j;
    }
    for(i=r; i>0; --i)
      if (map[i][j] != '.')
        break;
    if (i > 0 && map[i][j] == 'v')
    {
      id[i][j] = ++tot;
      px[tot] = i;
      py[tot] = j;
    }
  }
  for(int i=0; i<=r+1; ++i)
  {
    int j;
    for(j=1; j<=c; ++j)
      if (map[i][j] != '.')
        break;
    if (j <= c && map[i][j] == '<')
    {
      id[i][j] = ++tot;
      px[tot] = i;
      py[tot] = j;
    }
    for(j=c; j>0; --j)
      if (map[i][j] != '.')
        break;
    if (j > 0 && map[i][j] == '>')
    {
      id[i][j] = ++tot;
      px[tot] = i;
      py[tot] = j;
    }
  }
  memset(sr, 0, sizeof(sr));
  memset(sc, 0, sizeof(sc));
  for(int i=1; i<=r; ++i)
  {
    for(int j=1; j<=c; ++j)
      if (map[i][j] != '.')
        ++sr[i];
  }
  for(int j=1; j<=c; ++j)
  {
    for(int i=1; i<=r; ++i)
      if (map[i][j] != '.')
        ++sc[j];
  }
  bool imp = false;
  for(int i=1; i<=r; ++i)
    for(int j=1; j<=c; ++j)
      if (sr[i] == 1 && sc[j] == 1 && map[i][j] != '.')
        imp = true;
  if (imp)
    printf("IMPOSSIBLE\n");
  else
    printf("%d\n", tot);
}

int main()
{
  int T;
  cin >> T;
  for(int i=1; i<=T; ++i)
  {
    init();
    printf("Case #%d: ", i);
    work();
  }
}
