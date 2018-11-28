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

//typedef long long           lli;
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
int n;
int mote[200],my;
int eat(int &m,int k)
{
    int step=0;
    if(m-1<=0) return inf;
    while(m<=k) step++ , m+= (m-1);
    return step;
}
int main(void)
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("outAsmall-1.txt","w",stdout);
    //freopen("in2.cpp","w",stdout);
    //TimeLogger tm;
    int i,j,k,kase=0;
    int t;SD( t );
   // printf("%d\n",t);
    while( t-- )
    {

        SD(my),SD(n);
        rep(i,n) SD(mote[i]) ;
        sort(mote,mote+n);
        int step=0;
        rep(i,n)
        {
            if(my<=mote[i])
            {
                int tmp = eat(my,mote[i]);
                my+= mote[i];
                if(n-i <= tmp)
                {
                    step+=(n-i);
                    break;
                }
                step+=tmp;
            }
            else
            {
                my+=mote[i];
            }
        }
        printf("Case #%d: %d\n",++kase,step);
    }
    return 0;
}
