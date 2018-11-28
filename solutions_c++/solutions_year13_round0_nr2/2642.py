#include<iostream>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stdio.h>
#include<stack>
#include<queue>
#include<map>
#include<set>
#define ll long long 
#define oo 1000000000
using namespace std;   
int arc[12][12],n,m;
bool f[12][12];
bool ok()
{
      int i,j;
      for (i=1;i<=n;i++)
         for (j=1;j<=m;j++)
           if (arc[i][j]==1 && !f[i][j]) return false;
      return true;
}
int main()
{
     // freopen("B-small-attempt0.in","r",stdin);
     // freopen("output.txt","w",stdout);
      int T,t,i,j;
      scanf("%d",&T);
      for (t=1;t<=T;t++)
      {   
            scanf("%d%d",&n,&m);
            for (i=1;i<=n;i++)
              for (j=1;j<=m;j++)
                scanf("%d",&arc[i][j]);
            memset(f,false,sizeof(f));
            for (i=1;i<=n;i++)
            if (arc[i][1]==1)
            {
                   for (j=1;j<=m;j++)
                     if (arc[i][j]==2) goto A;
                   for (j=1;j<=m;j++) f[i][j]=true;  
                   A: ;
            }
            for (j=1;j<=m;j++)
            if (arc[1][j]==1)
            {
                   for (i=1;i<=n;i++)
                     if (arc[i][j]==2) goto B;
                   for (i=1;i<=n;i++) f[i][j]=true;  
                   B: ;                             
            }
            printf("Case #%d: ",t);
            if (ok()) printf("YES\n");
               else printf("NO\n");
      }
      return 0;
}
