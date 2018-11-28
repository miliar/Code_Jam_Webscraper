/// Containers Start
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define NDEBUG
#include <assert.h>

/// C Header Files
#include <cstdio>
#include <cctype>
#include <cmath>
#include <math.h>
#include <ctime>
#include <cstring>
/// Containers End



using namespace std;
 


#ifdef _WIN32
#  define LLDFORMAT "%I64d"
#else
#  define LLDFORMAT "%lld"
#endif


#ifndef ONLINE_JUDGE
#define DEBUG
#endif


#define INPUTFILEp  stdin
#define OUTPUTFILEp stdout


/// TypeDef Start

typedef  unsigned long int       uli;
typedef  long int                li;
typedef  unsigned long long int  ulli;
typedef  long long int           lli;

typedef  map<int,int>            mii;
typedef  map<string,int>         msi;
typedef  map<int,string>         mis;
typedef  map<lli, lli>           mlli;
typedef  map<char,int>           mci;
typedef  map<int,char>           mic;

typedef  pair<int,int>           pii;
typedef  pair<string, int>       psi;
typedef  pair<int, string>       pis;
typedef  pair<string, string>    pss;

typedef  vector<int>             vi;
typedef  vector<string>          vs;
typedef  vector<char>            vc;
typedef  vector<bool>            vb;
typedef  vector< pii >           vii;
typedef  vector< pis >           vis;

typedef  set<int>                si;
typedef  set<string>             ss;
typedef  set<char>               sc;

typedef  deque<int>              di;
typedef  deque<string>           ds;
typedef  deque<char>             dc;

typedef  stack<int>              sti;
typedef  stack<string>           sts;
typedef  stack<char>             stc;

/// TypeDef End




/// Math Start
#define PI                    3.1415926535897932384626433832795
#define EPS                   (1e-9)

#define Sqr(n)                ( (n) * (n) )
#define Cub(n)                ( (n) * (n) * (n) )
/// Math End
 

/// Constants
const double pi=acos(-1.0);
const double eps = 1e-9;

const ulli pow10n[30]={1, 
10, 
100, 
1000, 
10000, 
100000, 
1000000, 
10000000, 
100000000, 
1000000000, 
10000000000, 
100000000000, 
1000000000000, 
10000000000000, 
100000000000000, 
1000000000000000, 
10000000000000000, 
100000000000000000, 
1000000000000000000,
};

#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define limax numeric_limits<li>::max()
#define limin numeric_limits<li>::min()
#define ulmax numeric_limits<uli>::max()
#define ulmin numeric_limits<uli>::min()
#define llimax numeric_limits<lli>::max()
#define llimin numeric_limits<lli>::min()
#define ullimax numeric_limits<ulli>::max()
#define ullimin numeric_limits<ulli>::min()

#define MOD                   1000000007
#define INF                   2147483647


/// Array Start
//#define seta(a)               memset( a, -1,    sizeof a )
#define clra(a)                memset( a,  0,    sizeof (a) )
#define seta(a,val)            memset( a,  val,  sizeof(a) )
/// Array End
 
 
/// Extra Start
#define ff                    first
#define ss                    second
#define mp                    make_pair
#define endl                  '\n'
#define pb                    push_back
#define SS                    stringstream

#define csi(a)                (int((a).size()))                                    //container size 
#define asi(a)                (int(sizeof(a)/sizeof((a)[0])))                        //array size

#define space                 " "
#define all(x)                (x).begin(), (x).end()
#define rall(x)               (x).rbegin(), (x).rend()

#define cign                  cin.ignore


#define Trace(x) #x

#define Bound(A, B, C) is( B <= A && A <= C)
#define is(x) if(!(x)){cerr<<"cerr> Check failed: "#x<<endl;}

#define ininc(a,b,c) (b <= a && a <= c)
#define inexc(a,b,c) (b < a && a < c)
#define outinc(a,b,c) (a <= b || a >= c)
#define outexc(a,b,c) (a < b || a > c)
/// Extra End
 


