/********************************************
*                                           *
*    Solved By : Bir Bahadur Khatri(B'ru)   *
*      Be Positive,be Happy.                *
*                                           *
*********************************************/

#define ff first
#define D double
#define sz size()
#define ss second
#define PB push_back
#define SQR(n) (n*n)
#define CHR getchar()
#define NL printf("\n")
#include<bits/stdc++.h>
#define ULL unsigned LL
#define PI 2.0*acos(0.0)
#define LL long long int
#define S1(a) a=in<int>()
#define SL1(a) a=in<LL>()
#define Max(a,b) ((a>b)?a:b)
#define Min(a,b) ((a<b)?a:b)
#define all(a) a.begin(),a.end()
#define _Max(a,b,c) Max(a,Max(b,c))
#define _Min(a,b,c) Min(a,Min(b,c))
#define SL2(a,b) a=in<LL>(),b=in<LL>()
#define F(i,a,b) for(int i=a;i<b; i++)
#define S2(a,b) a=in<int>(),b=in<int>()
#define R(i,a,b) for(int i=a-1;i>=b; i--)
#define BitCnt(a) __builtin_popcountll(a)
#define MEM(a,val) memset(a,val,sizeof(a))
#define SL3(a,b,c) a=in<LL>(),b=in<LL>(),c=in<LL>()
#define S3(a,b,c) a=in<int>(),b=in<int>(),c=in<int>()
#define cp printf("***** here here here here *****\n");
#define trace1(x)                cerr << #x << ": " << x << endl;
#define InpOut freopen("A.in","r",stdin),freopen("A1.out","w",stdout)
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;

using namespace std;
template <typename T> T in(){char ch;T n = 0;bool ng = false;while (1){ch = getchar();if (ch == '-'){ng = true;ch = getchar();break;}if (ch>='0' && ch<='9')     break;}while (1){n = n*10 + (ch - '0');ch = getchar();if (ch<'0' || ch>'9')   break;}return (ng?-n:n);}
template<typename T>inline T POW(T B,T P){ if(P==0) return 1; if(P&1) return B*POW(B,P-1);  else return SQR(POW(B,P/2));}
template<typename T>inline T Gcd(T a,T b){if(a<0)return Gcd(-a,b);if(b<0)return Gcd(a,-b);return (b==0)?a:Gcd(b,a%b);}
template<typename T>inline T Lcm(T a,T b) {if(a<0)return Lcm(-a,b);if(b<0)return Lcm(a,-b);return a*(b/Gcd(a,b));}
long long Bigmod(long long base, long long power, long long MOD){long long ret=1;while(power){if(power & 1)ret=(ret*base)%MOD;base=(base*base)%MOD;power>>=1;}return ret;}
bool isVowel(char ch){ ch=toupper(ch); if(ch=='A'||ch=='U'||ch=='I'||ch=='O'||ch=='E') return true; return false;}
long long ModInverse(long long number, long long MOD){return Bigmod(number, MOD-2, MOD);}
bool isConst(char ch){if (isalpha(ch) && !isVowel(ch)) return true; return false;}
int toInt(string s)  { int sm; stringstream ss(s); ss>>sm; return sm; }

///**********************************************************//

#define MD1 1000000007ULL
#define MD2 1000000009ULL
#define MD3 1000000021ULL
#define BS1 10000019ULL
#define BS2 10000079ULL
#define BS3 10000103ULL
#define PUL pair<ULL,ULL>

///         0123456789
#define MX  400007
#define MOD 1000000007
#define INF 2000000000
#define EPS 1e-9
/// ==========================================////

vector<int> A[102];

int a[55][55];

int vis[102],tot,n;

bool IsValid(int ko,int p) {
    if(ko<=n) {
        for(int i=1;i<=n;i++) {
            int vl=A[p][i-1];
            if( a[ko][i]==0 ) continue;
            if(a[ko][i]!=vl) return 0;
        }
        return 1;
    }
    else {
        ko=ko-n;
        for(int i=1;i<=n;i++) {
            int vl=A[p][i-1];
            if( a[i][ko]==0 ) continue;
            if(a[i][ko]!=vl) return 0;
        }
        return 1;
    }
}
int ms;
vector<int> ans;
void Wow(int ko) {
    if(ko<=n) {
        for(int i=1;i<=n;i++) {
            ans.PB( a[ko][i] );
        }
    }
    else {
        ko=ko-n;
        for(int i=1;i<=n;i++) {
            ans.PB( a[i][ko] );
        }
    }
}

vector<int> Valid(int ko,int p) {
    vector<int> nw;
    if(ko<=n) {
        for(int i=1;i<=n;i++) {
            int vl=A[p][i-1];
            nw.PB(a[ko][i]);
            a[ko][i]=vl;
        }
    }
    else {
        ko=ko-n;
        for(int i=1;i<=n;i++) {
            int vl=A[p][i-1];
            nw.PB(a[i][ko]);
            a[i][ko]=vl;
        }
    }
    return nw;
}

void Remake(int ko,int p,vector<int> v) {
    if(ko<=n) {
        for(int i=1;i<=n;i++) {

            a[ko][i]=v[i-1];
        }
    }
    else {
        ko=ko-n;
        for(int i=1;i<=n;i++) {

            a[i][ko]=v[i-1];
        }
    }
}


int Solve(int p) {

    if(p==-1) {
        Wow(ms);
        return 1;
    }
    int np;
    if(p<=n) {
        np=p+n;
    }
    else {
        np=(p-n+1);
        if(np==(n+1)) np=-1;
    }
    if(p==ms) {
        return Solve(np);
    }
    int f=0;
    for(int i=1;i<=tot;i++) {
        if(!vis[i]) {
            if(IsValid(p,i)) {
                vector<int> nw;

                nw=Valid(p,i);
                vis[i]=1;

                int tp=Solve(np);
                if(tp) {
                    f=1;
                    break;
                }

                vis[i]=0;
                Remake(p,i,nw);
            }
        }
    }
    return f;
}

int main()
{
    freopen("A.in","r",stdin),freopen("A1.out","w",stdout);

    int t;
    S1(t);

    for(int cs=1;cs<=t;cs++) {
        F(i,0,102) A[i].clear();
        ans.clear();

        S1(n);
        tot=n*2-1;
        int mn=100000;
        F(i,1,2*n) {
            F(j,0,n)
            {
                int x;
                S1(x);
                if(j==0) {
                    mn=min(mn,x);
                }
                A[i].PB(x);
            }
        }
        vector<int> IDs;
        for(int i=1;i<=tot;i++) {
            if(A[i][0]==mn) {
                IDs.PB(i);
            }
        }

        printf("Case #%d: ",cs);
        for(int mis=2;mis<=n*2;mis++) {
            MEM(a,0);

            for(int i=1;i<=n;i++) {
                a[1][i]=A[ IDs[0] ][i-1];
            }
            MEM(vis,0);
            vis[ IDs[0] ]=1;
            ms=mis;

            int tp=Solve(n+1);

            if(tp) {
                for(int i=0;i<ans.sz;i++) {
                    if(i) printf(" ");
                    cout<<ans[i];
                }
                NL;
                break;
            }
        }
    }

    return 0;
}
///============= Thank You ===================///
