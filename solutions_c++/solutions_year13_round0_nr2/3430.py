#include <cstdio>

#define MAX_N 100

int grid[MAX_N][MAX_N];
int output[MAX_N][MAX_N];

using namespace std;

int main()
{
  int t, n, m;
  scanf("%d",&t);
  for (int k=0; k<t; k++)
  {
    scanf("%d %d",&n,&m);
    for (int i=0; i<n; i++)
      for (int j=0; j<m; j++)
        scanf("%d",&grid[i][j]);
    /*
    for (int i=0; i<n; i++)
    {
      for (int j=0; j<m; j++)
        printf("%d ",grid[i][j]);
      printf("\n");
      }*/
    //taglia righe
    for (int i=0; i<n; i++)
    {
      int max = grid[i][0];
      for (int j=1; j<m; j++)
        if (max<grid[i][j])
          max = grid[i][j];
      for (int j=0; j<m; j++)
        output[i][j] = max;
    }
    //taglia colonne
    for (int j=0; j<m; j++)
    {
      int max = grid[0][j];
      for (int i=1; i<n; i++)
        if (max < grid[i][j])
          max = grid[i][j];
      for (int i=0; i<n; i++)
        if (output[i][j] > max)
          output[i][j] = max;
    }/*
    printf("\n");
    for (int i=0; i<n; i++)
    {
      for (int j=0; j<m; j++)
        printf("%d ",output[i][j]);
      printf("\n");
      }*/
    printf("Case #%d: ",k+1);
    bool ok = true;
    for (int i=0; i<n; i++)
      for (int j=0; j<m; j++)
        if (output[i][j] != grid[i][j])
          ok = false;
    if (ok)
      printf("YES\n");
    else
      printf("NO\n");
  }
  return 0;
}
