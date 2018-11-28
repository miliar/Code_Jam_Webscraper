// ==========================================================================
//
//                Starting by the name of Almighty Allah
//
// ==========================================================================

#include<bits/stdc++.h>

#include <algorithm>
#include <cstdio>
#include <sstream>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <iterator>
#include <deque>
#include <climits>
#include <complex>
#include <bitset>

using namespace std;

#define LL                          long long
#define ULL                         unsigned long long

// I/O
#define I(X)                        scanf("%d",     &(X))
#define II(X, Y)                    scanf("%d%d",   &(X), &(Y))
#define III(X, Y, Z)                scanf("%d%d%d", &(X), &(Y), &(Z))

#define IL(X)                       scanf("%lld", &X)
#define IIL(X,Y )                   scanf("%lld%lld", &X,&Y)
#define IIIL(X,Y,Z)                 scanf("%lld%lld%lld", &X,&Y,&Z)

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

#define SS(s)                       scanf("%s",s)

#define PI(x)                       printf("%d\n",      x)
#define PII(x,y)                    printf("%d %d\n",   x,y)
#define PIII(x,y,z)                 printf("%d %d %d\n",x,y,z)

#define PIL(x)                      printf("%lld\n",          x)
#define PIIL(x,y)                   printf("%lld %lld\n",     x,y)
#define PIIIL(x,y,z)                printf("%lld %lld %lld\n",x,y,z)

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
#define Max(a,b)                    (a>b?a:b)
#define Min(a,b)                    (a<b?a:b)
#define _Max(a,b,c)                 Max(a,Max(b,c))
#define _Min(a,b,c)                 Min(a,Min(b,c))
#define MAX(a)                      (*max_element(all(a)))
#define MIN(a)                      (*min_element(all(a)))

#define FastMax(x,y)                ((((y-x)>>(32-1))&(x^y))^y)
#define FastMin(x,y)                ((((y-x)>>(32-1))&(x^y))^x)

#define SQR(n)          ((n)*(n))

#define all(a)          a.begin(),a.end()
#define PB              push_back
#define NL              puts("");
#define pline           cout << "_________________________" << endl;
// pair
#define XX              first
#define YY              second
// binary search
#define LB(a,x)         (lower_bound(all(a),x)-a.begin())
#define UB(a,x)         (upper_bound(all(a),x)-a.begin())

//#define SI(X)           X=in<int>()
//#define SII(X,Y)        X=in<int>(),Y=in<int>()
//#define SIII(X,Y,Z)     X=in<int>(),Y=in<int>(),Z=in<int>()
//
//#define SL(X)           X=in<LL>()
//#define SLL(X,Y)        X=in<LL>(),Y=in<LL>()
//#define SLLL(X,Y,Z)     X=in<LL>(),Y=in<LL>(),Z=in<LL>()

//#define SEG             int mid=(s+e)>>1,l=(idx<<1),r=(l|1);
#define in(l,x,r)       ( l<=x && x<=r )

// Bit-op
#define countbit(x)     __builtin_popcount(x)
template< class T, class X > inline bool checkbit(T a, X pos) { T t=1;return ((a&(t<<pos))>0);  }
template< class T, class X > inline T      setbit(T a, X pos) { T t=1;return (a|(t<<pos));      }
template< class T, class X > inline T    resetbit(T a, X pos) { T t=1;return (a&(~(t<<pos)));   }
template< class T, class X > inline T   togglebit(T a, X pos) { T t=1;return (a^(t<<pos));      }
// mathematics
template<typename T> T POW(T base,T power)              { T ret=1; while(power)  { if(power & 1) ret=(ret*base); base=(base*base);  power>>=1; }return ret; }
template<typename T> T PPOW(T B,T P)                    { if(P==0) return 1; if(P&1) return B*POW(B,P-1);  else return SQR(POW(B,P/2));}
template<typename T> T Bigmod(T base,T power,T mod)     { T ret=1; while(power)  { if(power & 1) ret=(ret*base)%mod; base=(base*base)%mod;  power>>=1; }return ret; }
template<typename T> T ModInverse(T number,T mod)       { return Bigmod(number,mod-2,mod); }
template<typename T> T GCD(T a,T b)                     { if(a<0)return GCD(-a,b);if(b<0)return GCD(a,-b);return (b==0)?a:GCD(b,a%b);}
template<typename T> T LCM(T a,T b)                     { if(a<0)return LCM(-a,b);if(b<0)return LCM(a,-b);return a*(b/GCD(a,b));}
template<typename T> T EUCLIDE(T a,T b,T &x,T &y)       { if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}   if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}   if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
template<typename T> T ABS(T a)                         { if(a<0)return -a;else return a;}
// geometry
template<typename T> double DIS(T x1,T y1,T x2, T y2)   { return sqrt( (double)( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) ) );}
template<typename T> T ANGLE(T x1,T y1,T x2, T y2)      { return atan( double(y1-y2) / double(x1-x2));}
template<typename T> LL isLeft(T a,T b,T c)             { return (c.x-a.x)*(b.y-a.y)-(b.x-a.x)*(c.y-a.y); }
// Degree and Radian
//double DEG(double x) { return (180.0*x)/(M_PI*1.0);}
//double RAD(double x) { return (x*(M_PI*1.0))/(180.0);}

