#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <cmath>

int t;
int n,m;
int A[100][100];
int R[100][100];
int maxCol[100];
int maxRow[100];

inline void podarFila(int f, int v)
{
 for(int i=0;i<m;i++)
  R[f][i] = std::min(v,R[f][i]);
}

inline void podarCol(int c, int v)
{
 for(int i=0;i<n;i++)
  R[i][c] = std::min(v,R[i][c]);
}

int main()
{
 //freopen("B-large.in", "r", stdin);
 //freopen("B-large.out", "w", stdout);

 scanf("%d", &t);
 for(int i_=1;i_<=t;i_++)
 {
  printf("Case #%d: ", i_);
  scanf("%d %d", &n, &m);
  
  for(int i=0;i<n;i++) maxRow[i] = 0;
  for(int i=0;i<m;i++) maxCol[i] = 0;
  
  for(int i=0;i<n;i++)
  {
   for(int j=0;j<m;j++)
   {
    scanf("%d", &A[i][j]);
    if(A[i][j] > maxRow[i]) maxRow[i] = A[i][j];
    if(A[i][j] > maxCol[j]) maxCol[j] = A[i][j];
    R[i][j] = 100;
   }
  }
 // for(int i=0;i<n;i++)printf("%d ", maxRow[i]);printf("\n");
  //for(int i=0;i<m;i++)printf("%d ", maxCol[i]);printf("\n");
  
  for(int i=0;i<n;i++) podarFila(i,maxRow[i]);
  for(int i=0;i<m;i++) podarCol(i,maxCol[i]);
  bool can = true;
  for(int i=0;i<n;i++)for(int j=0;j<m;j++)if(R[i][j]!=A[i][j]){can=false;goto end;}
  end:
   
  printf("%s\n", can?"YES":"NO");
 }
}
