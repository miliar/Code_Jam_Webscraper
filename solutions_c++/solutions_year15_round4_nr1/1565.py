#include <iostream>
#include <cstdio>
#define MAX 100
using namespace std;

char str[MAX][MAX];
int R,C;

void read()
{
  char c;
  scanf("%d %d%c",&R,&C,&str[0][0]);
  for(int i=0;i<R;i++)
    {
      for(int j=0;j<C;j++)
	scanf("%c",&str[i][j]);
      scanf("%c",&c);
    }
}

int dOf(char c)
{
  if(c=='>')
    return 1;
  if(c=='^')
    return 2;
  if(c=='<')
    return 4;
  if(c=='v')
    return 8;
  return 0;
}


int solve()
{
  int X[R][C];
  for(int i=0;i<R;i++)
    for(int j=0;j<C;j++)
      X[i][j]=0;
  for(int c=0;c<C;c++)
    {
      if(str[0][c]!='.')
	X[0][c]|=2;
      else
	{
	  int r=0;
	  while(++r<R && str[r][c]=='.');
	  if(r!=R)
	    X[r][c]|=2;
	}
    }
  for(int c=0;c<C;c++)
    {
      if(str[R-1][c]!='.')
	X[R-1][c]|=8;
      else
	{
	  int r=R-1;
	  while(--r>=0 && str[r][c]=='.');
	  if(r!=-1)
	    X[r][c]|=8;
	}
    }
  for(int r=0;r<R;r++)
    {
      if(str[r][0]!='.')
	X[r][0]|=4;
      else
	{
	  int c=0;
	  while(++c<C && str[r][c]=='.');
	  if(c!=C)
	    X[r][c]|=4;
	}
    }
  for(int r=0;r<R;r++)
    {
      if(str[r][C-1]!='.')
	X[r][C-1]|=1;
      else
	{
	  int c=C-1;
	  while(--c>=0 && str[r][c]=='.');
	  if(c!=-1)
	    X[r][c]|=1;
	}
    }
  int rst=0;
  for(int r=0;r<R;r++)
    for(int c=0;c<C;c++)
      {
	if(str[r][c]!='.')
	  {
	    if(X[r][c]==15)
	      return -1;
	    if(X[r][c] & dOf(str[r][c]))
	      rst++;
	  }
      }
  return rst;
}

int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      int rst = solve();
      if(rst==-1)
	printf("Case #%d: IMPOSSIBLE\n",t);
      else
	printf("Case #%d: %d\n",t,rst);
    }
}
