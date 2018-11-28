//humanity is a very illusive quality

/*
Name:
OJ:
Link:
Algorithm:
Type:
Difficulty:
Interest:
Additional:
*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include <ctime>
using namespace std;

class TimeLogger {
    clock_t st, nd; double elapsed;
public:
	TimeLogger() { st = clock(); }
	~TimeLogger() {
		nd = clock(); elapsed = (nd - st)/(double)CLOCKS_PER_SEC;
		printf("\nYour program took %.3lf seconds\n", elapsed);
	}
};

const int    inf = (1<<28);
const double pi  = (2.0*acos(0.0));
const double eps = 1e-9;
const double eps2 = 1e-12; //  printf rounder
const double sensitiveEPS = 1e-14;// depends on digits after . ex 7 digit

typedef long long           lli;
//typedef __int64             lli;
//typedef unsigned long long  llu;
//typedef unsigned __int64    llu;
//typedef pair < int , int >  pii;
//typedef vector < int >      vi;
//typedef vector < string >   vs;

#define isp2( a ) (!(a & (a-1)))
#define CLR( a )  memset(a , 0  , sizeof (a))
#define SET( a , b)  memset(a , b , sizeof (a))
#define SZ( a )   ((int)a.size())
#define all( a )  a.begin(),a.end()


//#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define _rep( i, a, b, x )  for( i = ( a ) ; i <= ( b ) ; i += x )
#define rep( i, n )        _rep( i, 0, n - 1, 1 )
#define _rrep( i, a, b, x ) for( i = (a) ; i >= (b) ; i -= x )
#define rrep( i, a, b)     _rrep( i, a, b, 1)
#define xrep( i, a, b)     _rep( i, a, b, 1)

#define SD( a ) scanf("%d",&a)
#define SL( a ) scanf("%lld",&a)
#define SI( a ) scanf("%I64d",&a)
#define SS( a ) scanf("%s",a)
#define SF( a ) scanf("%lf",&a)

#define pb push_back
#define ff first
#define ss second
///Comparision macros
#define _aEb(a,b) (fabs((a)-(b))<eps)
#define _aGb(a,b) ((a)>(b)+eps)
#define _aLb(a,b) ((a)+eps<(b))
#define _aLEb(a,b) (_aLb(a,b) || _aEb(a,b))
#define _aGEb(a,b) (_aGb(a,b) || _aEb(a,b))
#define _minf(a,b) ((a)+eps<(b)?(a):(b))
#define _maxf(a,b) ((a)+eps<(b)?(b):(a))
#define _sq(x) ((x)*(x))

#define build_unique( x ) x.erase( unique( all(x) ) , x.end() )

int N,J;
vector < int > jc;

lli binInt(int x)
{
    lli val = 0,i;
    rep(i,16+1)
    {
        val *= 10;
        if( x & (1<<(16-i)) ) val+=1;
    }
    return val;
}
lli convert( int val , int b )
{
    lli ans = 0;
    lli bb = 1;
    int i;
    rep(i,16+1)
    {
        if( val & (1<<i) ) ans += bb;
        bb *= b;
    }
    return ans;
}
#define data long long
const int WitnessLoop = 10;
inline bool even(data a)
{
    return (a%2 == 0);
}
inline data mulmod(data a,data b,data c){
    data x = 0 , y = a%c;
    while(b > 0)
    {
        if(b%2 == 1) x = (x+y)%c;
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}
inline void bisect(data &a)
{
    a>>=1;
}
inline data powmod(data a, data k, data n)
{
	data res = 1;
	while( k )
	{
		if( !even(k) )
		{
			res = mulmod(res,a,n);
			--k;
		}
		else
		{
			a = mulmod(a, a, n);
			bisect (k);
		}
	}
	return res;
}
inline bool miller_rabin1(data P) // A bit compact
{
    if( P == 1 ) return false;
	if(P!=2 && P%2==0)  return false;
	data s=P-1;
    while(s%2==0)   s/=2;
    for(int i=0;i<WitnessLoop;i++)
    {
        data a = rand()%(P-1)+1 , temp=s;
        data mod = powmod(a,temp,P);
        while(temp!=(P-1) && mod!=1 && mod!=(P-1))
        {
            mod=mulmod(mod,mod,P);
            temp *= 2;
        }
        if(mod!=(P-1) && temp%2==0) return false; //tempt%2==0 means it was in while()
    }
    return true;
}
void compute_jam()
{
    int i,b;
    int lim = (1<<16);
    int val,val2;
    xrep(i,(1<<15),(1<<16))
    {
        xrep(b,2,10)
        {
            if( miller_rabin1( convert( i , b ) ) )
            {
                break ;
            }
        }
        if( b==11 )
        {
            jc.pb(i);
            if( SZ(jc) == 60 ) return ;
        }
    }
}

inline data gcd (const data &a, const data &b)
{
	return (a == 0) ? b : gcd (b % a, a);
}
#define mabs(a) (((a)>0)?(a):-(a))
inline data pollard_rho(data n)
{
	int i=0,k=2;
	data x=3,y=3;
	while(1)
	{
		i++;
		x = f(x,n);
		data d=gcd(mabs(y-x),n);
		if(d!=1 && d!=n)    return d;
		if(i==k) ///Brent's Cycle
			y=x,k*=2;
	}
}
void print(int x)
{
    printf("%d",x);
    int b;
    xrep(b,2,10) printf(" %lld",convert(x,b));
    printf("\n");
    return;
}
int main(void)
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    //TimeLogger tm;
    int i,j,k,kase=0;

    compute_jam();

    int t;
    SD( t );
    while( t-- )
    {
        SD( N ) , SD( J );
        printf("Case #1:\n");

        rep(i,J)
        {
            printf("%lld",convert(jc[i],10));
            xrep(k,2,10) printf(" %lld",pollard_rho(convert(jc[i],k)));
            printf("\n");
        }
    }
    return 0;
}
