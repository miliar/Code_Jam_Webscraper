#include<stdio.h>
#include<fstream>
#include<cstdio>

int t,n,m,i,j,ar[102][102],flag;
using namespace std;
int main()
{
   freopen("B-large (1).in","r",stdin);
freopen("B-large (1).out","w",stdout);
      scanf("%d",&t);
    for(int p=0;p<t;p++)
    {    printf("Case #%d: ",p+1);
         int flag1=0;
       scanf("%d%d",&n,&m) ;
        flag=0;
         for(i=0;i<n;i++)
            for(j=0;j<m;j++)
               scanf("%d",&ar[i][j]);

             for(i=0;i<n;i++)
             for(j=0;j<m;j++)
             {
                 flag=0;
                 flag1=0;
                 for(int k=0;k<n;k++)
                 if(ar[k][j]>ar[i][j])
                 {
                     //printf("\n%d %d %d             %d  %d \n",i,j,k,ar[k][j],ar[i][j]);
                     flag=1;
                     break;
                 }
                 for(int k=0;k<m;k++)
                 if(ar[i][k]>ar[i][j])
                 {
                    //printf("\n%d %d %d       %d  %d \n",i,j,k,ar[i][k],ar[i][j]);
                     flag1=1;
                     break;
                 }
                      // printf("%d   %d",flag,flag1);
                                if(flag&&flag1)
                                {
                                    printf("NO\n");
                                    goto x;
                                }

             }


             printf("YES\n");

                x:printf("");
    }
}
