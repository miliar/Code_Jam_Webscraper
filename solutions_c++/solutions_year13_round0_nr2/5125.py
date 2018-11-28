#include <iostream>
#include <string.h>
#include <stdio.h>
#define maxn 101
using namespace std;
int map[ maxn ][ maxn ];
int map2[maxn][maxn];
int ma[maxn];
int ma2[maxn];
int n,m;
bool cut()
{
    if(n==1||m==1) return true;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            map2[i][j]=ma[i];
        }
    }
    for(int j=0; j<m; j++)
    {
        int ans=0;
        for(int i=0; i<n; i++)
        {
            ans=max(ans,map[i][j]);
        }
        ma2[j]=ans;
    }
    for(int j=0; j<m; j++)
    {
        for(int i=0; i<n; i++)
        {
            if(map2[i][j]>ma2[j])
                map2[i][j]=ma2[j];
        }
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(map[i][j]!=map2[i][j]) return false;
        }
    }
    return true;
}
int main()
{
  //  freopen("B-large.in","r",stdin);
  //  freopen("out.txt","w",stdout);
    int t;
    int cnt=0;
    scanf("%d",&t);
    while(cnt!=t)
    {
        cnt++;
        scanf("%d%d",&n,&m);
        for(int i=0; i<n; i++)
        {
            int ans=0;
            for(int j=0; j<m; j++)
            {
                scanf("%d",&map[i][j]);
                map2[i][j]=100;
                ans=max(ans,map[i][j]);
            }
            ma[i]=ans;
        }
        if(cut())
            printf("Case #%d: YES\n",cnt);
        else
            printf("Case #%d: NO\n",cnt);
    }
    return 0;
}
