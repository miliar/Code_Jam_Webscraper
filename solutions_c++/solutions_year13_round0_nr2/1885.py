#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int data[150][150];
bool sign[150][150];
struct node
{
    int v,i,j;
}g[20000];
bool cmp(node a,node b)
{
   return a.v<b.v;

}
int main()
{
	int i,j,k,l,n,m,t,T,ii,c1,c2;
	freopen("c://B-large.in","r",stdin);
	freopen("c://B-large.txt","w",stdout);
    scanf("%d",&T);
    for(ii=1;ii<=T;++ii)
    {
       scanf("%d%d",&n,&m);
       memset(sign,0,sizeof(sign));
       for(i=0;i<n;++i)
       {
           for(j=0;j<m;++j)
           {
               scanf("%d",&data[i][j]);
           }
       }

       int t=0;
       for(i=0;i<n;++i)
       {
           for(j=0;j<m;++j)
           {
            g[t].v=data[i][j];
            g[t].i=i;
            g[t].j=j;
            ++t;
           }
       }
       sort(g,g+t,cmp);
       int a;
       for(a=0;a<t;++a)
       {
           int r=g[a].i,c=g[a].j,v=g[a].v;
           for(i=0;i<n;++i)
           {
               if(sign[i][c]==0)
                if(data[i][c]!=v)break;

           }
           for(j=0;j<m;++j)
           {
               if(sign[r][j]==0)
                if(data[r][j]!=v)break;
           }
           if(i==n&&j==m)
           {
               for(i=0;i<n;++i)sign[i][c]=1;
               for(j=0;j<m;++j)sign[r][j]=1;
           }
           else if(j==m)
           {
               for(j=0;j<m;++j)sign[r][j]=1;
           }
           else if(i==n)
           {
               for(i=0;i<n;++i)sign[i][c]=1;
           }
           else break;

       }
       if(t==a)
       {
           printf("Case #%d: YES",ii);
       }
       else
       {
           //printf("%d %d\n",g[a].i,g[a].j);
           printf("Case #%d: NO",ii);
       }
       if(ii!=T)printf("\n");

    }


    return 0;
}
