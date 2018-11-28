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
#define ULL unsigned LL
#define PI 2.0*acos(0.0)
#define D double
#define sz size()
#define PB push_back
#define cp printf("here\n");
#define NL printf("\n")
#define CHR getchar()
#define SQR(n) (n*n)
#define MEM(a,val) memset(a,val,sizeof(a))
#define Max(a,b) ((a>b)?a:b)
#define Min(a,b) ((a<b)?a:b)
#define _Max(a,b,c) Max(a,Max(b,c))
#define _Min(a,b,c) Min(a,Min(b,c))
#define S1(a) a=in<int>()
#define S2(a,b) a=in<int>(),b=in<int>()
#define S3(a,b,c) a=in<int>(),b=in<int>(),c=in<int>()
#define SL1(a) a=in<LL>()
#define SL2(a,b) a=in<LL>(),b=in<LL>()
#define SL3(a,b,c) a=in<LL>(),b=in<LL>(),c=in<LL>()
#define F(i,a,b) for(int i=a;i<b; i++)
#define R(i,a,b) for(int i=a-1;i>=b; i--)
#define all(a) a.begin(),a.end()
#define cnt_bit(a) __builtin_popcountll(a)
#define InpOut freopen("B-large.in","r",stdin),freopen("A1.out","w",stdout)
#define _cin ios_base::sync_with_stdio(0)
#include <time.h>

using namespace std;
template <typename T> T in(){char ch;T n = 0;bool ng = false;while (1){ch = getchar();if (ch == '-'){ng = true;ch = getchar();break;}if (ch>='0' && ch<='9')     break;}while (1){n = n*10 + (ch - '0');ch = getchar();if (ch<'0' || ch>'9')   break;}return (ng?-n:n);}
template<typename T>inline T Dis(T x1,T y1,T x2, T y2){return sqrt( SQR(x1-x2) + SQR(y1-y2) );}


///         0123456789
#define MX  1007
#define MOD 1000000007
#define INF (1<<28)
#define eps 1e-9

/// ==========================================////

int ar[MX],dp[MX][MX];
int N;

int Dfs(int n,int m)
{
    if(dp[n][m]!=-1) return dp[n][m];
    if(n<=m) return 0;
    else return dp[n][m]=1+Dfs(n-m,m);
}

int Solve(int n)
{
    int sum=n;
    F(i,1,N+1)
    {
        sum+=Dfs(ar[i],n);
    }

    return sum;
}

int main()
{
    InpOut;
    int t;
    MEM(dp,-1);
    S1(t);

    F(cs,1,t+1)
    {
        int n;
        S1(n);
        N=n;
        int ans=INF,mx=0;

        F(i,1,n+1)
        {
            S1(ar[i]);
            mx=max(mx,ar[i]);
        }
        F(i,1,mx+1)
        {
            ans=min(ans,Solve(i));
        }
        printf("Case #%d: %d\n",cs,ans);
    }

    return 0;
}
