//BISMILLAHIRRAHMANIRRAHIM
/*
 manus tar shopner soman boro
 Author :: Shakil Ahmed
.............AUST_CSE27.........
 prob   ::
 Type   ::
 verdict::
 */

#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define pi acos(-1.0)
#define ff first
#define ss second
#define re return
#define QI queue<int>
#define SI stack<int>
#define SZ(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define ms(a,b) memset((a),(b),sizeof(a))
#define G() getchar()
#define MAX3(a,b,c) max(a,max(b,c))
#define II ( { int a ; read(a) ; a; } )
#define LL ( { Long a ; read(a) ; a; } )
#define DD ({double a; scanf("%lf", &a); a;})

double const EPS=3e-8;
using namespace std;

#define FI freopen ("input.txt", "r", stdin)
#define FO freopen ("1.txt", "w", stdout)

typedef long long Long;
typedef long long int64;
typedef unsigned long long ull;
typedef vector<int> vi ;
typedef set<int> si;
typedef vector<Long>vl;
typedef pair<int,int>pii;
typedef pair<string,int>psi;
typedef pair<Long,Long>pll;
typedef pair<double,double>pdd;
typedef vector<pii> vpii;

// For loop

#define forab(i, a, b)	for (__typeof (b) i = (a) ; i <= b ; ++i)
#define rep(i, n)		forab (i, 0, (n) - 1)
#define For(i, n)		forab (i, 1, n)
#define rofba(i, a, b)	for (__typeof (b)i = (b) ; i >= a ; --i)
#define per(i, n)		rofba (i, 0, (n) - 1)
#define rof(i, n)		rofba (i, 1, n)
#define forstl(i, s)	for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)

template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }

//Fast Reader
template<class T>inline bool read(T &x){int c=getchar();int sgn=1;while(~c&&c<'0'||c>'9'){if(c=='-')sgn=-1;c=getchar();}for(x=0;~c&&'0'<=c&&c<='9';c=getchar())x=x*10+c-'0'; x*=sgn; return ~c;}

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction

/* **************************************  My code start here ****************************************** */
const int MX = 1e6 + 10 ;
bool vis[MX] ;
int rev( int x)
{
    vector < int > num ;
    while( x )
    {
        num.pb( x % 10 );
        x/=10;
    }
    reverse ( num.begin() , num.end() );
    int i ;
    int mul = 1 ;
    int cur = 0 ;
    rep( i , num.size() )
    {
        cur = cur + ( num[i] * mul );
        mul *= 10 ;
    }
    return cur ;
}
int main()
{
   // I will always use scanf and printf
   // May be i won't be a good programmer but i will be a good human being
      FI ;
      FO ;
     int cs , t = II ;
     for ( cs = 1 ; cs <= t ; cs++ )
     {
         int n = II ;
         queue < pii > q ;
         rep( i ,  n + 1 ) vis[i] = 0 ;
         q.push( mp( 1 , 1 ) ) ;
         vis[1] = 1 ;
         int ans = 0 ;
         while( !q.empty() )
         {
             int now = q.front().ff ;
             int c = q.front().ss ;
             q.pop();
             if( now == n )
             {
                 ans = c  ;
                 break;
             }
             if( now  + 1 <= n && !vis[now + 1 ] )
             {
                 vis[now + 1] = 1 ;
                 q.push( mp ( now  + 1 ,c + 1 ));
             }
             int rv = rev( now );
             if( rv <= n && !vis[rv] )
             {
                 vis[rv] = 1 ;
                 q.push( mp ( rv , c + 1 ) );
             }
         }
         printf("Case #%d: %d\n",cs,ans);


     }


    return 0;
}
