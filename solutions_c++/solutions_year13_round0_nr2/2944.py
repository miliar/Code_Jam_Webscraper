#include <stdio.h>
#include <stdlib.h>

int n,count = 1;
int nrow,ncol;
int maze[105][105];


void printMaze()
{
  for(int i=0;i<nrow;i++)
    {
      for(int j=0;j<ncol;j++)
	{
	  printf("%d ",maze[i][j]);
	}
      printf("\n");
    }
}

bool cutRow(int row,int n)
{
  for(int c = 0;c<ncol;c++)
    {
      if(maze[row][c]>n)
	return false;
    }
  return true;
}
bool cutCol(int col,int n)
{
  for(int r = 0;r<nrow;r++)
    if(maze[r][col]>n)
      return false;
  return true;
}

void solve(int count,int nrow,int ncol)
{
  //printMaze();
  for(int i=0;i<nrow;i++)
    for(int j=0;j<ncol;j++)
      {
	if( !cutRow(i,maze[i][j]) && !cutCol(j,maze[i][j]))
	  {
	    // printf("x=%d,y=%d\n",i,j);
	    printf("Case #%d: NO\n",count);
	    return ;
	  }
      }
  printf("Case #%d: YES\n",count);
  return;
}
int main()
{
  scanf("%d",&n);
  while(count<=n)
    {
      scanf("%d%d",&nrow,&ncol);
      for(int i=0;i<nrow;i++)
	for(int j=0;j<ncol;j++)
	  scanf("%d",&maze[i][j]);
      solve(count++,nrow,ncol);
    }
  return 0;
}
