//GCJ round 2 A
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#define MAXN 105
#define INF 1000000000
#define eps 1e-6
using namespace std;
char c[MAXN][MAXN];
bool v[MAXN][MAXN];
bool yf;
int cnt,R,C;
bool f(int x,int y)
{
    bool tmp=0;
    if(c[x][y]!='.')
    {

        for(int i=1;i<=R;++i)
        {
            if(c[i][y]!='.'&&i!=x) tmp=1;
        }
        for(int i=1;i<=C;++i)
        {
            if(c[x][i]!='.'&&i!=y) tmp=1;
        }
    }
    if(tmp) return true;
    else return false;
}
void BT(int x,int y)
{
    bool tmp=0;
    if(c[x][y]=='^')
    {
        for(int i=1;i<x;++i)
        {
            if(c[i][y]!='.')
                tmp=1;
        }
        if(tmp==0) cnt++;
    }
    if(c[x][y]=='v')
    {
        for(int i=x+1;i<=R;++i)
        {
            if(c[i][y]!='.')
                tmp=1;
        }
        if(tmp==0) cnt++;
    }
    if(c[x][y]=='<')
    {
        for(int i=1;i<y;++i)
        {
            if(c[x][i]!='.')
                tmp=1;
        }
        if(tmp==0) cnt++;
    }
    if(c[x][y]=='>')
    {
        for(int i=y+1;i<=C;++i)
        {
            if(c[x][i]!='.')
                tmp=1;
        }
        if(tmp==0) cnt++;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int Case,T;
    scanf("%d",&Case);
    for(int T=1;T<=Case;++T)
    {
        scanf("%d%d",&R,&C);
        for(int i=1;i<=R;++i)
            scanf("%s",c[i]+1);
        memset(v,0,sizeof(v));
        yf=1;
        cnt=0;
        for(int i=1;i<=R;++i)
            for(int j=1;j<=C;++j)
                if(c[i][j]!='.'&&f(i,j)==0) yf=0;
        for(int i=1;i<=R;++i)
            for(int j=1;j<=C;++j)
                if(c[i][j]!='.') BT(i,j);
        printf("Case #%d: ",T);
        if(yf==0) printf("IMPOSSIBLE\n");
        else printf("%d\n",cnt);
    }
    return 0;
}
