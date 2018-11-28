
// default code for competitive programming
// c2251393 ver 3.141 {{{

// Includes
#include <bits/stdc++.h>

// Defines
#define NAME(x) #x
#define SZ(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()
#define FOR(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define REP(i, s, e) for(int i = (s); i <= (e); i++)
#define REPD(i, s, e) for(int i = (s); i >= (e); i--)
#define DEBUG 1
#define fst first
#define snd second
 
using namespace std;

// Typedefs
typedef double real;
typedef long long ll;
typedef pair<ll, int> pli;
typedef tuple<ll, int> tli;
typedef pair<int, int> pii;
typedef tuple<int, int> tii;
typedef unsigned long long ull;

// Some common const.
const double EPS = 1e-9;
const double Pi = acos(-1);
 
// Equal for double
bool inline equ(double a, double b)
{return fabs(a - b) < EPS;}

// }}}
// start ~~QAQ~~

const int MAXN = 110;

typedef tuple< double , double > tdd;

int n;
double V , X , r[ MAXN ] , c[ MAXN ];
tdd in[ MAXN ];

bool go( double mid )
{
  double rl , rr;
  double acc = 0.0 , rst = V , temp = 0.0;
  REP( i , 1 , n )
  {
    double R , C;
    tie( C , R ) = in[ i ];
    double get = min( mid * R, rst );
    temp = temp + get * C;
    acc += get;
    rst -= get;
    if( rst < EPS ) break ;
  }
  if( rst > EPS ) return 0;
  rl = temp / V;
  acc = 0.0 , rst = V , temp = 0.0;
  REPD( i , n , 1 )
  {
    double R , C;
    tie( C , R ) = in[ i ];
    double get = min( mid * R, rst );
    temp = temp + get * C;
    acc += get;
    rst -= get;
    if( rst < EPS ) break ;
  }
  if( rst > EPS ) return 0;
  rr = temp / V;

  return rl - EPS < X && X < rr + EPS;
}

ll getint(){
    ll _x=0,_tmp=1; char _tc=getchar();
    while( (_tc<'0'||_tc>'9')&&_tc!='-' ) _tc=getchar();
    if( _tc == '-' ) _tc=getchar() , _tmp = -1;
    while(_tc>='0'&&_tc<='9') _x*=10,_x+=(_tc-'0'),_tc=getchar();
    return _x*_tmp;
}

tdd getS()
{
  int ri , rq , ci , cq;
  ri = getint();
  rq = getint();
  ci = getint();
  cq = getint();
  return tdd( ci * 10000 + cq , ri * 10000 + rq );
}

int main()
{
  int tc;tc = getint();//cin >> tc;
  REP( _ , 1 , tc )
  {printf( "Case #%d: " , _ );
    //cin >> n;
    n = getint();
    tie( X , V ) = getS();
    REP( i , 1 , n )
    {
      in[ i ] = getS();
    }
    sort( in + 1 , in + n + 1 );
    bool flag = 0;
    double lb = 0.0 , ub = 1e13;
    REP( T , 1 , 1000 )
    {
      double mid = ( lb + ub ) * 0.5;
      //double tl , tr;
      //tie( tl , tr ) = go( mid );
      //if( tl - EPS < X && X < tr + EPS )
      if( go( mid ) )
      {
        ub = mid;
        flag = 1;
      }
      else lb = mid;
    }
    if( flag ) printf( "%.10f\n" , lb );
    else puts( "IMPOSSIBLE" );
  }
}


