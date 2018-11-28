#include <stdio.h>

int lawn[128][128];
int n, m;

bool isOkay(int x, int y)
{
  bool okayH = true;
  bool okayV = true;
  for(int i(0); i < n; ++i)
  {
    if(i == x)
      continue;

    if(lawn[x][y] < lawn[i][y])
      okayV = false;

    if(okayV == false)
      break;
  }

  for(int i(0); i < m; ++i)
  {
    if(i == y)
      continue;

    if(lawn[x][y] < lawn[x][i])
      okayH = false;

    if(okayH == false)
      break;
  }

  return okayH || okayV;
}

int main(void)
{
  int t;

  scanf("%d", &t);
  for(int r = 0; r < t; ++r)
  {
    scanf("%d %d", &n,&m);

    bool okay = true;

    for(int i(0); i < n; ++i)
    {
      for(int j(0); j < m; ++j)
      {
        scanf("%d",&lawn[i][j]);
      }
    }

    for(int i(0); i < n; ++i)
    {
      for(int j(0); j < m; ++j)
      {
        if(!isOkay(i, j))
          okay = false;

        if(!okay)
          break;
      }
      if(!okay)
        break;
    }

    if(okay)
      printf("Case #%d: YES\n",r+1);
    else
      printf("Case #%d: NO\n",r+1);
  }

  return 0;
}
