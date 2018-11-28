#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int arr[55][55];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("Coutlarge.txt","w",stdout);
    int t,tc;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
        int r,c,m,e;
        int i,j,x,y,it1,it2;
        scanf("%d%d%d",&r,&c,&m);
        if(r*c-m==1)
        {
            printf("Case #%d:\n",tc);
            for(i=0;i<r;i++)
            {
                for(j=0;j<c;j++)
                {
                    if(i==0 && j==0)
                        printf("c");
                    else
                        printf("*");
                }
                printf("\n");
            }
            continue;
        }
        if(r==1)
        {
            printf("Case #%d:\n",tc);
            printf("c");
            for(i=1;i<c-m;i++)
                printf(".");
            for(i=0;i<m;i++)
                printf("*");
            printf("\n");
            continue;
        }
        if(c==1)
        {
            printf("Case #%d:\n",tc);
            printf("c\n");
            for(i=1;i<r-m;i++)
                printf(".\n");
            for(i=0;i<m;i++)
                printf("*\n");
            continue;
        }
        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
                arr[i][j]=1;
        e=r*c-m;
        int flag=0;
        for(i=2;i<=r;i++)
            for(j=2;j<=c;j++)
                for(x=0;x<=j;x++)
                    for(y=0;y<=i;y++)
                    {
                        if(x==1 || y==1)
                            continue;
                        if(i==r && x>0)
                            continue;
                        if(j==c && y>0)
                            continue;
                        if(i*j+x+y==e)
                        {
                            flag=1;
                            goto here;
                        }
                    }
        here:
        printf("Case #%d:\n",tc);
        if(flag==1)
        {
           for(it1=0;it1<i;it1++)
             for(it2=0;it2<j;it2++)
               arr[it1][it2]=0;
           for(it1=0;it1<x;it1++)
               arr[i][it1]=0;
           for(it1=0;it1<y;it1++)
               arr[it1][j]=0;
           arr[0][0]=2;
           for(i=0;i<r;i++)
           {
               for(j=0;j<c;j++)
               {
                   if(arr[i][j]==0)
                      printf(".");
                   else if(arr[i][j]==1)
                      printf("*");
                   else
                      printf("c");
               }
               printf("\n");
           }
        }
        else
            printf("Impossible\n");
    }
    return 0;
}
