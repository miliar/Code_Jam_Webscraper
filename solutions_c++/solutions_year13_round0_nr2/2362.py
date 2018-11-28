#include<iostream>
#include<string.h>
using namespace std;
int a[101][101];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int i,j,k,sign;
    int n,m;
    for(k=1;k<=t;k++)
    {
             scanf("%d%d",&n,&m);
             memset(a,0,sizeof(a));
             for(i=1;i<=n;i++)
             for(j=1;j<=m;j++)
             {
             scanf("%d",&a[i][j]);
             if(a[i][0]<a[i][j]) a[i][0]=a[i][j];
             if(a[0][j]<a[i][j]) a[0][j]=a[i][j];
             }
             for(i=1;i<=n;i++)
             {
                   for(j=1;j<=m;j++)
                   {
                          if(a[i][j]!=a[i][0]&&a[i][j]!=a[0][j]) break;
                   }
                   if(j!=(m+1)) break;
             }
             printf("Case #%d: ",k);
             if(i==(n+1)) printf("YES\n");
             else printf("NO\n"); 
             
    }
    return 0;
}
