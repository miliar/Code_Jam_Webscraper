#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
using namespace std;
const int MAXN=110;
int g[MAXN][MAXN];
int a[MAXN][MAXN];
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
    int n,m;
    scanf("%d",&T);
    int iCase=0;
    while(T--)
    {
        iCase++;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
          for(int j=0;j<m;j++)
          {
              scanf("%d",&g[i][j]);
              a[i][j]=100;
          }
        for(int i=0;i<n;i++)
        {
            int t=0;
            for(int j=0;j<m;j++)
              t=max(t,g[i][j]);
            for(int j=0;j<m;j++)
              if(a[i][j]>=t)
                  a[i][j]=t;
        }
        for(int j=0;j<m;j++)
        {
            int t=0;
            for(int i=0;i<n;i++)
              t=max(t,g[i][j]);
            for(int i=0;i<n;i++)
              if(a[i][j]>=t)
                  a[i][j]=t;
        }
        int flag=true;
        for(int i=0;i<n;i++)
          for(int j=0;j<m;j++)
            if(a[i][j]!=g[i][j])
            {
                flag=false;
                break;
            }
        if(flag)printf("Case #%d: YES\n",iCase);
        else printf("Case #%d: NO\n",iCase);
    }
    return 0;
}
