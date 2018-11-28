
#include <iostream>
#include <cstdio>
#include <queue>
#include <algorithm>
#include <cstring>
using namespace std;

#define DBG(X)

int plansza[200][200];
int plansza2[200][200];
    int n, m;

class ValueRequest {
  public:
  int p;
  int row;
  int col;
  ValueRequest(int p_, int row_, int col_) {
    p = p_;
    row = row_;
    col = col_;
  }
  bool operator<(const ValueRequest& y) const
  {
    return p < y.p;
  }
};


bool fillToLeft(int row, int col)
{
  int el = plansza[row][col];
  bool ok = true;
  for (int i = m - 1; i >= 0; i--)
  {
    if (el < plansza[row][i])
    {
      ok = false;
    }
  }
  if (ok)
  {
    for (int i = m - 1; i >= 0; i--)
    {
      plansza2[row][i] = el;
    }
  }
  return ok;
}

bool fillToRight(int row, int col)
{
  int el = plansza[row][col];
  bool ok = true;
  for (int i = 0; i < m; i++)
  {
    if (el < plansza[row][i])
    {
      ok = false;
    }
  }
  
  if (ok)
  {
    for (int i = 0; i < m; i++)
    {
      plansza2[row][i] = el;
    }
  }
  return ok;
}

bool fillToUp(int row, int col)
{
  int el = plansza[row][col];
  bool ok = true;
  for (int i = n - 1; i >= 0; i--)
  {
    if (el < plansza[i][col])
    {
      ok = false;
    }
  }
  if (ok)
  {
    for (int i = n - 1; i >= 0; i--)
    {
      plansza2[i][col] = el;
    }
  }
  return ok;
}

bool fillToDown(int row, int col)
{
  int el = plansza[row][col];
  bool ok = true;
  for (int i = 0; i < n; i++)
  {
    if (el < plansza[i][col])
    {
      ok = false;
    }
  }
  
  if (ok)
  {
    for (int i = 0; i < n; i++)
    {
      plansza2[i][col] = el;
    }
  }
  return ok;
}


int main()
{
  int T;
  scanf("%d", &T);


  
  for (int z = 0; z < T; z++)
  {
    scanf("%d %d\n", &n, &m);
    priority_queue<ValueRequest> pl;

    bool notfinish = false;
    int k = 0;
    
    for (int i = 0; i < n; i++)
    {
    
      for (int j = 0; j < m; j++)
      {
        scanf("%d", &plansza[i][j]);
        
        ValueRequest x(plansza[i][j], i, j);
        pl.push(x);
      }
    }
    bool found = true;
    memset(plansza2, 0, sizeof(plansza2));
    while (!pl.empty())
    {
      ValueRequest x = pl.top();
      pl.pop();
      //printf("%d %d %d\n",x.p, x.row,x.col);
      if (x.row == 0 && x.col == 0)
      {
        bool ok = fillToRight(x.row, x.col);
        ok |= fillToDown(x.row, x.col);
        if (!ok)
        {
          found = false;
          //break;
        }
      }
      else
      if (x.row == n - 1 && x.col == 0)
      {
        bool ok = fillToRight(x.row, x.col);
        ok |= fillToUp(x.row, x.col);
        if (!ok)
        {
          found = false;
          //break;
        }
      }
      else
      if (x.row == n - 1 && x.col == m - 1)
      {
        bool ok = fillToLeft(x.row, x.col);
        ok |= fillToUp(x.row, x.col);
        if (!ok)
        {
          found = false;
          //break;
        }
        
      }
      else
      if (x.row == 0 && x.col == m - 1)
      {
        bool ok = fillToLeft(x.row, x.col);
        ok |= fillToDown(x.row, x.col);
        if (!ok)
        {
          found = false;
          //break;
        }
        
      }
      else
      if (x.row == 0)
      {
        bool ok = fillToDown(x.row, x.col);
        if (!ok)
        {
          found = false;
          //break;
        }
        
      }
      else
      if (x.row == n - 1)
      {
        bool ok = fillToUp(x.row, x.col);
        if (!ok)
        {
          found = false;
          //break;
        }
      }
      else
      if (x.col == 0)
      {
        bool ok = fillToRight(x.row, x.col);
        if (!ok)
        {
          found = false;
          //break;
        }
      }
      else
      if (x.col == m - 1)
      {
        bool ok = fillToLeft(x.row, x.col);
        if (!ok)
        {
          found = false;
          //break;
        }
      }
      else
      {
        if (plansza[x.row][m - 1] >= plansza[x.row][0])
        {
          bool ok = fillToLeft(x.row, x.col);
          if (!ok)
          {
            found = false;
            //break;
          }
        }
        else
        {
          bool ok = fillToRight(x.row, x.col);
          if (!ok)
          {
            found = false;
            //break;
          }
        }

        if (plansza[0][x.col] >= plansza[n - 1][x.col])
        {
          bool ok = fillToDown(x.row, x.col);
          if (!ok)
          {
            found = false;
            //break;
          }
        }
        else
        {
          bool ok = fillToUp(x.row, x.col);
          if (!ok)
          {
            found = false;
            //break;
          }
        }
      }
    }
    
    DBG(
      for (int i = 0; i < n; i++)
      {
      for (int j = 0; j < m; j++)
      {
        printf("%d ", plansza2[i][j]);
      }
      
      printf("\n");
      }
      printf("\n");)

    
      bool ok =true;
      for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
      if (plansza[i][j] != plansza2[i][j])
        ok = false;
        
     if (ok)
      printf("Case #%d: YES\n", z + 1);
      else 
      printf("Case #%d: NO\n", z + 1);
      
  }
  return 0;
}
