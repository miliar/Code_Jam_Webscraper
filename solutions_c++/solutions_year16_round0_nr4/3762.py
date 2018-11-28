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

int main()
{
//    freopen("in.txt","r",stdin);
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    long long int i,j,k,c,s,t;
    scanf("%lld",&t);
    for(j=1;j<=t;j++)
    {
        printf("Case #%lld: ",j);
        scanf("%lld %lld %lld",&k,&c,&s);
        if(c==1)
        {
            for(i=1;i<=k;i++)
            {
                if(i==1)printf("%lld",i);
                else printf(" %lld",i);
            }
            printf("\n");
        }
        else if(k==1)printf("1\n");
        else
        {
            for(i=2;i<=k;i++)
            {
                if(i==2)printf("%lld",i);
                else printf(" %lld",i);
            }
            printf("\n");
        }
    }
    return 0;
}

