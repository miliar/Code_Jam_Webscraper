/// ===========================================///
/// B *                                       *///
/// I *    Solved By : JU_Undefined_Coder     *///
/// R *    Team Member : Bir Bahadur Khatri   *///
/// U *                                       *///
/// ===========================================///
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <list>
#define LL long long int
#define PI 2.0*acos(0.0)
#define MEM(a,val) memset(a,val,sizeof(a))

#define Max(a,b) ((a>b)?a:b)
#define Min(a,b) ((a<b)?a:b)
#define _Max(a,b,c) Max(a,Max(b,c))
#define _Min(a,b,c) Min(a,Min(b,c))
#define S1(a) scanf("%d",&a)
#define S2(a,b) scanf("%d%d",&a,&b)
#define S3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define SL1(a) scanf("%lld",&a)
#define SL2(a,b) scanf("%lld%lld",&a,&b)
#define SL3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define  F(i,a,b) for(int i=a;i<b; i++)
#define CHR getchar()
#define D double
#define sz size()
#define PB push_back
#define cp printf("here\n");
#define SQR(n) (n*n)
#define NL printf("\n")
#include <time.h>

template <typename T> T in()
{
    char ch;
    T n = 0;
    bool ng = false;
    while (1)
    {
        ch = getchar();
        if (ch == '-')
        {
            ng = true;
            ch = getchar();
            break;
        }
        if (ch>='0' && ch<='9')     break;
    }
    while (1)
    {
        n = n*10 + (ch - '0');
        ch = getchar();
        if (ch<'0' || ch>'9')   break;
    }
    return (ng?-n:n);
}
template<typename T>inline T Bigmod(T b,T p,T m)
{
    if(p==0) return 1;
    else if (!(p&1)) return SQR(Bigmod(b,p/2,m)) % m;
    else return ((b % m) * Bigmod(b,p-1,m)) % m;
}
template<typename T>inline T ABS(T a)
{
    if(a<0)return -a;
    else return a;
}
template<typename T>inline T Dis(T x1,T y1,T x2, T y2)
{
    return sqrt( SQR(x1-x2) + SQR(y1-y2) );
}
template<typename T>inline T gcd(T a,T b)
{
    if(a<0)return gcd(-a,b);
    if(b<0)return gcd(a,-b);
    return (b==0)?a:gcd(b,a%b);
}
template<typename T>inline T lcm(T a,T b)
{
    if(a<0)return lcm(-a,b);
    if(b<0)return lcm(a,-b);
    return a*(b/gcd(a,b));
}
template <typename T> T ModInv (T b,T m)
{
    return Bigmod(b,m-2,m);
}
bool isVowel(char ch)
{
    ch=toupper(ch);
    if(ch=='A'||ch=='U'||ch=='I'||ch=='O'||ch=='E') return true;
    return false;
}
template <typename T> T POW(T b,T p)
{
    if (p == 0) return 1;
    if (p%2 == 0)
    {
        T s = POW(b,p/2);
        return s*s;
    }
    return b*POW(b,p-1);
}

/// if(st<=l&&ed>=r)
using namespace std;

#define MOD 1000064507
#define INF (1<<28)
#define eps 1e-1
#define MX 100007

/// ==========================================////

D c,f,x;
map<D,D>dp;

D DP(D now,int cnt)
{

    if(cnt>=6*x) return x/now;
    D &res=dp[now];
    res=(c/now)+DP(now+f,cnt+1);
    res=min(res,x/now);
    return res;
}

int main()
{
    int t;

    freopen("B-small-attempt9.in","r",stdin);
    freopen("outputB.txt","w",stdout);
    S1(t);


    F(i,1,t+1)
    {

        scanf("%lf%lf%lf",&c,&f,&x);


        printf("Case #%d: %.10lf\n",i,DP(2.0,0));

        dp.clear();
    }

    return 0;
}

///============= Thank You ===================///

