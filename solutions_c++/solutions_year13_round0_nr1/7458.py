#include<cstdio>
#include<cstring>
#define MAXN 6
using namespace std;
char g[MAXN][MAXN];

int row(int t)
{
  int n1,n2,n3,i,j;
  for (i=0;i<4;i++)
  {
    n1=n2=n3=0;
    for (j=0;j<4;j++)
    {
      if (g[i][j]=='X')
        n1++;
      if (g[i][j]=='O')
        n2++;
      if (g[i][j]=='T')
        n3++;
    }
    if (n1+n3>=4)
    {
      printf("Case #%d: X won\n",t);
      return 1;
    }
    if (n2+n3>=4)
    {
      printf("Case #%d: O won\n",t);
      return 1;
    }
  }
  return 0;
}

int col(int t)
{
  int n1,n2,n3,i,j;
  for (j=0;j<4;j++)
  {
    n1=n2=n3=0;
    for (i=0;i<4;i++)
    {
      if (g[i][j]=='X')
        n1++;
      if (g[i][j]=='O')
        n2++;
      if (g[i][j]=='T')
        n3++;
    }
    if (n1+n3>=4)
    {
      printf("Case #%d: X won\n",t);
      return 1;
    }
    if (n2+n3>=4)
    {
      printf("Case #%d: O won\n",t);
      return 1;
    }
  }
  return 0;
}

int dia(int t)
{
  int n1,n2,n3,i,j;
 
    n1=n2=n3=0;
    for (i=0;i<4;i++)
    {
      if (g[i][i]=='X')
        n1++;
      if (g[i][i]=='O')
        n2++;
      if (g[i][i]=='T')
        n3++;
    }
    if (n1+n3>=4)
    {
      printf("Case #%d: X won\n",t);
      return 1;
    }
    if (n2+n3>=4)
    {
      printf("Case #%d: O won\n",t);
      return 1;
    }
 
 
  n1=n2=n3=0;
    for (i=0;i<4;i++)
    {
      if (g[i][3-i]=='X')
        n1++;
      if (g[i][3-i]=='O')
        n2++;
      if (g[i][3-i]=='T')
        n3++;
    }
    if (n1+n3>=4)
    {
      printf("Case #%d: X won\n",t);
      return 1;
    }
    if (n2+n3>=4)
    {
      printf("Case #%d: O won\n",t);
      return 1;
    } 
 
  return 0;
}

int end(int t)
{
  int i;
  for (i=0;i<4;i++)
    if (strstr(g[i],"."))
    { 
      printf("Case #%d: Game has not completed\n",t);
      return 0;
    }
  return 1;
} 

int main()
{
  int i,j,k,tc;
  char tmp[999];
  scanf("%d\n",&tc);
  for (k=1;k<=tc;k++)
  {
    for (i=0;i<4;i++)
      gets(g[i]);
    gets(tmp);
    if (row(k)) continue;
    if (col(k)) continue;
    if (dia(k)) continue;
    if (end(k)==0) continue;
    printf("Case #%d: Draw\n",k);
  }
  return 0;
}
