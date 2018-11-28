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
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,k,cnt,t;
    string s;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        cin>>s;
        printf("Case #%d: ",j);
        int neg=0,pos=0;
        cnt=0;
        for(i=0;i<s.length();i++)
        {
            if(i==0)
            {
                if(s[i]=='+')pos=1;
                else neg=1;
            }
            else if(s[i]=='+'&&pos==0)
            {
                cnt++;
                pos=1;
                neg=0;
            }
            else if(s[i]=='-'&&neg==0)
            {
                cnt++;
                pos=0;
                neg=1;
            }
        }
        if(neg==1)cnt++;
        printf("%d\n",cnt);
    }
    return 0;
}
