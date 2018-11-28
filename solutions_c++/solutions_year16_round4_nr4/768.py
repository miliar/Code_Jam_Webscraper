#include <vector>
#include <stdio.h>
#include <iostream>
#include <cmath>
#include <string.h>
#include <set>


using namespace std;

const int N=205;

int n;
char s[N][N];

int f[205];
int g[205];

int dfs(int dep)
{
    if(dep==n+1) return 1;

    for(int per=1;per<=n;per++) if(!g[per])
    {
        g[per]=1;
        int sum=0;
        for(int i=1;i<=n;i++) if(!f[i]&&s[per][i]=='1')
        {
            sum++;
            f[i]=1;
            if(!dfs(dep+1)) return 0;
            f[i]=0;
        }
        if(!sum) return 0;
        g[per]=0;
    }


    return 1;

}

int check()
{
    memset(f,0,sizeof(f));
    memset(g,0,sizeof(g));
    return dfs(1);
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("ans","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        scanf("%d",&n);
        for(int i=1;i<=n;i++) scanf("%s",s[i]+1);
        vector<pair<int,int> >  a;
        for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) if(s[i][j]=='0')
        {
            a.push_back(make_pair(i,j));
        }
        int ans=-1;
        if(a.size()==0)
        {
            puts("0"); continue;
        }
        int m=a.size();
        for(int i=0;i<(1<<m);i++)
        {
            int tmp=0;
            for(int j=0;j<m;j++) if(i&(1<<j))
            {
                tmp++;
                s[a[j].first][a[j].second]='1';
            }
            if(ans==-1||tmp<ans)
            {
                if(check())
                {
                    ans=tmp;
                }
            }

            for(int j=0;j<m;j++) if(i&(1<<j))
            {
                s[a[j].first][a[j].second]='0';
            }
        }
        printf("%d\n",ans);
    }
}

