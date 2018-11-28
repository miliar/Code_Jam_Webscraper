#include<stdio.h>
int main()
{
    int t,r,C[4][4],A[4],x,n,i,j,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
              x=0;
              scanf("%d",&r);
              r--;
              for(i=0;i<4;i++)
              {
                      for(j=0;j<4;j++)
                        scanf("%d",&C[i][j]);
              }
              for(j=0;j<4;j++)
                A[j]=C[r][j];
                
              for(j=0;j<4;j++)
                printf("%d ",A[j]);
                
              scanf("%d",&r);
              r--;
              for(i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                        scanf("%d",&C[i][j]);
              }
              for(i=0;i<4;i++)
              {
                      for(j=0;j<4;j++)
                      {
                         if(A[i]==C[r][j])
                           {
                              x++;
                              n=A[i];
                           }
                      }
                      if(x>1)
                      {
                         printf("Case #%d: Bad magician!\n",k);
                         break;
                      }
              }
              if(x==0)
                printf("Case #%d: Volunteer cheated!\n",k);
              if(x==1)
                printf("Case #%d: %d\n",k,n);
    }
}
