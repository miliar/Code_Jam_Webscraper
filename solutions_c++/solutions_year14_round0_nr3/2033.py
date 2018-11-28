#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <set>
using namespace std;

#define DBG(X)
char odp[64][64];
int odw[64][64];
int miny[64][64];

bool sprawdz(int i, int j, int r, int c)
{
  for (int a = -1; a < 2; a++)
  for (int b = -1; b < 2; b++)
    
    if (i + a >= 0 && i + a < r && j + b >= 0 && j + b < c)
    if (odp[i + a][j + b] == '*')
    return false;
  return true;
}


void check(int i, int j, int r, int c)
{
  if (i < 0 || i >= r || j < 0 || j >= c)
    return;
  if (odp[i][j] == '*')
    return;
  if (odw[i][j])
    return;

  odw[i][j] = 1;
  
  if (miny[i][j] >= 1) return;

  
  check(i - 1, j, r, c);
  check(i, j - 1, r, c);
  check(i + 1, j, r, c);
  check(i, j + 1, r, c);
  check(i + 1, j + 1, r, c);
  check(i + 1, j - 1, r, c);
  check(i - 1, j + 1, r, c);
  check(i - 1, j - 1, r, c);
}

int main()
{
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; t++)
  {

    //cout << C << " " << F << " " << X << endl;
    int r, c, m;
    scanf("%d%d%d", &r, &c, &m);
    int skl = 0;
    if (m && m == r * c - 1)
    {
        printf("Case #%d:\n", t);
        int o = 1;
        for (int a = 0; a < r; a++)
        {
        for (int b = 0; b < c; b++)
        {
          if (a == r - 1 && b == c - 1)
          {
            printf("c");
          }
          else printf("*");
        }
        printf("\n");
        }
      
      continue;
    }
    for (int b = 0; b < (1 << (r * c)); b++ )
    {
      int s = 0;
      //printf("%d\n",b);
      for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++)
      {
        int ofs = c * i + j;
        //printf("ofs %d\n",ofs);
        if (b & (1 << ofs))
        {
          odp[i][j] = '.';
        }
        else
        {
          odp[i][j] = '*';
          s++;
        }
      }
      if (s != m) continue;
      
        /*for (int a = 0; a < r; a++)
        {
        for (int bb = 0; bb < c; bb++)
        {
          printf("%c", odp[a][bb]);
        }
        printf("\n");
        }*/
      
      //printf("\n");
      memset(odw, 0, sizeof(odw));
      skl = 0;
      for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++)
      {
        if (sprawdz(i,j,r,c))
          miny[i][j]=0;
        else
        if (odp[i][j] == '.')
          miny[i][j] = 1;
        else
          miny[i][j] = 2;
      }

      for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++)
      {
        if (!skl && !miny[i][j])
        {
          check(i, j, r, c);
          skl++;
        }
      }
     
      bool ok = true;
      if (skl==1)
      {
      for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++)
       if (odp[i][j]=='.' && !odw[i][j])
       ok = false;
      if (!ok) skl= 2;
      }

      
      if (skl == 1)
        break;

    }

      if (skl != 1)
      {
        printf("Case #%d:\nImpossible\n", t);
      }
      else
      {
        printf("Case #%d:\n", t);
        int o = 1;
        for (int a = 0; a < r; a++)
        {
        for (int b = 0; b < c; b++)
        {
          if (miny[a][b] == 0 && o)
          {
            printf("c");
            o=0;
          }
          else printf("%c", odp[a][b]);
        }
        printf("\n");
        }
      }
    

#if 0
    
    //printf("%d %d %d\n", r, c, m);
    bool ok = false;

    for (int i = r - 1; i >= 0; i--)
    for (int j = 0; j < c; j++)
    for (int k = i; k >= 0; k--)
    for (int l = j; l < c; l++)
    {
      int x1 = max(0, j - 1), y1 = max(0, i - 1);
      int x2 = min(c - 1, j + 1), y2 = min(r - 1, i + 1);
      
      int X1 = max(0, l - 1), Y1 = max(0, k - 1);
      int X2 = min(c - 1, l + 1), Y2 = min(r - 1, k + 1);
      
      int P = 0;
      int reszta  = 0;
      /*if (i == k && j == l)
      {
        P = (X2 - x1 + 1) * (Y2 - y1 + 1);
      }
      
      else
      if (i == k)
      {
        P = (X2 - x1 + 1) * (Y2 - y1 + 1);
      }
      else
      if (j == l)
      {
        P = (X2 - x1 + 1) * (y1 - Y2 + 1);
        
      }
      else*/
      {
        int p1 = (X2 - x1 + 1) * (y2 - Y1 + 1);
        int p2 = (X1 - x1) * (y1 - Y1);
        DBG(printf("X1 = %d, Y1 = %d, X2 = %d, Y2 = %d\n", X1, Y1, X2, Y2);
        printf("x1 = %d, y1 = %d, x2 = %d, y2 = %d\n", x1, y1, x2, y2);
        printf("p1 = %d p2 = %d\n", p1, p2);)
        P = p1 - p2;
        reszta = p2;
      }
      
      if (r * c - m <= P + reszta && r * c - m >= P)
      {
        DBG(printf("P %d reszta %d i = %d j = %d k = %d l = %d\n", P, reszta, i, j, k, l);)
        
        ok =true;
        int R = r * c - m - P;
        DBG(printf("R %d\n", R);)
        for (int a = 0; a < r; a++)
        for (int b = 0; b < c; b++)
          odp[a][b] = '*';
          
        for (int a = x1; a <= X2; a++)
        for (int b = y1; b <= y2; b++)
        {
          odp[b][a] = '.';
        }
        for (int a = X1; a <= X2; a++)
        for (int b = Y1; b <= y1; b++)
        {
          odp[b][a] = '.';
        }

        DBG(printf("%d %d %d %d\n",X1, Y1, x1, y1);)
        for (int a = y1 - 1; a >= Y1; a--)
        for (int b = X1 - 1; b >= x1; b--)
        {
          if (R)
          {
            odp[a][b] = '.';
            R--;
          }
          else
          break;
        }
        
        odp[i][j] = 'c';
        //odp[k][l] = 'c';
        goto et;
        
      }
    }
et:    
    
    //cout << endl;
    if (ok)
    {
        printf("Case #%d:\n", t);
        for (int a = 0; a < r; a++)
        {
        for (int b = 0; b < c; b++)
        {
          printf("%c", odp[a][b]);
        }
        printf("\n");
        }
          
      
    }
    else
    printf("Case #%d:\nImpossible\n", t);
#endif    

  }
  
  return 0;
}



