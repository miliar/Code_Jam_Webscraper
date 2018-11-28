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

// Type limits
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
#define clra(a)                memset( (a),  0,    sizeof (a) )
#define seta(a,val)            memset( (a),  (val),  sizeof(a) )
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


// Check if in range
#define ininc(a,b,c) (((b) <= (a)) && ((a) <= (c)))
#define inexc(a,b,c) (((b) < (a)) && ((a) < (c)))
#define outinc(a,b,c) (((a) <= (b)) || ((a) >= (c)))
#define outexc(a,b,c) (((a) < (b)) || ((a) > (c)))

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

#define FSTDIN(f)             freopen(f, "r", stdin);
#define FSTDOUT(f)            freopen(f, "w", stdout);

#define _UNSYNCIO             ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
// use only if using cin cout
// printf scanf freopen maynot work


//Fast I/O goes here


//DEBUG

#ifdef DEBUG
// Assert without abort
#define is(x) if(!(x)){cerr<<"cerr> Check failed: "#x<<endl;}
#define Bound(A, B, C) is( B <= A && A <= C)
// Trace variables
#define pendl   cout<<endl;
#define XDEBUG1(x) cerr << #x << "=" << x << "; ";
#define XDEBUG2(a,b)   XDEBUG1(a) XDEBUG1(b)
#define XDEBUG3(a,b,c)  XDEBUG2(a,b) XDEBUG1(c)
#define XDEBUG4(a,b,c,d)  XDEBUG3(a,b,c) XDEBUG1(d)
#define XDEBUG5(a,b,c,d,e)  XDEBUG4(a,b,c,d) XDEBUG1(e)
#define XDEBUG6(a,b,c,d,e,f)  XDEBUG5(a,b,c,d,e) XDEBUG1(f)
#define debug(...) cerr<<"cerr> "; GET_MACRO(__VA_ARGS__, XDEBUG6, XDEBUG5, XDEBUG4,XDEBUG3, XDEBUG2, XDEBUG1)(__VA_ARGS__) cerr<<endl;
#define GET_MACRO(_1,_2,_3,_4,_5,_6,NAME,...) NAME
#endif
#ifndef DEBUG
#define debug(...) ;
#endif


/// I/O End

 
/// Functions Start

//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

template < class T > T teql( T a, T b ){return ( abs(a-b) < EPS );}                      // a==b

template < class T > T tge( T a, T b ){return ( a > b-EPS );}                            // a>=b
template < class T > T tgt( T a, T b ){return ( a >= b+EPS );}                          // a>b

template < class T > T tle( T a, T b ){return ( a < b-EPS );}                            // a<=b
template < class T > T tlt( T a, T b ){return ( a <= b+EPS );}                          // a<b

//@@@@@@@@@@@@@@@@@@@@@@@//////////////////////////////////////////////////////////// check above comp


template<typename T> inline int sgn(const T& x){return (x>+EPS)-(x<-EPS);}
template<typename T> inline int cmp(const T& a,const T& b){return tsgn(a-b);}

template < class T > inline T rmax( T a, T b ){return ( a > b ? a : b );}
template < class T > inline T rmin( T a, T b ){return ( a < b ? a : b );}              //Return 
template<typename T> inline bool smax(T& a,const T& b){return a<b?a=b,true:false;}     //Set a
template<typename T> inline bool smin(T& a,const T& b){return b<a?a=b,true:false;}

template<typename T> inline T sqr(const T& x){return x*x;}
template<typename T> inline T cub(const T& x){return x*x*x;}

template<typename T> inline T mod(const T& x){return x%MOD;}

template<typename T> inline T gcd(T a,T b){if(b)while((a%=b)&&(b%=a));return a+b;}
template<typename T> inline T lcm(T a,T b){return a*b/gcd(a,b);}



// STL Ops

//Pair operators
template<typename T> inline pair<T, T> operator-(const pair<T, T>& x){return mp(-x.first,-x.second);}           // -pair elementwise neg
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

template < class T > string vtostr( vector<T> &v ){SS x; VFOR(it,v) x<<v[it];  return x.str();} 
template < class T > string strtov( vector<T> &v ){SS x; T n; while(x>>n)v.pb(n);} 


// Bit functions go here


/// Functions End
 

//Unsync stdio for fast io
struct Initializer{
time_t programstarttime;
Initializer(){

    _UNSYNCIO

    programstarttime=clock();}
~Initializer(){
    #ifdef DEBUG
    //cerr << "cerr> Program ran in "<< ( clock()-programstarttime ) / CLOCKS_PER_SEC << " s " << endl;
    #endif
}
}initializer;


char dig[10][10]={"ZERO", "TWO",  "EIGHT", "SIX", "THREE", "FOUR", "FIVE",  "SEVEN", "NINE", "ONE"};
int num[10]={0,2,8,6,3,4,5,7,9,1};

int main()
{

    //Solution here

    li T=1;

    int f,i;

    string s,no,stemp;

    cin>>T;

    for(li t=1; t<=T; t++)
    {
        no="";
        cin>>s;


        for(i=0;i<10;)
        {
            stemp=s;

            f=1;
            FOR(j,0,strlen(dig[i]),1)
            {
                //debug(s,i,j);
                if(s.find(dig[i][j])!=std::string::npos)
                {
                    s.erase(s.find(dig[i][j]),1);
                }else
                {  
                    f=0;
                    break;
                }

            }
            if(f!=1)
            {
                s=stemp;
                i++;
            }
            else
                no+=num[i]+'0';
        }

        sort(no.begin(), no.end());

        cout<<"Case #"<<t<<": ";
        cout<<no;
        // print o/p

        cout<<endl; 
    }

    return 0;
}