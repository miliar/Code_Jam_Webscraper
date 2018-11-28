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
const int maxn =300;
double p[maxn],ans=0,ch[maxn],tem;
int n,k,len;
void df(double l,int c,int t)
{
    if(t>k)
    {
        if(c==k/2)tem+=l;
        return;
    }
    if(c<k/2)
    {
        df(l*ch[t],c+1,t+1);
    }
    df(l*(1.0-ch[t]),c,t+1);
}
double check()
{
    tem=0;
    df(1,0,1);
    return tem;
}
void dfs(int t)
{
    if(t>n)
    {
        if(len==k)ans=max(ans,check());
        return ;
    }
    if(len<k)
    {
        len++;
        ch[len]=p[t];
        dfs(t+1);
        len--;
    }
    dfs(t+1);
    if(len==k)ans=max(ans,check());
}
int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    //map<long long int,int>ma;                 %I64d
    //vector<int>::iterator iter;
    //memset(m,0,sizeof(int));               for(iter=trtr[rt].begin();iter!=trtr[rt].end();iter++)
    //for(int x=1;x<=n;x++)
    //for(int y=1;y<=n;y++)
    //scanf("%d%d",&a,&b);
    //scanf("%d",&n);
    //printf("%d\n",ans);
    int T;
    scanf("%d",&T);
    for(int gg=1;gg<=T;gg++)
    {
        scanf("%d%d",&n,&k);
        for(int x=1;x<=n;x++)
            scanf("%lf",&p[x]);
        sort(p+1,p+n+1);
        ans=0;
        len=0;
        dfs(1);
        printf("Case #%d: %.6f\n",gg,ans);
    }
    return 0;
}
