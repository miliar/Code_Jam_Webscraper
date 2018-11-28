#include<stdio.h>
int main()
{
  int T;
  scanf("%d",&T);
  for(int Ti=1;Ti<=T;Ti++)
  {
    int N,M;
    scanf("%d %d",&N,&M);
    int A[N][M];
    for(int i=0;i<N;i++)
    {
      for(int j=0;j<M;j++)
      {
        scanf("%d",&A[i][j]);
      }
    }
    int r_max[N],c_max[M];
    for(int i=0;i<N;i++)
    {
      r_max[i]=0;
      for(int j=0;j<M;j++)
      {
        if(r_max[i]<A[i][j])r_max[i]=A[i][j];
      }
    }
   for(int i=0;i<M;i++)
    {
      c_max[i]=0;
      for(int j=0;j<N;j++)
      {
        if(c_max[i]<A[j][i])c_max[i]=A[j][i];
      }
    }
   bool ans=true;
   for(int i=0;i<N;i++)
   {
     for(int j=0;j<M;j++)
     {
       if(A[i][j]<r_max[i] &&
           A[i][j]<c_max[j])
       {
         ans=false;
       }
     }
   }
   printf("Case #%d: %s\n", Ti,(ans)?"YES":"NO");
         

  }
  return 0;
}
