/*

To believe is to know that every day

is a new beginning.

It is to trust that miracles happen,

and dreams really do come true.

To believe is to know that wonderful surprises

are just waiting to happen.

And all our hopes and dreams are within reach.

If only we believe.

*/
#include<bitset>
#include<map>
#include<vector>
#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>
#include<stack>
#include<queue>
#include<set>
#define inf 0x3f3f3f3f
#define mem(a,x) memset(a,x,sizeof(a))
#define F first
#define S second
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;

inline int in()
{
    int res=0;char c;int f=1;
    while((c=getchar())<'0' || c>'9')if(c=='-')f=-1;
    while(c>='0' && c<='9')res=res*10+c-'0',c=getchar();
    return res*f;
}
const int N=1010,MOD=1e9+7;
ll state[N];

ll zhuanhuan(ll x,int base,int n)
{
    ll ret=0;
    for(int i=n-1;i>=0;i--)
    {
        if(x&1<<i) ret=ret*base+1;
        else ret*=base;
    }
    return ret;
}

bool is_prime(ll n)
{
    for(ll i=2;i*i<=n;i++)
    {
        if(n%i==0) return 0;
    }
    return 1;
}

bool ok(int x,int n)
{
    if(!(x&1)) return 0;
    if(!(x&1LL<<(n-1))) return 0;
    for(int i=2;i<=10;i++)
    {
        ll now=zhuanhuan(x,i,n);
        if(is_prime(now)) return 0;
    }
    return 1;
}
ll getYinzi(int x,int base,int n)
{
    ll now=zhuanhuan(x,base,n);
    //cout<<"base=="<<base<<" now=="<<now<<endl;
    for(ll i=2;i*i<=now;i++)
    {
        if(now%i==0) return i;
    }
    return -inf;
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T=in(),ca=1;
    while(T--)
    {
        int n=in(),m=in();
        ll all=1LL<<n;
        int cnt=0;
        for(ll i=(1LL<<(n-1))+1;i<all;i+=2)
        {
            if(ok(i,n))
            {
                 state[cnt++]=i;
                 if(cnt==m) break;
            }
        }
        printf("Case #%d:\n",ca++);

        for(int i=0;i<cnt;i++)
        {
            for(int j=n-1;j>=0;j--)
            {
                if(state[i]&1LL<<j) putchar('1');
                else putchar('0');
            }
            putchar(' ');
            for(int j=2;j<=10;j++)
            {
                printf("%I64d%c",getYinzi(state[i],j,n),j==10?'\n':' ');
            }
        }
    }
    return 0;
}