// debug
void P_ARR(int *ar,int a,int b) {  if(a>b) swap(a,b); if(a<=b) cout << ar[a]; for(int i=a+1;i<=b;i++) cout << " "<<ar[i];  cout << endl; }
template<typename T> T In(){ char ch; T n = 0; bool ng = false; while (1) { ch = getchar(); if (ch == '-') { ng = true; ch = getchar(); break;} if (ch>='0' && ch<='9') break; }    while (1) { n = n*10 + (ch - '0'); ch = getchar(); if (ch<'0' || ch>'9')   break;    }  return (ng?-n:n);  }

//int month[]={31,28,31,30,31,30,31,31,30,31,30,31};                                    /// month
//int dir[5][2] = { {0,0},{1,0},{0,1},{-1,0},{0,-1} };                                  /// 4 Direction
//int dir[9][2] = { {0,0},{1,0},{0,1},{-1,0},{0,-1},{-1,1},{-1,-1},{1,-1},{1,1}};       /// 8 direction
//int dir[9][2] = { {0,0},{2,1},{1,2},{-1,2},{-2,1},{-2,-1},{-1,-2},{1,-2},{2,-1} };    /// Knight Direction
//int dir[8][2] = { {0,0},{2,0},{1,1},{-1,1} ,{-2,0} , {-1,-1} ,{1,-1} };               /// Hexagonal Direction
// dir[][0] = x value, dir[][1] = y value

/// ======================================================================================================
#define  debug  0
#define  AA     if(debug)
#define eps     (1e-9)
//#define pi      (2.0*acos(0.0)) //#define PI acos(-1.0)
// IO
#define READ            freopen("C:\\Users\\backbencher\\Desktop\\input.txt","r",stdin)
#define WRITE           freopen("C:\\Users\\backbencher\\Desktop\\output.txt","w",stdout)
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




bool check(LL n)
{
    CLR( ar );

    rep(i,0,15){

        if( checkbit(n,i) ){

            rep(base,2,10){

                ar[base] += POW((LL)base,(LL)i);

            }
        }
    }

//    cout << "who " << endl;
//
//    rep(base,2,10){
//        cout << ar[base] << " ";
//    }
//    cout << endl;



    bool flag  = 0;

    CLR( res );

    rep(base,2,10){

        vector<long long>vv;

        cc = 0;

//        cout << base << "->" << ar[base] << endl;

        llfactorize( ar[base] , vv );

//        pline;


        if( vv.size()==1 ) return false;

        res[base] = vv[0];

//        for(auto i : vv )
//        {
//            if( i==ar[base] ) continue;
//
//            LL n = ar[base];
//
//            int cnt =0;
//            while( n%i==0 ) n/=i , cnt++;
//
//            if( cnt>0 && cnt%2==0 ){
//                res[base] = i;
//                break;
//            }
//        }
//
//        if( res[base]==0 ) return false;

    }

    return true;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

//    LL val = ( 1<< (16) )-1;
//    bitset<16>x = val;
//    cout << x << endl;
//    cout << val << endl;
//    cout << POW(9LL,15LL) << endl;

      sieve();
//
//      check(32769LL);
//
//      cout << "ses"  << endl;

//    check(9LL);
//    vector<long long>vv;
//    llfactorize(15LL,vv);
//    for( auto i : vv )  cout << i << " -> " << endl;


    DI(tc);

    rep(cas,1,tc)
    {
        DII( j , n );


        printf("Case #%d:\n",cas);

        int cnt =0 ;

        rep(i,0,(1<<j)-1)
        {
//            continue;

            if( !checkbit(i,j-1) ) continue;

            if( i%2==0) continue;

//            cout << i << " ->  "  << endl;

            if( check( (LL)i ) ){

                cnt++;

                vector<int>a;

                int b = i;

                while( b ) a.push_back(b%2) , b /= 2;

                revv(ii,a) cout << a[ii];

                rep(base,2,10){
                    cout << " " << res[base];
                }
                cout<<endl;
            }

            if(cnt==n) break;

//            i++;
        }
    }



    return 0;
}

