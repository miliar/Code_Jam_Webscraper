#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<utility>
#include<iomanip>
#include<queue>
using namespace std;

#define LL long long int
#define uLL unsigned long long int

#define S(a) scanf("%d",&a)
#define S2(a,b) scanf("%d%d",&a,&b)
#define S3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define SLL(a) scanf("%lld",&a)
#define SLL2(a,b) scanf("%lld%lld",&a,&b)
#define SLL3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define SC(a) scanf("%c",&a)
#define P(a) printf("%d",a)
#define PS(a) printf("%s",a)
#define PLL(a) printf("%lld",a)
#define PCASE(kk) printf("Case #%d: ",kk++)
#define PCASENL(kk) printf("Case %d:\n",kk++)
#define NL puts("")

#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define pi (2.0*acos(0.0))
#define pii pair<int,int>

template<typename T>inline T POW(T B, T P)
{
    if (P == 0) return 1;
    if (P & 1) return B * POW(B, P - 1);
    else return SQR(POW(B, P / 2));
}
template <typename T>inline T ModInv (T b, T m)
{
    return BigMod(b, m - 2, m);
}
template<typename T>inline T ABS(T a)
{
    if (a < 0)return -a;
    else return a;
}
template<typename T>inline T gcd(T a, T b)
{
    if (a < 0)return gcd(-a, b);
    if (b < 0)return gcd(a, -b);
    return (b == 0) ? a : gcd(b, a % b);
}
template<typename T>inline T lcm(T a, T b)
{
    if (a < 0)return lcm(-a, b);
    if (b < 0)return lcm(a, -b);
    return a * (b / gcd(a, b));
}
template <class T> inline T BMOD(T p, T e, T m)
{
    T ret = 1;
    while (e)
    {
        if (e & 1) ret = (ret * p) % m;
        p = (p * p) % m;
        e >>= 1;
    }
    return (T)ret;
}

//for(__typeof(pp.begin()) i=pp.begin(); i!=pp.end(); i++ )

//knight and king move....



//int Dx[]={-2,-1,1,2,1,2,-2,-1};
//int Dy[]={-1,-2,2,1,-2,-1,1,2};
//int dx[]={-1,1,0,0};
//int dy[]={0,0,-1,1};
//int dx[]= {-1,-1,0,0,1,1};
//int dy[]= {-1,0,-1,1,0,1};
//////////////////////////////////////////////////

LL n,ar[12];

void func(LL x)
{
    LL tmp=x;
    while(tmp)
    {
        LL tt=tmp;
        LL t=tt%10;
        ar[t]=1;
        tmp/=10;
    }
    return ;
}

int main()
{
    freopen("A-large.in", "r", stdin);
	freopen("A-large1.out", "w", stdout);


    int t,tc=1;
    S(t);
    while(t--)
    {
        SLL(n);
        for(int i=0;i<=9;i++)ar[i]=0;
        LL tmp1=0;
        int i=0;

        PCASE(tc);
        for(i=1;i<=100000;i++)
        {
            int fl=1;
            tmp1=n*(LL)i;
            func(tmp1);
            for(int j=0;j<=9;j++)
            {
                if(ar[j]==0)
                {
                    fl=0;break;
                }
            }
            if(fl==1)break;
        }
//        P(i),NL;
        if(n==0 || i==100001)
        {
            printf("INSOMNIA\n");
        }
        else PLL(tmp1),NL;
    }
    return 0;
}
