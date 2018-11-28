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
#define MX  100000007
#define MOD 1000000007
#define INF 100000000
/// ==========================================////

LL multimod(LL a,LL b,LL m) {
    LL ans=0ll;
    a%=m,b%=m;
    while(b) {
        if(b&1ll) ans=m-ans>a?ans+a:ans+a-m;
        b>>=1ll;
        a=(m-a)>a?a+a:a+a-m;
    }
    return ans;
}

LL bigmod(LL b,LL p,LL m) {
    LL ret=1ll;
    while(p) {
        if(p&1ll)
            ret=multimod(ret,b,m);
        b=multimod(b,b,m);
        p>>=1ll;
    }
    return ret;
}

bool isProbablePrime(LL n,int k) {
    if(n < 2) {
        return false;
    }
    if(n != 2 && n % 2 == 0) {
        return false;
    }
    LL s = n - 1;
    while(s % 2 == 0) {
        s >>= 1;
    }
    for (int i = 0; i < k; i++) {
        LL a=(rand()%(n-1))+1;
        LL temp = s;
        LL mod = bigmod(a,temp,n) % n;
        while(temp != n - 1ll && mod != 1ll && mod != n - 1ll) {
            mod = multimod(mod,mod,n);
            temp = temp * 2ll;
        }
        if(mod != n - 1ll && temp % 2ll == 0) {
            return false;
        }
    }
    return true;
}

int pm[MX];
bool prime[MX+9];
int cnt;
void seive()
{
    prime[1]=true;
    int s=sqrt(MX);
    for(int i=2; i<=s; i++)
    {
        if(!prime[i])
        {
            for(int j=2*i; j<=100000000; j+=i)
            {
                prime[j]=true;

            }
        }
    }
    cnt=0;
    F(i,2,100000001) if(!prime[i]) pm[cnt++]=i;
}

int a[MX];

LL Base(LL n,int k) {
    int ln=0;
    LL m=n;
    while(n) {
        a[ln++]=n%10;
        n/=10;
    }
    reverse(a,a+ln);

    LL ans=0;
    for(int i=0;i<ln;i++) {
        ans=(ans*k+a[i]);
    }
    return ans;
}

vector<LL> v;

void Dekhi(LL n,int ln) {
    if(ln==0) {
        n=n*10+1;
        v.PB(n);
        return ;
    }
    Dekhi(n*10,ln-1);
    Dekhi(n*10+1,ln-1);
}

LL b[10009];

int main()
{
    freopen("A.in","r",stdin),freopen("A1.out","w",stdout);
    seive();
    int t;
    S1(t);
    int len,k;
    cin>>len>>k;
    printf("Case #1:\n");

    Dekhi(1,len-2);

    for(int i=0;i<v.sz;i++) {
        int f=0;
        int now=0;
        for(int bse=2;bse<=10;bse++) {
            LL tp=Base(v[i],bse);
            b[now++]=tp;
            if(isProbablePrime(tp,10)) {
                f=1;
                break;
            }
        }
        if(!f) {
            printf("%lld",v[i]);
            for(int j=0;j<9;j++) {
                LL v=b[j];
                for(int l=0;l<cnt;l++) {
                    if(v%pm[l]==0) {
                        printf("% d",pm[l]);
                        break;
                    }
                }
            }
            NL;
            k--;
        }
        if(!k) break;
    }


    return 0;
}
