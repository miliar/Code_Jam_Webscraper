#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<set>
#include<string.h>
#include<algorithm>
using namespace std;
int r,n,m,k;
int ans[110][5],solved[110];
int hash[130];
int data[110][10],flag;
int main()
{
    freopen("reada.txt","r",stdin);
    freopen("outa.txt","w",stdout);
    int t,a,b,c,i,j;
    scanf("%d",&t);
    printf("Case #1:\n");
    scanf("%d%d%d%d",&r,&n,&m,&k);
    for(i=0;i<r;i++)
      for(j=0;j<k;j++)
         scanf("%d",&data[i][j]);
    for(a=2;a<=5;a++)
      for(b=2;b<=5;b++)
        for(c=2;c<=5;c++)
        {
           for(i=0;i<130;i++) 
                hash[i]=0;
           hash[1]=1;
           hash[a]=1;
           for(i=1;i<=5;i++)
           {
              if(hash[i]==1 && hash[b*i]==0) 
                      hash[b*i]=2;
           }
           for(i=1;i<=25;i++)
              if( (hash[i]==1 || hash[i]==2) && hash[c*i]==0) hash[c*i]=3;
           for(i=0;i<r;i++)
           {
             if(solved[i]==0)
             {
                flag=0;
                for(j=0;j<k;j++)
                {
                  if(hash[data[i][j]]==0)
                  { flag=1; break; }
                }
                if(flag==0)
                {
                   ans[i][0]=a; ans[i][1]=b; ans[i][2]=c;
                   solved[i]=1;
                }
             }
           }
        }
    for(i=0;i<r;i++)
       printf("%d%d%d\n",ans[i][0],ans[i][1],ans[i][2]);
    return 0;
}
