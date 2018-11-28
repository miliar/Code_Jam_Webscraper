/*===============================================================
*   Copyright (C) 2013 All rights reserved.
*   
*   file: A.cpp
*   author: ivapple
*   date: 2013-04-13
*   description: 
*
*   update log: 
*
================================================================*/
#include <cstdlib>
#include <cstdio>
#include <cstring>

#include <iostream>

#define out(x) (cout<<#x<<": "<<x<<endl)

#define FOR(i,s,t) for(i=s; i<t; i++)

using namespace std;

template<class T>void show(T a, int n){int i; for(i=0;i<n;i++)cout<<a[i]<<" ";cout<<endl;}

template<class T>void show(T a, int r, int l){int i; for(i=0;i<r;i++)show(a[i],l);cout<<endl;}


int T;
char matrix[5][5];
int O_row_count;
int O_coloum_count;
int O_diagnal_count;
int X_row_count;
int X_coloum_count;
int X_diagnal_count;

void init()
{
  int i;
  O_row_count = 0;
  O_coloum_count = 0;
  O_diagnal_count = 0;
  X_row_count = 0;
  X_coloum_count = 0;
  X_diagnal_count = 0;
}
//1 X win
//0 O win
//-1 no one win<
int check()
{
  int i, j;
  bool hasT;
  bool isfull;
  isfull = 1;
  for (i=0; i<4; i++)
  {
    O_row_count = 0;
    X_row_count = 0;
    hasT = 0;
    for (j=0; j<4; j++)
    {
      if (matrix[i][j] == 'X')
        X_row_count++;
      if (matrix[i][j] == 'O')
        O_row_count++;
      if (matrix[i][j] == 'T')
        hasT = 1;
      if (matrix[i][j] == '.')
        isfull = 0;
    }
    if (X_row_count == 4 or X_row_count ==3 and hasT)
      return 1;
    if (O_row_count == 4 or O_row_count ==3 and hasT)
      return 0;
  }
  for (j=0; j<4; j++)
  {
    O_coloum_count = 0;
    X_coloum_count = 0;
    hasT = 0;
    for (i=0; i<4; i++)
    {
      if (matrix[i][j] == 'X')
        X_coloum_count++;
      if (matrix[i][j] == 'O')
        O_coloum_count++;
      if (matrix[i][j] == 'T')
        hasT = 1;
    }
    if (X_coloum_count == 4 or X_coloum_count ==3 and hasT)
      return 1;
    if (O_coloum_count == 4 or O_coloum_count ==3 and hasT)
      return 0;
  }
  hasT = 0;
  for (i=0; i<4; i++)
  {
    if (matrix[i][i] == 'X')
      X_diagnal_count++;
    if (matrix[i][i] == 'O')
      O_diagnal_count++;
    if (matrix[i][i] == 'T')
      hasT = 1;
    //if (matrix[i][j] == '.')
      //isfull = 0;
    if (X_diagnal_count == 4 or X_diagnal_count ==3 and hasT)
      return 1;
    if (O_diagnal_count == 4 or O_diagnal_count ==3 and hasT)
      return 0;
  }
  hasT = 0;
  X_diagnal_count = 0;
  O_diagnal_count = 0;
  for (i=0; i<4; i++)
  {
    if (matrix[i][3-i] == 'X')
      X_diagnal_count++;
    if (matrix[i][3-i] == 'O')
      O_diagnal_count++;
    if (matrix[i][3-i] == 'T')
      hasT = 1;
    //if (matrix[i][j] == '.')
      //isfull = 0;
    if (X_diagnal_count == 4 or X_diagnal_count ==3 and hasT)
      return 1;
    if (O_diagnal_count == 4 or O_diagnal_count ==3 and hasT)
      return 0;
  }
  if (isfull)
    return -1;
  else
    return -2;
}



int main()
{
  int i,j;
  int state;
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  scanf("%d", &T);
  int t;
  char buf[5];
  t = 1;
  while (T--)
  {
    init();
    for (i=0; i<4; i++)
    {
      scanf("%s", matrix[i]);
    //  show(matrix[i], 4);
    }
    state = check();
    printf("Case #%d: ", t);
    if (state == 1)
      printf("X won\n");
    if (state == 0)
      printf("O won\n");
    if (state == -1)
      printf("Draw\n");
    if (state == -2)
      printf("Game has not completed\n");
    t++;
    //scanf("%s", buf);
  }
  return 0;
}
