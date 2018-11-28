#include<cstdio>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<cstring>
using namespace std;
#define L(x) tree[x].ch[0]
#define R(x) tree[x].ch[1]
#define INF 0x7fffffff
#define inf 99999999.9
#define eps 1e-9
#define MAXN 100015
#define db double
#define op operator
#define cp const P&
#define cs const
typedef __int64 ll;
ll prim[50] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,
100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,
10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,
1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,
1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
int ser(ll x){
    int l = 0,r = 39;
    while(l < r){
        int m = (l+r)>>1;
        if(prim[m] > x) r = m;
        else l = m + 1;
    }
    return l;
}
int main()
{
    //freopen("C-large-1.in","r",stdin);
    //freopen("C-large-1.out","w",stdout);
    int T,cas = 1;
    ll a,b;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%I64d%I64d",&a,&b);
        printf("Case #%d: %d\n",cas ++,ser(b) - ser(a-1));
    }
return 0;
}
