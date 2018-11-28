#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int n,m;
char w[105][105];
bool fu(int x,int y)
{
    int i=x-1;
    while(i)
    {
        if(w[i][y]!='.')return true;
        i--;
    }
    return false;
}
bool fd(int x,int y)
{
    int i=x+1;
    while(i<=n)
    {
        if(w[i][y]!='.')return true;
        i++;
    }
    return false;
}
bool fl(int x,int y)
{
    int j=y-1;
    while(j)
    {
        if(w[x][j]!='.')return true;
        j--;
    }
    return false;
}
bool fr(int x,int y)
{
    int j=y+1;
    while(j<=m)
    {
        if(w[x][j]!='.')return true;
        j++;
    }
    return false;
}
int work()
{
    int tot=0;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            if(w[i][j]!='.')
            {
                int p,q;
                q=fl(i,j)|fr(i,j)|fd(i,j)|fu(i,j);
                //cout<<i<<' '<<j<<' '<<q<<endl;
                if(w[i][j]=='^')
                {
                    p=fu(i,j);
                    if(!p)
                    {
                        if(!q)return -1;
                        tot++;
                    }
                }
                else if(w[i][j]=='v')
                {
                    p=fd(i,j);
                    if(!p)
                    {
                        if(!q)return -1;
                        tot++;
                    }
                }
                else if(w[i][j]=='<')
                {
                    p=fl(i,j);
                    if(!p)
                    {
                        if(!q)return -1;
                        tot++;
                    }
                }
                else if(w[i][j]=='>')
                {
                    p=fr(i,j);
                    if(!p)
                    {
                        if(!q)return -1;
                        tot++;
                    }
                }
            }
    return tot;
}
void Solve()
{
    int T,cnt=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++)
            scanf(" %s",w[i]+1);
        printf("Case #%d: ",++cnt);
        int ans=work();
        if(ans==-1)printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    Solve();
    return 0;
}
