//#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <bitset>
#include <string>
using namespace std;
double esp=1e-11;
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define cle(a) while(!a.empty())a.pop()
#define mem(p) memset(p,0,sizeof(p))
#define memf(p) memset(p,0x3f,sizeof(p))
#define memn(p) memset(p,-1,sizeof(p))
#define mp(A, B) make_pair(A, B)
#define pb push_back
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
typedef long long int LL;
const double PI = acos(-1.0);
const LL INF=0x3f3f3f3f3f3f3f3f;
const LL MOD = 1000000009ll;
const int maxn =110;
int ans[maxn],tem[maxn];
int T,n,r,p,s;
int ch(int a,int b)
{
    if(a!=1&&b!=1)return 2;
    if(a!=0&&b!=0)return 1;
    return 0;
}
int check()
{
    for(int x=1;x<=(1<<n);x++)tem[x]=ans[x];
    for(int x=n;x>=1;x--)
    {
        for(int y=1;y<=(1<<(x-1));y++)
        {
            if(tem[2*y-1]==tem[2*y])return 0;
            tem[y]=ch(tem[2*y-1],tem[2*y]);
        }
    }
    return 1;
}
int dfs(int t)
{
    if(t>(1<<n))
        return check();
    if(p>0)
    {
        p--;
        ans[t]=0;
        if(dfs(t+1))return 1;
        p++;
    }
    if(r>0)
    {
        r--;
        ans[t]=1;
        if(dfs(t+1))return 1;
        r++;
    }
    if(s>0)
    {
        s--;
        ans[t]=2;
        if(dfs(t+1))return 1;
        s++;
    }
    return 0;
}
int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    //map<long long int,int>ma;                 %I64d
    //vector<int>::iterator iter;
    //memset(m,0,sizeof(int));               for(iter=trtr[rt].begin();iter!=trtr[rt].end();iter++)
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d%d",&a,&b);
    //scanf("%d",&n);
    //printf("%d\n",ans);
    scanf("%d",&T);
    for(int gg=1;gg<=T;gg++)
    {
        scanf("%d%d%d%d",&n,&r,&p,&s);
        printf("Case #%d: ",gg);
        if(dfs(1))
        {
            for(int x=1;x<=(1<<n);x++)
                if(ans[x]==0)
                    putchar('P');
                else if(ans[x]==1)
                    putchar('R');
                else
                    putchar('S');
            putchar('\n');
        }
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
