#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <climits>

#include <string>
#include <complex>
#include <iomanip>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>

#include <map>
#include <set>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <bitset>

#include <new>
#include <limits>
#include <memory>
#include <locale>
#include <iterator>

#include <cwchar>
#include <cerrno>
#include <cfloat>
#include <clocale>
#include <ciso646>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cwctype>

using namespace std;

#define EPS 1e-7
#define INF INT_MAX
#define PI 3.14159265358979323846264338327950
#define RAD PI / 180

#define MEM( x, y ) memset( x, y, sizeof( x ) )
#define IN(F) freopen("in.txt","r",stdin)
#define OUT(F) freopen("out.txt","w",stdout)
#define KS printf("Case #%d: ",++kase)
#define NL printf("\n")
#define DB(n) printf("%d\n",n)
#define llDB(n) printf("%lld\n")
#define py puts("Y")
#define rep(i, n) for(i=0; i<n; i++)
#define repl(i, n) for(i=1; i<=n; i++)

#define SCANi(x) scanf("%d",&x)
#define SCANii(x, y) scanf("%d %d",&x,&y)
#define SCANl(x) scanf("%lld",&x)
#define SCANll(x, y) scanf("%lld %lld",&x,&y)
#define SCANd(x) scanf("%lf",&x)
#define SCANdd(x, y) scanf("%lf %lf",&x,&y)
#define SCANs(x) scanf("%s",x)

#define PRINTi(x) printf("%d\n",x)
#define PRINTii(x, y) printf("%d %d\n",x,y)
#define PRINTl(x) printf("%lld\n",x)
#define PRINTll(x, y) printf("%lld %lld\n",x,y)

#define PB( x ) push_back( x )
#define PF( x ) push_front( x )

/// Powers
template <class T> inline T sqr( T x ) { return x*x; }
template <class T> inline T cube( T x ) { return x*x*x; }
template <class T> inline T quad( T x ) { return x*x*x*x; }
template <class T> inline T powr( T x, T y) { T ret = (T)1; while(y--) ret *= x; return ret;}

/// Precision Equality
template<class T> inline bool Equal(T x, T y) { return fabs(x-y) < EPS;}

/// Bit Manipulation
template <class T> inline T bitSet( T n, T pos ) { return n = n | ( (T)1 << pos ); }
template <class T> inline T bitReset( T n, T pos ) { return n = n & ~( (T)1 << pos ); }
template <class T> inline bool bitCheck( T n, T pos ) { return n & ( (T)1 << pos ); }

/// GCD, LCM
template <class T> inline T GCD( T a, T b ) { if( a < 0 ) return GCD( -a , b );
    if( b < 0 ) return GCD( a, -b ); return ( b == 0 ) ? a : GCD( b, a%b ); }
template <class T> inline T LCM( T a, T b ) { if( a < 0 ) return LCM( -a, b );
    if( b < 0 ) return LCM( a, -b ); return a * ( b / GCD( a, b ) ); }

/// Prime
template <class T> inline bool isPrime( T n ) { if( n <= 1 ) return false;
    for( T i = 2; i*i <= n; i++ ) if( n % i == 0 ) return false; return true; }


/// Debugs
template <class T> inline void debug( T x )
{ cout << "x = " << x << endl; }
template <class T1, class T2> inline void debug( T1 x, T2 y )
{ cout << "x = " << x << ", y = " << y << endl; }
template <class T1, class T2, class T3> inline void debug( T1 x, T2 y, T3 z )
{ cout << "x = " << x << ", y = " << y << ", z = " << z << endl; }

/// 4 Direction
int dx[]={+1,-1,+0,+0};
int dy[]={+0,+0,+1,-1};

/// 8 Direction
//int dx[]={+0,+0,+1,-1,-1,+1,-1,+1};
//int dy[]={-1,+1,+0,+0,+1,+1,-1,-1};


/// Operator overload
// bool operator < ( const className& c ) const { return w > c.w; }


typedef long long int i64;


int main()
{
    int i,curr_standing, deff, extra, t, kase=0, mx, len;
    char s[1500];
    IN(F);
    OUT(F);

    SCANi(t);
    while(t--)
    {
        SCANi(len);
        SCANs(s);

        curr_standing = extra = 0;

        for(i=0; i<=len; i++)
        {
            if(s[i] != '0')
            {
                deff = i - curr_standing;
                if(deff > 0)
                {
                    extra += deff;
                    curr_standing += deff;
                }
                curr_standing += s[i] - 48;
            }

        }

        KS; PRINTi(extra);
    }

    return 0;
}
