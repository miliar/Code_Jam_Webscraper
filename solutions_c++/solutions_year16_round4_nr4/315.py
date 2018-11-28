#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
char s[5][5];
int mp[5][5];
vector<int> pre[17];
int n;
int visx[5],visy[5],pred[5];
bool match(int x)
{
    visx[x]=1;
    for(int i=0; i<n; i++) if(mp[x][i])
    {
        if(visy[i]) continue;
        visy[i]=1;
        if(pred[i]==-1||match(pred[i]))
        {
            pred[i]=x;
            return 1;
        }
    }
    return 0;
}
int hung()
{
    memset(pred,-1,sizeof(pred));
    int ans=0;
    for(int i=0; i<n; i++)
    {
        memset(visx,0,sizeof(visx));
        memset(visy,0,sizeof(visy));
        if(match(i)) ans++;
    }
    return ans;
}
int gg[6];
int ch2=0,ch3=0;
void dfs2(int cur,int n,int st)
{
    if(cur==n||ch3==1) return ;
    int now=gg[cur];
    int qq=0;
    for(int i=0;i<n;i++) if(mp[now][i])
    {
        if((st&(1<<i))==0)
        {
            dfs2(cur+1,n,st|(1<<i));
            qq=1;
        }
    }
    if(qq==0) ch3=1;

}
void dfs(int cur,int n,int st)
{
    //if(ch2==1) return ;
    if(cur==n)
    {
        ch3=0;
        dfs2(0,n,0);
        if(ch3==1) ch2=1;
        return ;
    }
    for(int i=0;i<n;i++) if((st&(1<<i))==0)
    {
        gg[cur]=i;
        dfs(cur+1,n,st|(1<<i));
    }
}
main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        int cnt=0;
        for(int i=0;i<n;i++)
        {
            scanf("%s",s[i]);
            int len=strlen(s[i]);
            for(int j=0;j<len;j++) if(s[i][j]=='0') cnt++;
        }
        memset(pre,0,sizeof(pre));
        for(int i=0;i<(1<<cnt);i++)
        {
            int ct=0;
            for(int j=0;j<cnt;j++) if(i&(1<<j)) ct++;
            pre[ct].push_back(i);
        }
        int ans;
        for(int i=0;i<=cnt;i++)
        {
            int ch=0;
            for(int j=0;j<pre[i].size();j++)
            {
                memset(mp,0,sizeof(mp));
                int u=pre[i][j];
                int d=0;
                for(int x=0;x<n;x++)
                for(int y=0;y<n;y++)
                {
                    if(s[x][y]=='1') mp[x][y]=1;
                    else
                    {
                        if(u&(1<<d)) mp[x][y]=1;
                        d++;
                    }
                }

                if(hung()!=n) continue;
                ch2=0;
                dfs(0,n,0);
                if(ch2==0)
                {
                    ch=1;break;
                }

            }
            if(ch==1)
            {
                ans=i;break;
            }
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
}
