#include<stdio.h>
int main()
{
    int T,N,M,i,j,k,ar[10][10],ct,r,f,no,p;
    scanf("%d",&T);
    for( i=1;i<=T;i++)
    {
         scanf("%d%d",&N,&M);
         printf("Case #%d: ",i);
         
         for(j=0;j<N;j++)
         for( k=0;k<M;k++)
              scanf("%d",&ar[j][k]);
         
         if(N==1 || M==1)
         {
                 printf("YES");
                 continue;
         }
         no=0;
         
         for( j=0;j<N;j++)
         {
              ct=0;
              f=0;
              for( k=0;k<M;k++)
              {
               if( ar[j][k]==1)
               {
                  ct++;
                  r=0;
                  for(p=0;p<N;p++)
                                  if(ar[p][k]==1)
                                                 r++;
                  if(r!=N)
                          f=1;
               }
              }
              if(ct!=0 && ct!=M && f==1)
              {
                       printf("NO\n");
                       no=1;
                       break;
              }         
         }
         if(no==1)
                  continue;
         printf("YES\n");
    }
         
}

