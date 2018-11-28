#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<queue>
#include<vector>
#include<list>
#include<map>
#include<string>
#include<deque>
#include<set>

using namespace std;

#define LS (v<<1)
#define RS (v<<1|1)
#define MID (l+r>>1)
#define INF 0x7fffffff
#define INFL 0x7fffffffffffffffll
#define maxn 0

int egcd(int a,int b,int &x,int &y)
{
    if(b==0)
    {
        x=1,y=0;
        return a;
    }
    int c=egcd(b,a%b,x,y);
    int d=x;
    x=y;
    y=d-a/b*x;
    return c;
}
int gcd(int a,int b){return b?gcd(b,a%b):a;}
int cb[1][1];
void Combination(int len,int mod)
{
    cb[0][0]=1;
    for(int i=1;i<=len;i++)
    {
        cb[i][0]=1;
        for(int j=1;j<=len;j++)
        {
            cb[i][j]=(cb[i-1][j-1]+cb[i-1][j])%mod;
        }
    }
}

int n,m;
int mp[110][110];
int res[110][110];

int doit()
{
    int i,j,mx,mi,mj;
    mx=0;
    mi=mj=0;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf("%d",&mp[i][j]);
            if(mp[i][j]>mx)
            {
                mx=mp[i][j];
                mi=i;
                mj=j;
            }
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            res[i][j]=mx;
        }
    }
    for(i=0;i<n;i++)
    {
        if(i!=mi)
        for(j=0;j<m;j++)
        {
            res[i][j]=min(res[i][j],mp[i][mj]);
        }
    }
    for(j=0;j<m;j++)
    {
        if(j!=mj)
        for(i=0;i<n;i++)
        {
            res[i][j]=min(res[i][j],mp[mi][j]);
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(res[i][j]!=mp[i][j])
            {
                return 0;
            }
        }
    }
    return 1;
}

int main()
{
  //  freopen("B-large.in","r",stdin);
  //  freopen("B-large.out","w",stdout);
    int cas=1,t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        if(doit()) printf("Case #%d: YES\n",cas++);
        else printf("Case #%d: NO\n",cas++);
    }

    return 0;
}
