// Bis-mil-lah

#include<bits/stdc++.h>

using namespace std;

#define LL                          long long
#define ULL                         unsigned long long

// I/O
#define I(X)                        scanf("%d",     &(X))
#define II(X, Y)                    scanf("%d%d",   &(X), &(Y))
#define III(X, Y, Z)                scanf("%d%d%d", &(X), &(Y), &(Z))

#define ID(x)                       scanf("%lf",&x)
#define IID(x,y)                    scanf("%lf%lf",&x,&y)
#define IIID(x,y,z)                 scanf("%lf%lf%lf",&x,&y,&z)

#define DI(X)         int X;        I(X);
#define DII(X, Y)     int X, Y;     II(X,Y)
#define DIII(X, Y, Z) int X, Y, Z;  III(X,Y,Z);

#define DIL(X)        LL X;         IL(X)
#define DIIL(X,Y)     LL X,Y;       IIL(X,Y)
#define DIIIL(X,Y,Z)  LL X,Y,Z;     IIIL(X,Y,Z)

#define DDI(x)        double x;     ID(x);
#define DDII(x,y)     double x,y;   IID(x,y);
#define DDDII(x,y,z)  double x,y,z; IIID(x,y,z);


// LOOP
#define rep(i,a,b)                  for(int i=a;i<=b;i++)
#define rev(i,a,b)                  for(int i=a;i>=b;i--)
#define repv(i,a)                   for(int i=0;i<(int)a.size();i++)
#define revv(i,a)                   for(int i=((int)a.size())-1;i>=0;i--)

#define FS(x)                       for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define PR(x)                       for(typeof (x.begin()) it = x.begin(); it != x.end (); it++) {  cout << *it << " "; } cout << endl;

// array initialization
#define MEM(a,val)                  memset(a,val,sizeof(a));
//#define SET(a)                      memset(a,-1,sizeof a)
#define CLR(a)                      memset(a,0,sizeof a)

// min-max


#define SQR(n)          ((n)*(n))

#define all(a)          a.begin(),a.end()
#define PB              push_back
#define NL              puts("");
#define pline           cout << "_________________________" << endl;
// pair

// Bit-op
#define countbit(x)     __builtin_popcount(x)
template< class T, class X > inline bool checkbit(T a, X pos) { T t=1;return ((a&(t<<pos))>0);  }
template< class T, class X > inline T      setbit(T a, X pos) { T t=1;return (a|(t<<pos));      }
template< class T, class X > inline T    resetbit(T a, X pos) { T t=1;return (a&(~(t<<pos)));   }

/// ======================================================================================================
#define  debug  0
#define  AA     if(debug)
#define eps     (1e-9)

#define _cin            ios_base::sync_with_stdio(0); cin.tie(0);


//              0123456789
#define  MX     500007
#define  MOD    1000000007
#define  inf    100000000


#define MAXL (50000>>5)+1
#define GET(x) (mark[x>>5]>>(x&31)&1)
#define SET(x) (mark[x>>5] |= 1<<(x&31))

int mark[1000013+7];
int P[1000013+7], Pt = 0;

void sieve() {
    register int i, j, k;
    SET(1);
    //int n = 46340;
    int n = 1000013;
    for (i = 2; i <= n; i++) {
        if (!GET(i)) {
            for (k = n/i, j = i*k; k >= i; k--, j -= i)
                SET(j);
            P[Pt++] = i;
        }
    }
}
long long mul(unsigned long long a, unsigned long long b, unsigned long long mod) {
    long long ret = 0;
    for (a %= mod, b %= mod; b != 0; b >>= 1, a <<= 1, a = a >= mod ? a - mod : a) {
        if (b&1) {
            ret += a;
            if (ret >= mod)	ret -= mod;
        }
    }
    return ret;
}
void exgcd(long long x, long long y, long long &g, long long &a, long long &b) {
    if (y == 0)
        g = x, a = 1, b = 0;
    else
        exgcd(y, x%y, g, b, a), b -= (x/y) * a;
}
long long llgcd(long long x, long long y) {
    if (x < 0)    x = -x;
    if (y < 0)    y = -y;
    if (!x || !y)    return x + y;
    long long t;
    while (x%y)
        t = x, x = y, y = t%y;
    return y;
}
long long inverse(long long x, long long p) {
    long long g, b, r;
    exgcd(x, p, g, r, b);
    if (g < 0)	r = -r;
    return (r%p + p)%p;
}

