///============================================================================///
///                                                                            ///
///                            IT'S ME                                         ///
///                         BISHAL GAUTAM                                      ///
///                  CSE,JAHANGIRNAGAR UNIVERSITY,DHAKA                        ///
///               "Follow Excellence..Success will chase U"                    ///
///                                                                            ///
///============================================================================///
#include<bits/stdc++.h>
#define PI acos(-1.0)
#define X first
#define Y second
#define mpp make_pair
#define nl printf("\n")
#define SZ(x) (int)(x.size())
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>

///==Scanning====///
#define S(a) scanf("%d",&a)
#define P(a) printf("%d",a)
#define SL(a) scanf("%lld",&a)
#define S2(a,b) scanf("%d%d",&a,&b)
#define S3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define SL2(a,b) scanf("%lld%lld",&a,&b)
#define SL3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)

///==Arr,Vec Functions==///
#define all(v) v.begin(),v.end()
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define CPY(a,b) memcpy(a,b,sizeof(a))
#define MAX(a) (*max_element(all(a)))
#define MIN(a) (*min_element(all(a)))
#define fv(i,v)  for(int i=0;i<(int)v.size();i++)
#define fr(i,a,n) for(int i=a;i<=n;i++)
#define rf(i,n,a) for(int i=n;i>=a;i--)

///===Some Useful====///
#define OnBit(a) __builtin_popcountll((ll)a)
#define LB(v,k) lower_bound(v.begin(),v.end(),k)
#define _cin ios_base::sync_with_stdio(0),cin.tie(0)
#define dbg(x) cerr<<__LINE__<< ":: "<<#x<<"= "<<x<<endl
#define UNIK(v) sort(all(v)),v.resize( unique(all(v)) -v.begin() );
#define fi(n) for(__typeof(n.begin()) it=n.begin();it!=n.end();it++)
#define IO freopen("A.in","r",stdin),freopen("Out.out","w",stdout)
using namespace std;

///===TypeDefs=====///
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<pii> vii;

///===Number Theory===///
//template< class T > inline T SQR(T a) { return ((a)*(a)); }
//template< class T > inline T gcd(T a,T b) {a=abs(a);b=abs(b); if(!b) return a; return gcd(b,a%b);}
//template< class T > inline T lcm(T a,T b) {a=abs(a);b=abs(b); return (a/_gcd(a,b))*b;}
//template<typename T> T POW(T b,T p) {T r=1; while(p){if(p&1)r=(r*b);b=(b*b);p>>=1;}return r;}
//template<typename T> T BigMod(T b,T p,T m) {T r=1; while(p){if(p&1)r=(r*b)%m;b=(b*b)%m;p>>=1;}return r;}
//template<typename T> T ModInverse(T n,T m) { return BigMod(n,m-2,m); }
//
/////==GeoMetry=========///
//double DEG(double x) { return (180.0*x)/(PI);}
//double RAD(double x) { return (x*(double)PI)/(180.0);}
//template<typename T> double DIS(T a,T b){ return sqrt((double)( SQR(a.X-b.X)+ SQR(a.Y-b.Y))); }
//template<typename T> T ANGLE(T a,T b){ return atan( double(a.Y-b.Y) / double(a.X-b.X));}
//template<typename T> int isLeft(T a,T b,T c) { return (c.X-a.X)*(b.Y-a.Y)-(b.X-a.X)*(c.Y-a.Y); }
//
/////===IO-Related===///
//template< class T > void prnt(T v) { fv(i,v) {if(!i)cout<<v[i];else cout<<" "<<v[i];} cout<<endl; }
//template< class T > void BIN(T n) { if(!n){nl;return;}BIN(n/2);cout<<(n%2); }
//template<typename T> T in(){ char ch; T n = 0; bool ng = false; while (1) { ch = getchar(); if (ch == '-') { ng = true; ch = getchar(); break;} if (ch>='0' && ch<='9') break; }    while (1) { n = n*10 + (ch - '0'); ch = getchar(); if (ch<'0' || ch>'9')   break;    }  return (ng?-n:n);  }

///====Some-Stuff===///
// atoi( str.c_str() ); // char string to int
/// sprintf(str,"%d",num);// num to char string
///int month[]={-1,31,28,31,30,31,30,31,31,30,31,30,31}; //Not Leap Year
///int dx[]= {1,0,-1,0};int dy[]= {0,1,0,-1}; //4 Direction
///int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 Direction
///int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction

/**************************************************************************************
 * ///////////////////////////////////////////////////////////////////////////////////*
 *************************************************************************************/

///==========CONSTANTS==============///
///  Digit     0123456789*#@%&^$"-  ///
#define MX     10000005
#define inf    2000000000
#define MD     1000000007LL
#define eps    1e-9
///================================///

//int vis[MX+2];
//void Seive( ) {
//    vis[1]=vis[0]=1;
//    for(int i=2; i<=MX; i++) {
//        for(int j=i+i; j<=MX; j+=i)vis[j]=i;
//    }
//}

ll multimod(ll a,ll b,ll m) {
    ll ans=0ll;
    a%=m,b%=m;
    while(b) {
        if(b&1ll) ans=m-ans>a?ans+a:ans+a-m;
        b>>=1ll;
        a=(m-a)>a?a+a:a+a-m;
    }
    return ans;
}

ll bigmod(ll b,ll p,ll m) {
    ll ret=1ll;
    while(p) {
        if(p&1ll)
            ret=multimod(ret,b,m);
        b=multimod(b,b,m);
        p>>=1ll;
    }
    return ret;
}

bool isProbablePrime(ll n,int k) {
    if(n < 2) {
        return false;
    }
    if(n != 2 && n % 2 == 0) {
        return false;
    }
    ll s = n - 1;
    while(s % 2 == 0) {
        s >>= 1;
    }
    for (int i = 0; i < k; i++) {
        ll a=(rand()%(n-1))+1;
        ll temp = s;
        ll mod = bigmod(a,temp,n) % n;
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
int ar[36];
int main() {
    int n,i,j,tc,cs=1,J;
    freopen("C-small-attempt2.in","r",stdin);
    freopen("AAAFinalA.txt","w",stdout);
    S(tc);
    //tc=1;
    //Seive();
    while(tc--) {
        S2(n,J);
        n-=2;
        vector<string>v;
        int lim=(1<<n)-1,cnt=0;
        for(i=0; i<=lim; i++) {
            string s="1";
            for(j=0; j<n; j++) {
                if( i&(1<<j) )s+="1";
                else s+="0";
            }
            s+="1";
            int f=1;
            for(ll j=2; j<=10; j++) {
                ll x=1LL,sm=0LL;
                for(int k=n+1; k>=0; k--) {
                    if( s[k]=='1' )sm+=x;
                    x*=j;
                }
                if( isProbablePrime(sm,10) ) {
                    f=0;
                    break;
                }
            }
            if( f==1 ) {
                v.pb(s);
                cnt++;
                if( cnt==J )break;
            }
        }
        int sz=SZ(v);
        printf("Case #%d:\n",cs++);
        for(i=0; i<J; i++) {
            string s=v[i];
            printf("%s",s.c_str());
            for(ll j=2; j<=10; j++) {
                ll x=1LL,sm=0LL;
                for(int k=n+1; k>=0; k--) {
                    if( s[k]=='1' )sm+=x;
                    x*=j;
                }
                ll sq=sqrt(sm)+1;
                for(ll k=2;k<=sq;k++){
                    if( sm%k==0 ){
                        printf(" %lld",k);
                        break;
                    }
                }
            }
            printf("\n");
        }

    }
    return 0;
}