/// Loops
#define FOR(i, j, k, d)  for(int i=(j) ; i<(k) ; i+=(d))
#define FORI(i, j, k, d)  for(int i=(j) ; i<=(k) ; i+=(d))
#define RFOR(i, j, k, d) for(int i=(j) ; i>(k) ; i-=(d))
#define RFORI(i, j, k, d) for(int i=(j) ; i>=(k) ; i-=(d))

#define REP(i, j)  FOR(i, 0, j, 1)
#define RREP(i, j) RFORI(i, (j-1), 0, 1)

//needs c++11
//define VFOR(it, c) for (auto it = (c).begin(); it != (c).end(); it++)
//define VRFOR(it, c) for (auto it = (c).begin(); it != (c).end(); it++)
#define VFOR(it,c)  for(int it=0;it!=c.size();it++)
#define RVFOR(it,c) for(int it=c.size()-1;it>=0;it--)

#define csort(v) sort(v.begin(),v.end())
#define rcsort(v) sort(v.rbegin(), v.rend())

#define rev(v) reverse(v.begin(),v.end())
 


/// I/O Start
#define sf      scanf
#define pf      printf
 

#define sfl(t)  scanf("%ld",&t)

#define sfc(t)  scanf("%c",&t)
#define sfs(t)  scanf("%s",t)
#define sff(t)  scanf("%f",&t)
#define sflf(t) scanf("%lf",&t)

#define sfi(a)                scanf("%d", &(a))
#define sf2i(a,b)             scanf("%d %d",&(a), &(b))
#define sf3i(a,b,c)           scanf("%d %d %d", &(a), &(b), &(c))
#define sf4i(a,b,c,d)         scanf("%d %d %d %d", &(a), &(b), &(c), &(d))
 
#define sfll(a)               scanf("%I64d", &(a))
#define sf2ll(a,b)            scanf("%I64d %I64d", &(a), &(b))
#define sf3ll(a,b,c)          scanf("%I64d %I64d %I64d", &(a), &(b), &(c))
#define sf4ll(a,b,c, d)       scanf("%I64d %I64d %I64d %I64d", &(a), &(b), &(c), &(d))


#define pf1(a)                printf("%d", (a))
#define pf2(a,b)              printf("%d %d",(a), (b))
#define pf3(a,b,c)            printf("%d %d %d", (a), (b), (c))
#define pf4(a,b,c, d)         printf("%d %d %d %d", (a), (b), (c), (d))
 
#define pf1ll(a)              printf("%I64d", (a))
#define pf2ll(a,b)            printf("%I64d %I64d", (a), (b))
#define pf3ll(a,b,c)          printf("%I64d %I64d %I64d", (a), (b), (c))
#define pf4ll(a,b,c, d)       printf("%I64d %I64d %I64d %I64d", (a), (b), (c), (d))


#define FSTDIN(f)             freopen(f, "r", stdin);
#define FSTDOUT(f)            freopen(f, "w", stdout);

#define _UNSYNCIO             ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
// use only if using cin cout
// printf scanf freopen maynot work


//DEBUG
#define pendl   cout<<endl;
#define DEBUG1(x) cerr << #x << "=" << x << "; ";
#define DEBUG2(a,b) DEBUG1(a) DEBUG1(b)
#define DEBUG3(a,b,c)   DEBUG2(a,b) DEBUG1(c)
#define DEBUG4(a,b,c,d)   DEBUG2(a,b,c) DEBUG1(d)
#define DEBUG5(a,b,c,d,e)   DEBUG2(a,b,c,d) DEBUG1(e)
#define DEBUG6(a,b,c,d,e,f)   DEBUG2(a,b,c,d,e) DEBUG1(f)
#define debug(...) cout<<"cerr> "; GET_MACRO(__VA_ARGS__, DEBUG3, DEBUG2, DEBUG1)(__VA_ARGS__) pendl
#define GET_MACRO(_1,_2,_3,NAME,...) NAME

