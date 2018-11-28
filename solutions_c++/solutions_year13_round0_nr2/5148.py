#include <iostream>
#include <cstring>
#include <cstdio>
const int maxn=10000;
using namespace std;
int map[maxn][maxn];
int map2[maxn][maxn];
int ch[maxn];
int ch2[maxn];
int n,m;
bool cut()
{
    if(n==1||m==1) return true;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            map2[i][j]=ch[i];
        }
    }
    for(int j=0; j<m; j++)
    {
        int ans=0;
        for(int i=0; i<n; i++)
        {
            ans=max(ans,map[i][j]);
        }
        ch2[j]=ans;
    }
    for(int j=0; j<m; j++)
    {
        for(int i=0; i<n; i++)
        {
            if(map2[i][j]>ch2[j])
                map2[i][j]=ch2[j];
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

    //freopen("in.txt","r",stdin);
  // freopen("a.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cas=0;
    while(t--)
    {
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
            ch[i]=ans;
        }
        if(cut())
            printf("Case #%d: YES\n",++cas);
        else
            printf("Case #%d: NO\n",++cas);
    }
    return 0;
}
