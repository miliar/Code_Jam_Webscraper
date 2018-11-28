/// *********************************************** K
/// B *                                           * H
/// I *    Solved By : Bir Bahadur Khatri(B'ru)   * A
/// R *      Be Positive,be Happy.                * T
/// U *                                           * R
/// *********************************************** I

#include<bits/stdc++.h>

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

#define _cin ios_base::sync_with_stdio(0)
#include <time.h>

using namespace std;
template <typename T> T in(){char ch;T n = 0;bool ng = false;while (1){ch = getchar();if (ch == '-'){ng = true;ch = getchar();break;}if (ch>='0' && ch<='9')     break;}while (1){n = n*10 + (ch - '0');ch = getchar();if (ch<'0' || ch>'9')   break;}return (ng?-n:n);}
template<typename T>inline T Dis(T x1,T y1,T x2, T y2){return sqrt( SQR(x1-x2) + SQR(y1-y2) );}
template<typename T>inline T POW(T B,T P){ if(P==0) return 1; if(P&1) return B*POW(B,P-1);  else return SQR(POW(B,P/2));}


///         0123456789
#define MX  1007
#define MOD 1000000007
#define INF (1<<28)
#define eps 1e-9
#define InpOut freopen("C-small-attempt0 (1).in","r",stdin),freopen("A1.out","w",stdout)

/// ==========================================////

int coin[1009],dp[MX],ar[1009],N;

int ISOk(int n)
{
    F(i,1,n+1) if(dp[i]==INF) return 0;
    return 1;
}

int Solve(int mask)
{
    F(i,1,N+1) ar[i]=dp[i];
    F(i,1,17)
    {
        if(mask&(1<<i)) {
            for(int j=N;j>=1;j--) {
                if(j-i>=0&&ar[j-i]!=INF&&ar[j]==INF) {
                    ar[j]=0;
                }
            }
        }
    }
    F(i,1,N+1) if(ar[i]==INF) return INF;
    return cnt_bit(mask);
}

int main()
{
    InpOut;
    int t;
    S1(t);

    F(cs,1,t+1)
    {
        int c,n,m;
        S3(c,n,m);

        F(j,1,n+1) S1(coin[j]);

        F(j,1,m+1) dp[j]=INF;
        dp[0]=0;
        N=m;
        F(j,1,n+1)
        {
            F(k,1,m+1)
            {
                if(dp[k]!=INF) dp[k]=0;
            }
            F(k,coin[j],m+1)
            {
                if(dp[k]!=0)
                {
                    if(dp[k]>=dp[k-coin[j]]&&dp[k-coin[j]]<1)
                    {
                        dp[k]=dp[k-coin[j]]+1;
                    }
                }
            }
        }

        int ans=INF;
        F(i,0,(1<<16)+1)
        {
            ans=min(ans,Solve(i));
        }
        printf("Case #%d: %d\n",cs,ans);
    }

    return 0;
}

///============= Thank You ===================///
