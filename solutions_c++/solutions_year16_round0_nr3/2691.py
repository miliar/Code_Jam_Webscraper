//BISMILLAHIRRAHMANIRRAHIM
/*
 manus tar shopner soman boro
 all my suceesses are dedicated to my parents
 The true test of a man's character is what he does when no one is watching.
 Don't let your dreams be dreams.


 Author :: Shakil Ahmed
.............AUST_CSE27.........
 prob   ::
 Type   ::
 verdict::

*/

#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair

// Macro
#define eps 1e-9
#define pi acos(-1.0)
#define ff first
#define ss second
#define re return
#define QI queue<int>
#define SI stack<int>
#define SZ(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sq(a) ((a)*(a))
#define distance(a,b) (sq(a.x-b.x) + sq(a.y-b.y))
#define iseq(a,b) (fabs(a-b)<eps)
#define eq(a,b) iseq(a,b)
#define ms(a,b) memset((a),(b),sizeof(a))
#define G() getchar()
#define MAX3(a,b,c) max(a,max(b,c))
#define II ( { int a ; read(a) ; a; } )
#define LL ( { Long a ; read(a) ; a; } )
#define DD ({double a; scanf("%lf", &a); a;})

double const EPS=3e-8;
using namespace std;

#define FI freopen ("1.txt", "r", stdin)
#define FO freopen ("2.txt", "w", stdout)

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
#define __(args...) {dbg,args; cerr<<endl;}
struct debugger{template<typename T> debugger& operator , (const T& v){cerr<<v<<"\t"; return *this; }}dbg;
#define __1D(a,n) rep(i,n) { if(i) printf(" ") ; cout << a[i] ; }
#define __2D(a,r,c,f) forab(i,f,r-!f){forab(j,f,c-!f){if(j!=f)printf(" ");cout<<a[i][j];}cout<<endl;}

template<class A, class B> ostream &operator<<(ostream& o, const pair<A,B>& p){ return o<<"("<<p.ff<<", "<<p.ss<<")";} //Pair print
template<class T> ostream& operator<<(ostream& o, const vector<T>& v){ o<<"[";forstl(it,v)o<<*it<<", ";return o<<"]";} //Vector print
template<class T> ostream& operator<<(ostream& o, const set<T>& v){ o<<"[";forstl(it,v)o<<*it<<", ";return o<<"]";} //Set print

//Fast Reader
template<class T>inline bool read(T &x){int c=getchar();int sgn=1;while(~c&&c<'0'||c>'9'){if(c=='-')sgn=-1;c=getchar();}for(x=0;~c&&'0'<=c&&c<='9';c=getchar())x=x*10+c-'0'; x*=sgn; return ~c;}

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction

/* **************************************  My code start here ****************************************** */

const int NX = ( 1 << 16 );
const int MX = 1e6;
int prime[ MX ] , id , chk[ MX ];
int limit = 2 , idx = 1 ;
Long ans[ 55 ][ 20 ];
int vis[ NX ][ 19 ][ 19 ];

map < Long , int > taken ;

void ini()
{
    prime[id++] = 2 ;
    int i ;
    for( i = 3 ; ( Long ) i * i < MX ; i+= 2 )
    {
        if( chk[i] == 0 )
        {
            prime[id++] = i ;
            for( int j = i * i ; j < MX ; j += ( 2 * i ) ) chk[j] = 1 ;
        }
    }
    while( i < MX )
    {
        if( chk[i] == 0 ) prime[id++] = i ;
        i += 2 ;
    }
}
bool isPrime( Long x )
{
    for( int i = 0 ; i < id && ((Long) prime[i] * prime[i]) <= x ; i++ ) if( x % prime[i] == 0 ) return 0;
    return 1 ;
}


bool Possile( int mask )
{
    bool ok = 0 ;
    for( Long i = 2 ; i <= 10 && ok == 0 ; i++ )
    {
        Long val = 1 ;
        Long value = 0 ;
        for( int j = 0 ; j < 16 ; j++ )
        {
            if( mask & ( 1 << j ) )
            {
                value += val ;
            }
            val *= i ;
        }
      //  printf(" mask :: %d value :: %lld i :: %d\n" , mask , value , i );
        ok = isPrime( value );
        ans[ idx ][ ( int ) i ] = value ;
    }
    if( ok ) return 0 ;
    else return 1 ;
}

Long Even( Long x )
{
    for( int i = 0 ; i < id ; i++ )
    {
        if( x % prime[i] == 0 )
        {
            return prime[i];
        }
    }
    return -1 ;
}

void check( int mask )
{
    if( Possile(mask) )
    {
            Long sv = ans[idx][10];
          //  cout << " sv " << sv << endl ;
            bool evenly = 1 ;
            for( int i = 2 ; i <= 10 && evenly ; i++ )
            {
                Long v = Even( ans[idx][i] );
                if( v == -1 ) continue;
                else ans[ idx ][ i ] = v ;
            }

                ans[idx][1] = sv ;
               // printf(" idx :: %d ans : %lld\n" , idx , ans[idx][1]);
                idx++;
                limit--;


    }
}


void dfs( int mask , int pos , int can )
{
    if( limit == 0 ) return ;
    if( pos == 16 )
    {
        if( can == 0 )
        check( mask );
        return ;
    }
    if( vis[ mask ][ pos ][ can ] ) return ;
    vis[ mask ][ pos ][ can ] = 1;
    if( pos == 15 || pos == 0 )
    {
       dfs( mask | ( 1 << pos ) , pos + 1 , can );
    }
    else
    {
        if( 14 - pos + 1 == can ) dfs( mask | ( 1 << pos ) , pos + 1 , can - 1 );
        else
        {
            if( can > 0 )
            {
                dfs( mask | ( 1 << pos ) , pos + 1 , can - 1 );
                dfs( mask , pos + 1 , can );
            }
            else
            {
                dfs( mask , pos + 1 , can ) ;
            }
        }
    }
}

int main()
{
   // I will always use scanf and printf
   // May be i won't be a good programmer but i will be a good human being
   FI ;
   FO ;
   ini();
   int cs , t = II , n;
   for( cs = 1 ; cs <= t ; cs++ )
   {
       n = II , limit = II ;
       idx = 1 ;
       int mask = ( 1 << 15 );
       mask |= ( 1 << 0 );
       int sv = mask ;
       check( sv );
       for( int i = 1 ; i <15 && limit > 0; i++ )
       {
           dfs( 0 , 0 , i );
       }

       printf("Case #1:\n");
       for( int i = 1 ; i <= 50 ; i++ )
       {
           for( int j = 1 ; j <= 10 ; j++ )
           {
               if( j > 1 ) printf(" ");
               printf("%lld",ans[i][j]);
           }
           puts("");
       }

   }

    return 0;
}
