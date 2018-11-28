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
#define eps 1e-9
#define MX 100007

/// ==========================================////

int ar[100][100],br[100][100],ans,vis[100];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("outputA.txt","w",stdout);

    int t;
    S1(t);

    F(i,0,t)
    {
        MEM(vis,0);
        int a;
        S1(a);
        F(j,1,5)
        {
            F(k,1,5)
            {
                S1(ar[j][k]);
            }
        }
        int b;
        S1(b);
        F(j,1,5)
        {
            F(k,1,5)
            {
                S1(br[j][k]);
            }
        }

        set<int> S;
        S.clear();
        F(j,1,5)
        {
            S.insert(ar[a][j]);
            vis[ar[a][j]]=1;
        }
        F(j,1,5)
        {
            S.insert(br[b][j]);
            if(vis[br[b][j]]==1)
            {
                ans=br[b][j];
            }
        }
        printf("Case #%d: ",i+1);
        int man=S.sz;
        if(man==8)
        {
            printf("Volunteer cheated!\n");
        }
        else if(man<7)
        {
            printf("Bad magician!\n");
        }
        else
        {
            printf("%d\n",ans);
        }
    }

    return 0;
}

///============= Thank You ===================///
