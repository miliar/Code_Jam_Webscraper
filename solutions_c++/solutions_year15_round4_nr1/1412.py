#include <iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
char maz[105][105];
int T,R,C;
bool Find(int x,int y)
{
    if(maz[x][y]=='<')
    {
        for(int i=y-1;i>=1;i--)
            if(maz[x][i]!='.') return true;
    }
    if(maz[x][y]=='>')
    {
        for(int i=y+1;i<=C;i++)
            if(maz[x][i]!='.') return true;
    }
    if(maz[x][y]=='^')
    {
        for(int i=x-1;i>=1;i--)
            if(maz[i][y]!='.') return true;
    }
    if(maz[x][y]=='v')
    {
        for(int i=x+1;i<=R;i++)
            if(maz[i][y]!='.') return true;
    }
    return false;
}
bool canfind(int x,int y)
{
    for(int i=y-1;i>=1;i--)
        if(maz[x][i]!='.') return true;
    for(int i=y+1;i<=C;i++)
        if(maz[x][i]!='.') return true;
    for(int i=x-1;i>=1;i--)
        if(maz[i][y]!='.') return true;
    for(int i=x+1;i<=R;i++)
        if(maz[i][y]!='.') return true;
    return false;
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%d%d",&R,&C);
        for(int i=1;i<=R;i++) scanf("%s",maz[i]+1);
        int res=0;
        bool ok=true;
        for(int i=1;i<=R;i++)
            for(int j=1;j<=C;j++)
        {
            if(maz[i][j]!='.')
            {
                if(Find(i,j)) continue;
                if(canfind(i,j)) res++;
                else ok=false;
            }
        }
        if(ok)
            printf("Case #%d: %d\n",kase,res);
        else
            printf("Case #%d: IMPOSSIBLE\n",kase);
    }
    return 0;
}
