///USER:Ahmed Maruf
///TASK:
///ALGO:Don't know yet :p
#include<bits/stdc++.h>
#define INF_MAX     2147483647
#define INF_MIN     -2147483648
#define INF         (1 << 30)
#define EPS         1e-9
#define N           2 + 1000000
#define MOD         10000000007
#define sz(x)       (int)(x).size()
#define all(x)      (x).begin(), (x).end()
#define Pi acos(-1.0)
#define MP(x, y) make_pair(x, y)
#define REV(s, e) reverse(s, e)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define i64 long long
#define ll long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >
#define ALL(c) (c).begin(),(c).end()
#define REP(i, n) for(int i=0; i<(int)n; ++i)
#define repv(i,n) for(int i=(int)n-1;i>=0;--i)
#define rep(i,a,b)  for(int i=(a); i<(b); i++)
#define repe(i,a,b) for(int i=(a); i<=b; i++)
#define repC(i,x)   for(size_t i=0; i<x.size(); i++)
#define FOR(i, c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
# define  minof(X)		min_element(all(X))-X.begin()
# define  maxof(X)		max_element(all(X))-X.begin()
# define  square(X)		(X)*(X)
# define  cube(X)		(X)*(X)*(X)
#define RD(n) scanf("%d",&n)
#define RD2(x,y) scanf("%d%d",&x,&y)
#define RD3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define RD4(x,y,z,w) scanf("%d%d%d%d",&x,&y,&z,&w)
#define PN(n) printf("%d",n)
#define PN2(x,y) printf("%d%d",x,y)
#define PN3(x,y,z) printf("%d%d%d",x,y,z)
#define PN4(x,y,z,w) printf("%d%d%d%d",x,y,z,w)
#define UNIQ(a)      sort(all(a)); (a).erase(unique(all(a)),(a).end())
#define upto(n) fixed<<setprecision(n)
using namespace std;

//template< class T > T sq(T x) { return x * x; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T a, T b, T c) { return a<=b && b<=c; }
template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }

template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r; }

template<class T> string itoa(T a)
{
    if(!a) return "0";
    string ret;
    for(T i=a; i>0; i=i/10) ret.PB((i%10)+48);
    reverse(ALL(ret));
    return ret;
}
#define on(n,pos) (n | (1LL<<(pos)))
#define off(n,pos) n & ~(1LL<<pos)
#define isOn(n,pos) (bool)(n & (1LL<<(pos)))
string toBin(int n)
{
    string s;
    repv(i,10)s+=(isOn(n,i)+'0');
    return s;
}
//int BigMod(ll B,ll P,ll M){     ll R=1; while(P>0)      {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;} /// (B^P)%M
ll powermod(ll n,ll p)
{
    if(p==0)
        return 1;
    ll a=powermod(n,p/2)%MOD;
    if(p%2==1)
        return (a*a*n)%MOD;
    return (a*a)%MOD;

}
inline ll bigmod ( ll a, ll p, ll m ) {
    ll res = 1 % m, x = a % m;
    while ( p ) {
        if ( p & 1 ) res = ( res * x ) % m;
        x = ( x * x ) % m; p >>= 1;
    }
    return res;
}
inline ll power ( ll a, ll p ) {
    ll res = 1, x = a;
    while ( p ) {
        if ( p & 1 ) res = ( res * x );
        x = ( x * x ); p >>= 1;
    }
    return res;
}
int num_digits(int number)
{
    int digits = 0;
    // remove following line if '-' counts as a digit
    if (number < 0)
        digits = 1;
    while (number)
    {
        number /= 10;
        digits++;
    }
    return digits;
}
long long factorial_exponent(long long n, long long p)
{
    long long ex = 0;
    do
    {
        n /= p;
        ex += n;
    }
    while(n > 0);
    return ex;
}

int dr[]= {0,-1, 0,1};
int dc[]= {1, 0,-1,0};
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction
//int N = 5000, status[5001];
//int mon[] = {31,28,31,30,31,30,31,31,30,31,30,31};
int main()
{
    #ifndef ONLINE JUDGE
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    #endif // ONLINE
    ios_base :: sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll int test,number,cnt;
    bool arr[50];
    cin>>test;
    repe(i,1,test)
    {
        cin>>number;
        if(!number)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        cnt=0;
        memset(arr,false,sizeof arr);
        repe(j,1,INF)
        {
            int hold = j*number;
            int ans = hold;
            while(hold)
            {
               // cout<<hold%10<<endl;
                if(arr[hold%10]==false)
                {
                    arr[hold%10] = true;
                    cnt++;
                }
                hold/=10;
            }
            if(cnt==10)
            {
                cout<<"Case #"<<i<<": "<<ans<<endl;
                break;
            }
        }
    }
    return 0;
}