/// I/O End




 
/// Functions Start

template < class T > T teql( T a, T b ){return ( abs(a-b) < EPS );}                      // a==b


template < class T > T tge( T a, T b ){return ( a > b-EPS );}                            // a>=b
template < class T > T tgt( T a, T b ){return ( a >= b+EPS );}                          // a>b

template < class T > T tle( T a, T b ){return ( a < b-EPS );}                            // a<=b
template < class T > T tlt( T a, T b ){return ( a <= b+EPS );}                          // a<b


//@@@@@@@@@@@@@@@@@@@@@@@//////////////////////////////////////////////////////////// check above comp



template < class T > T tmax( T a, T b ){return ( a > b ? a : b );}
template < class T > T tmin( T a, T b ){return ( a < b ? a : b );}


template < class T > string vtostr( vector<T> &v ){SS x; VFOR(it,v) x<<v[it];  return x.str();} 
template < class T > string strtov( vector<T> &v ){SS x; T n; while(x>>n)v.pb(n);} 


template<typename T> inline int tsgn(const T& x){return (x>+EPS)-(x<-EPS);}
template<typename T> inline int tcmp(const T& a,const T& b){return tsgn(a-b);}


template<typename T> inline bool smax(T& a,const T& b){return a<b?a=b,true:false;}
template<typename T> inline bool smin(T& a,const T& b){return b<a?a=b,true:false;}

template<typename T> inline T sqr(const T& x){return x*x;}
template<typename T> inline T cub(const T& x){return x*x*x;}

template<typename T> inline T mod(const T& x){return x%MOD;}
template<typename T> inline T tgcd(T a,T b){if(b)while((a%=b)&&(b%=a));return a+b;}
template<typename T> inline T tlcm(T a,T b){return a*b/gcd(a,b);}


template<typename T> inline pair<T, T> operator-(const pair<T, T>& x){return mp(-x.first,-x.second);}    // -pair elementwise neg
template<typename T> inline pair<T, T> operator+(const pair<T, T>& a,const pair<T, T>& b){return mp(a.first+b.first,a.second+b.second);}  // pair+pair elementwise
template<typename T> inline pair<T, T> operator-(const pair<T, T>& a,const pair<T, T>& b){return mp(a.first-b.first,a.second-b.second);}  // pair-pair elementwise 
template<typename T> inline pair<T, T> operator*(const pair<T, T>& a,const T& b){return mp(a.first*b,a.second*b);}               // pair*scalar mult
template<typename T> inline pair<T, T> operator/(const pair<T, T>& a,const T& b){return mp(a.first/b,a.second/b);}               // pair/scalar div
template<typename T> inline pair<T, T>& operator-=(pair<T, T>& a,const pair<T, T>& b){return a=a-b;}                    // pair -= pair
template<typename T> inline pair<T, T>& operator+=(pair<T, T>& a,const pair<T, T>& b){return a=a+b;}                    // pair += scalar
template<typename T> inline pair<T, T>& operator*=(pair<T, T>& a,const T& b){return a=a*b;}                             // pair *= scalar
template<typename T> inline pair<T, T>& operator/=(pair<T, T>& a,const T& b){return a=a/b;}                             // pair /= scalar
template<typename T> inline T pcross(const pair<T, T>& a,const pair<T, T>& b){return a.first*b.second-a.second*b.first;}        // cross *
template<typename T> inline T pdot(const pair<T, T>& a,const pair<T, T>& b){return a.first*b.first+a.second*b.second;}          // dot product


// >> and << for pair
template<typename istream,typename Ta,typename Tb> inline istream& operator>>(istream& cin,pair<Ta, Tb>& x){return cin>>x.first>>x.second;}
template<typename ostream,typename Ta,typename Tb> inline ostream& operator<<(ostream& cout,const pair<Ta, Tb>& x){return cout<<x.first<<" "<<x.second;}

