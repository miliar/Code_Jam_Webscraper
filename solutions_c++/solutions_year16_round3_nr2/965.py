#include <bits/stdc++.h>

#define S scanf
#define P printf

#define LL long long int
#define ULL unsigned long long int
#define D double

#define all(a) a.begin(),a.end()
#define X  first
#define Y  second
#define MP make_pair
#define NL P("\n")

#define S1(a)      scanf("%d",&a)
#define S2(a,b)    scanf("%d%d",&a,&b)
#define S3(a,b,c)  scanf("%d%d%d",&a,&b,&c)
#define SL1(a)     scanf("%lld",&a)
#define SL2(a,b)   scanf("%lld%lld",&a,&b)
#define SL3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define CHR        getchar()
#define PB(x)      push_back(x)
#define PS(x)      push(x)
#define UB         upper_bound
#define LB         lower_bound
#define mxe(a,n)   (*max_element(a,a+n))
#define mne(a,n)   (*min_element(a,a+n))
#define SUM(a,n)   (accumulate(a,a+n,0))
#define countbit(x) __builtin_popcount(x)
#define DBG(n)      P("Done %d\n",n);

// I/O

#define FS(x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)

#define MEM(a,val) memset(a,val,sizeof(a));
#define SET(a)     memset(a,-1,sizeof a)
#define CLR(a)     memset(a,0,sizeof a)
#define CMPL       cerr<< "Compilation Process Finished\n";cerr<< "----------------------------\n"

using namespace std;

template <typename T> T BigMod (T b,T p,T m){if (p == 0) return 1;if (p%2 == 0){T s = BigMod(b,p/2,m);return ((s%m)*(s%m))%m;}return ((b%m)*(BigMod(b,p-1,m)%m))%m;}
template <typename T> T ModInv (T b,T m){return BigMod(b,m-2,m);}
template <typename T> T in(){char ch;T n = 0;bool ng = false;while (1){ch = getchar();if (ch == '-'){ng = true;ch = getchar();break;}if (ch>='0' && ch<='9')     break;}while (1){n = n*10 + (ch - '0');ch = getchar();if (ch<'0' || ch>'9')   break;}return (ng?-n:n);}
template <typename T> T POW(T B,T P){ if(P==0) return 1; if(P&1) return B*POW(B,P-1);  else return SQR(POW(B,P/2));}
template <typename T> T Bigmod(T b,T p,T m){ if(p==0) return 1; else if (!(p&1)) return SQR(Bigmod(b,p/2,m)) % m;else return ((b % m) * Bigmod(b,p-1,m)) % m;}
template <typename T> T Dis(T x1,T y1,T x2, T y2){return sqrt( SQR(x1-x2) + SQR(y1-y2) );}
template <typename T> T Angle(T x1,T y1,T x2, T y2){ return atan( double(y1-y2) / double(x1-x2));}
template <typename T> T DIFF(T a,T b) { T d = a-b;if(d<0)return -d;else return d;}
template <typename T> T ABS(T a) {if(a<0)return -a;else return a;}
template <typename T> T gcd(T a,T b){if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template <typename T> T lcm(T a,T b) {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template <typename T> T euclide(T a,T b,T &x,T &y) {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}   if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}   if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
template <typename T> void ia (T a[],int n){for (int i=0; i<n; i++) cin >> a[i];}
template <typename T> void pa (T a[],int n){for (int i=0; i<n-1; i++) cout << a[i] << " ";cout << a[n-1] << endl;}
template <typename T> LL isLeft(T a,T b,T c) { return (a.x-b.x)*(b.y-c.y)-(b.x-c.x)*(a.y-b.y); }

int    Set(int N,int pos){ return N=N | (1<<pos);}
int  Reset(int N,int pos){return N= N & ~(1<<pos);}
bool Check(int N,int pos){return (bool)(N & (1<<pos));}
template< class T, class X > inline T   togglebit(T a, X i) { T t=1;return (a^(t<<i)); }

#define VI  vector< int >
#define VII vector< VI >
#define VLL vector< LL >
#define PII pair< int , int >
#define PLL pair< LL , LL >
#define VPI vector< PII >

///         0123456789
#define MX  57
#define MOD 1000000007
#define INF (1<<30)-1+(1<<30)
#define eps 1e-9

#define base ((1<<l)-1)
#define lft (idx<<1)
#define rgt (lft|1)
#define mid ((l+r)>>1)

/// Hashing Bases & MOD
///           0123456789
#define Base1 10000019ULL
#define Base2 10000079ULL
#define Base3 10000103ULL
#define MOD1  1000000007ULL
#define MOD2  1000000009ULL
#define MOD3  1000000021ULL
#define LOGX  17

int p[MX];
int mat[MX][MX];
int pth;
LL DP[MX];

void Back(int x,int l){
    if (!pth)   return;
    p[l] = x;

    if (x == 1){
        for (int i=l;i;i--){
            mat[ p[i] ][ p[i-1] ] = 1;
//            cout << p[i] << " ";
        }
//        cout << p[0] << endl;

        pth --;
        return ;
    }

    for (int i=1;i<x;i++){
        Back(i,l+1);
    }
}

int main(){
    int t,cs = 0;
    S("%d",&t);

    while(t--){
        int n,m;

        S("%d%d",&n,&m);

        DP[n] = 1;
        memset(mat,0,sizeof mat);

        for (int i=n-1;i;i--){
            DP[i] = 0;
            for (int j=i+1;j<=n;j++){
                DP[i] += DP[j];
            }

//            cout << i << ": " << DP[i] << endl;
        }

        for (int i=2;i<=n;i++){
            if (m >= DP[i]){
                mat[1][i] = 1;
                m -= DP[i];

                for (int j=i;j<=n;j++){
                    for (int k=j+1;k<=n;k++)
                        mat[j][k] = 1;
                }
            }
        }

        P("Case #%d: ",++cs);

        if (m)    puts("IMPOSSIBLE");
        else{
            puts("POSSIBLE");
            for (int i=1;i<=n;i++){
                for (int j=1;j<=n;j++)
                    P("%d",mat[i][j]);
                NL;
            }
        }
    }
return 0;
}