long long mpow(long long x, long long y, long long mod) { // mod < 2^32
    long long ret = 1;
    while (y) {
        if (y&1)
            ret = (ret * x)%mod;
        y >>= 1, x = (x * x)%mod;
    }
    return ret % mod;
}

long long mpow2(long long x, long long y, long long mod) {
    long long ret = 1;
    while (y) {
        if (y&1)
            ret = mul(ret, x, mod);
        y >>= 1, x = mul(x, x, mod);
    }
    return ret % mod;
}

int isPrime(long long p) { // implements by miller-babin
    if (p < 2 || !(p&1))	return 0;
    if (p == 2)				return 1;
    long long q = p-1, a, t;
    int k = 0, b = 0;
    while (!(q&1))	q >>= 1, k++;
    for (int it = 0; it < 2; it++) {
        a = rand()%(p-4) + 2;
        t = mpow2(a, q, p);
        b = (t == 1) || (t == p-1);
        for (int i = 1; i < k && !b; i++) {
            t = mul(t, t, p);
            if (t == p-1)
                b = 1;
        }
        if (b == 0)
            return 0;
    }
    return 1;
}
long long pollard_rho(long long n, long long c) {
    long long x = 2, y = 2, i = 1, k = 2, d;
    while (true) {
        x = (mul(x, x, n) + c);
        if (x >= n)	x -= n;
        d = llgcd(x - y, n);
        if (d > 1) return d;
        if (++i == k) y = x, k <<= 1;
    }
    return n;
}

void factorize(int n, vector<long long> &f) {
    for (int i = 0; i < Pt && P[i]*P[i] <= n; i++) {
    	if (n%P[i] == 0) {
    		while (n%P[i] == 0)
    			f.push_back(P[i]), n /= P[i];
    	}
    }
    if (n != 1)	f.push_back(n);
}

int cc;

void llfactorize(long long n, vector<long long> &f) {

    if (n == 1)
        return;
    if (n < 1e+9) {
        factorize(n, f);
        return ;
    }
    if ( isPrime(n) ) {
        f.push_back(n);
        cc++;
        return ;
    }

    long long d = n;
    for (int i = 2; d == n; i++)
    {
        d = pollard_rho(n, i);
        if( cc>1 ) return;
    }
    llfactorize(d, f);
    llfactorize(n/d, f);
}


LL  ar[13];
LL res[13];
template<typename T> T POW(T base,T power)              { T ret=1; while(power)  { if(power & 1) ret=(ret*base); base=(base*base);  power>>=1; }return ret; }


bool check(LL n)
{
    CLR( ar );

    rep(i,0,15) {
        if( checkbit(n,i) ) {
            rep(base,2,10) {
                ar[base] += POW((LL)base,(LL)i);
            }
        }
    }

    bool flag  = 0;
    CLR( res );

    rep(base,2,10){
        vector<long long>vv;
        cc = 0;
        llfactorize( ar[base] , vv );
        if( vv.size()==1 ) return false;
        res[base] = vv[0];
    }

    return true;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);


    sieve();

    DI(tc);

    rep(cas,1,tc)
    {
        DII( j , n );

        printf("Case #%d:\n",cas);

        int cnt =0 ;

        rep(i,0,(1<<j)-1){

            if( !checkbit(i,j-1) ) continue;
            if( i%2==0) continue;

            if( check( (LL)i ) ) {
                cnt++;
                vector<int>a;
                int b = i;
                while( b ) a.push_back(b%2) , b /= 2;
                revv(ii,a) cout << a[ii];
                rep(base,2,10) {
                    cout << " " << res[base];
                }
                cout<<endl;
            }
            if(cnt==n) break;
        }
    }

    return 0;
}

