#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int v[110][110];
int r[110];
int c[110];

bool solve(int n,int m)
{
    for(int i=1;i<=n;i++)
       for(int j=1;j<=m;j++)
       {
           if(v[i][j]<r[i] && v[i][j]<c[j] )  return 0;
       }
    return 1;
}

int main()
{
    int n,m;
    int cas,cas1=1;

    freopen("B-large.in","r",stdin);
    freopen("data.txt","w",stdout);

    cin>>cas;
    while(cas--)
    {
        memset(v,0,sizeof(v));
        memset(r,0,sizeof(r));
        memset(c,0,sizeof(c));
        cin>>n>>m;
        for(int i=1;i<=n;i++)
           for(int j=1;j<=m;j++)
           {
               scanf("%d",&v[i][j]);
               r[i]=max(r[i],v[i][j]);
               c[j]=max(c[j],v[i][j]);
           }
        int ans=solve(n,m);
        printf("Case #%d: %s\n",cas1++, ans==1?"YES":"NO");
    }
    return 0;
}
