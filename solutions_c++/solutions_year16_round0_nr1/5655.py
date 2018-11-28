/*
Bismillah ir-Rahman ir-Rahim
Author ::NAZMUS SAKIB
MIST......CSE-12
I WILL NEVER LOOSE HOPE INSHA ALLAH
*/
#pragma comment(linker, "/STACK:320000000")

#include <bits/stdc++.h>

using namespace std;

#define mem(a)  memset(a,0,sizeof(a))
#define mems(a) memset(a,-1,sizeof(a))
#define pb      push_back
#define SZ(a)   ((int)a.size())
#define SQR(x)  ((x)*(x))
#define IT      iterator
#define ff      first
#define ss      second
#define MP      make_pair
#define ALL(p)  p.begin(),p.end()
#define MOD     1000000007ll
#define LL      long long

const double EPS=1e-9;
const int INF=0x7f7f7f7f;
const double PI=acos(-1.0);

template< class T > inline T Abs(T n) { return ((n) < 0 ? -(n) : (n)); }
template< class T > inline T Max(T x, T y) {return (((y-x)>>(32-1))&(x^y))^y;}
template< class T > inline T Min(T x, T y) {return (((y-x)>>(32-1))&(x^y))^x;}
template< class T > inline T Swap(T &a, T &b) { a=a^b;b=a^b;a=a^b;}
template< class T > inline T gcd(T a, T b) { return (b) == 0 ? (a) : gcd((b), ((a) % (b))); }
template< class T > inline T lcm(T a, T b) { return ((a) / gcd((a), (b)) * (b)); }
template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

struct an
{
    int a;
    int d;
    bool operator <(const an &t) const
    {
        return d<t.d;
    }
};

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long long int i,j,k,t,n,a[20];
    scanf("%lld",&t);
    for(j=1;j<=t;j++)
    {
        memset(a,0,sizeof(a));
        int cnt=0,flag=0;
        scanf("%lld",&n);
        printf("Case #%lld: ",j);
        for(i=1;i<=100000;i++)
        {
            k=i*n;
            while(k>0)
            {
                if(cnt==10)break;
                if(a[k%10]==0)
                {
                    a[k%10]=1;
                    cnt++;
                }
                k/=10;
            }
            if(cnt==10)
            {
                flag=1;
                break;
            }
        }
        if(flag==1)printf("%lld\n",i*n);
        else printf("INSOMNIA\n");
    }
    return 0;
}