// >> and << for vector
template<typename istream,typename T> inline istream& operator>>(istream& cin,vector<T>& x){VFOR(it,x)cin>>x[it];return cin;}
template<typename ostream,typename T> inline ostream& operator<<(ostream& cout,const vector<T>& x){VFOR(it,x)cout<<x[it]<<(it+1==x.size()?"":" ");return cout;}


// Bit functions
inline int twopow(int n) { return 1 << n; }
inline int testbit(int n, int b) { return (n>>b)&1; }
inline void setbit(int & n, int b) { n |= twopow(b); }
inline void unsetbit(int & n, int b) { n &= ~twopow(b); }
inline int lastbit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }        // Check

/// Functions End
 

//Unsync stdio for fast io
struct Initializer{
time_t programstarttime;
Initializer(){
    //_UNSYNCIO
    programstarttime=clock();}
~Initializer(){cerr << "cerr> Program ran in "<< ( clock()-programstarttime ) / CLOCKS_PER_SEC << " s " << endl;}
}initializer;


#define gc() getchar()
#define pc(x) putchar((x))

#define MAXCOLS     100                 //max no. of lines per col
char linebuf[MAXCOLS+1];
int lbi=0;

template <typename T> inline int readint(T &n)
{
    n=0;
    signed char s=1, i=0;
    bool notdigit=true;
    char p=gc();


    while(notdigit)
    {
        while((p<'0'||p>'9')&&p!=EOF&&p!='-')
            p=gc();
        if(p=='-')
            s=-1,p=gc();
        else if(p=='+')
            p=gc();

        if('0' <= p && p <= '9')
            notdigit=false;
    }
    while(p>='0'&&p<='9') {
        i++;
        n = n*10 + (p - '0');
        p=gc();
    }

    //ungetc(p,INPUTFILEp);
    n=n*s;
    return i; //no. of digits excl sign
}



template <typename T> inline void writeint(T n)
{
    int i = 20;
    char buf[21];
    // buf[10] = 0;
    buf[20] = '\n';

    if(n<0)
    {
        pc('-');
        n*=-1;
    }

    do
    {
        buf[--i] = n % 10 + '0';
        n/= 10;
    }while(n);

    do
    {
        pc(buf[i]);
    } while (buf[++i] != '\n');
        
}



template <typename T> inline void readints(T *v[])
{

    lbi=0;
    fgets(linebuf,MAXCOLS,stdin);

    int vi=0,vn=sizeof(*v)/sizeof(**v);

    REP(vi,vn)
    *(v[vi])=0;

    vi=0;

    int s=1;

    while(linebuf[lbi]!='\n' && vi<vn)
    {
        while(!ininc(linebuf[lbi],'0','9'))
            lbi++;
        s=1;
        if(linebuf[lbi-1]=='-')
            s=-1;

        while(ininc(linebuf[lbi],'0','9'))
        {
            *v[vi]=( (*(v[vi])) * 10) + linebuf[lbi] - '0';
            lbi++;
        }

        *v[vi] *= s;
        vi++;
    }
}


#define inp(type,...) { type* aaa[]={__VA_ARGS__}; readints(aaa); }

int main()
{

    #ifndef ONLINE_JUDGE
    //FSTDIN("in.txt");
    #endif


    //Solution here

    int T=1;
    readint(T);
    char s[1001];
    deque<char> s2(1001);
    FORI(t,1,T,1)
    {
        cin>>s;
        s2.clear();
        s2.push_back(s[0]);
        FOR(i,1,strlen(s),1)
        {
            if(s[i]>=s2[0])
                s2.push_front(s[i]);
            else
                s2.push_back(s[i]);
        }
        cout<<"CASE #"<<t<<": ";
        FOR(i,0,strlen(s),1)
        cout<<s2.at(i);
        pc(endl);
         
    }

    return 0;
}