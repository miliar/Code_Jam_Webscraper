#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;

char mines[11][11];
int delta[] = {-1, 0, 1};

bool exists(int i, int j, int r, int c)
{
  if(i >= 0 && i < r && j >= 0 && j < c)
    return true;
  return false;
}

vector<ii> getAdj(int i, int j, int r, int c)
{
  vector<ii> adj;
  for(int k = 0; k < 3; k++)
    for(int l = 0; l < 3; l++)
      if(exists(i + delta[k], j + delta[l], r, c) && mines[i + delta[k]][j + delta[l]] == '*')
        adj.push_back(ii(i + delta[k], j + delta[l]));
  return adj;
}

bool populate(int i, int j, int r, int c, int m)
{
  /*printf("At (%d,%d)\n", i, j, m);
  for(int k = 0; k < r; k++)
  {
    for(int l = 0; l < c; l++)
      printf("%c", mines[k][l]);
    printf("\n");
  }
  getc(stdin);*/
  if(m == 0)
    return true;
  vector<ii> co = getAdj(i, j, r, c);
  if(m - (int)co.size() < 0)
    return false;
  for(int k = 0; k < co.size(); k++)
    mines[co[k].first][co[k].second] = '.';
  for(int k = 0; k < co.size(); k++)
  {
    int newi = co[k].first, newj = co[k].second;
    if(populate(newi, newj, r, c, m - (int)co.size()))
      return true;
  }
  for(int k = 0; k < co.size(); k++)
    mines[co[k].first][co[k].second] = '*';
  return false;
}

void fillWithMines(int r, int c)
{
  for(int i = 0; i < r; i++)
    for(int j = 0; j < c; j++)
      mines[i][j] = '*';
}

int main()
{
  int t;
  int cas = 1;
  scanf("%d", &t);
  while(t--)
  {
    bool worked = false;
    int r,c,m;
    scanf("%d %d %d", &r, &c, &m);
    printf("Case #%d:\n", cas++);
    for(int i = 0; i <= r/2; i++)
    {
      for(int j = 0; j <= c/2; j++)
      {
        fillWithMines(r, c);
        mines[i][j] = 'c';
        if(populate(i, j, r, c, r*c - m - 1))
        {
          worked = true;
          break;
        }
      }
      if(worked)
        break;
    }
    if(!worked)
      printf("Impossible\n");
    else
    {
      for(int i = 0; i < r; i++)
      {
        for(int j = 0; j < c; j++)
          printf("%c", mines[i][j]);
        printf("\n");
      }
    }
  }
  return 0;  
}
