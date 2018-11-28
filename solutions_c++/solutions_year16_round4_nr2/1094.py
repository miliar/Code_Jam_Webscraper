//#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cctype>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
#include <queue>
#include <stack>
#include <vector>
#include <deque>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
typedef pair< PI, int> PII;
#define lson l, m
#define rson m+1, r
const double eps=1e-5;
const int inf=1e5;
const double pi=acos(-1.0);
const int N=1e5+10;
const int mod=1e9+7;
//#pragma comment(linker, "/STACK:10240000,10240000")
#ifdef _WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif
LL quick(LL a, LL b, LL mod){LL ans=1;while(b){if(b & 1)ans=ans*a%mod;a=a*a%mod;b>>=1;}return ans%mod;}
inline int read(){char ch=' ';int ans=0;while(ch<'0' || ch>'9')ch=getchar();while(ch<='9' && ch>='0'){ans=ans*10+ch-'0';ch=getchar();}return ans;}
inline void print(LL x){printf(LLD, x);puts("");}
inline void read(double &x){char c = getchar();while(c < '0') c = getchar();x = c - '0'; c = getchar();while(c >= '0'){x = x * 10 + (c - '0'); c = getchar();}}
int lowbit(int x)
{
    return x&(-x);
}
void add(int x, int t)
{
//    for(;x<N*3;x+=lowbit(x))
//        sum[t][x]++;
}
LL get(int x, int t)
{
    LL ans=0;
//    for(;x>0;x-=lowbit(x))
//        ans+=sum[t][x];
    return ans;
}
int fact[N], inv[N];
int binpow(int a, int k)
{
    if(k == 0) return 1;
    int ans = binpow(a, k / 2);
    ans = 1ll * ans * ans % mod;
    if(k % 2) ans = 1ll * ans * a % mod;
    return ans;
}

LL C(int n, int k)
{
    if(k > n) return 0;
    LL ans = fact[n] * 1ll * inv[k] % mod;
    ans = 1ll * ans * inv[n-k] % mod;
    return ans;
}

void pre()
{
    fact[0] = inv[0] = 1;
    for(int i = 1; i < N; i++)
    {
        fact[i] = 1LL * i * fact[i-1] % mod;
        inv[i] = binpow(fact[i], mod-2);
    }
}
//======================================
int num[N<<2];
void pushup(int rt)
{
    num[rt]=max(num[rt<<1],num[rt<<1|1]);
}
void build(int l, int r, int rt)
{
    if(l==r)
    {
        scanf("%d", &num[rt]);
        return ;
    }
    int m=(l+r)>>1;
    build(lson, rt<<1);
    build(rson, rt<<1|1);
    pushup(rt);
}
void update(int p, int ma, int l, int r, int rt)
{
    if(l==r)
    {
        num[rt]=ma;
        return ;
    }
    int m=(l+r)>>1;
    if(p<=m)
        update(p, ma, lson, rt<<1);
    else
        update(p, ma, rson, rt<<1|1);
    pushup(rt);
}
int query(int L, int R, int l, int r, int rt)
{
    if(L<=l && R>=r)
        return num[rt];
    int m=(l+r)>>1;
    int ret=0;
    if(L<=m)
        ret=max(ret, query(L, R, lson, rt<<1));
    if(m<R)
        ret=max(ret, query(L, R, rson, rt<<1|1));
    return ret;
}
//=============================================
int L[N<<5], R[N<<5], sum[N<<5];
int tot;
int T[N], Hash[N];
int build(int l, int r)
{
    int rt=(++tot);
    sum[rt]=0;
    if(l<r)
    {
        int m=(l+r)>>1;
        L[rt]=build(lson);
        R[rt]=build(rson);
    }
    return rt;
}

int update(int pre, int l, int r, int x)
{
    int rt=(++tot);
    L[rt]=L[pre], R[rt]=R[pre], sum[rt]=sum[pre]+1;
    if(l<r)
    {
        int m=(l+r)>>1;
        if(x<=m)
            L[rt]=update(L[pre], lson, x);
        else
            R[rt]=update(R[pre], rson, x);
    }
    return rt;
}

int queryk(int u, int v, int l, int r, int k)
{
    if(l>=r)
        return l;
    int m=(l+r)>>1;
    int num=sum[L[v]]-sum[L[u]];
    if(num>=k)
        return queryk(L[u], L[v], lson, k);
    else
        return queryk(R[u], R[v], rson, k-num);
}

//===============================================================================

int main()
{

    return 0;
}
