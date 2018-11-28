#include <list>
#include <set>
#include <map>
#include <ctime>
#include <stack>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <deque>
#include <bitset>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <iterator>
#include <cassert>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <complex>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
 
#define LL long long
#define int64 LL

typedef vector < int > VI;
typedef pair< int , int > pii;
typedef pair < LL , LL > PLL;
#define fr first
#define se second
#define pi M_PI
#define rad(x) (x)*acos(-1)/180.0
#define EPS 1e-7
#define INF 10000*10000*10000LL
stringstream ss;
#define two(x) ( 1LL<<x )
#define sq(x) ( (x)*(x) )
LL mod = 1000000007LL;

/**************************Code****************************/


int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		double ans = 1e20, now = 0., R = 2.;
		double C, F, X;
		cin >> C >> F >> X;
		ans = X / 2.;
		for( int i = 1 ; i <= X ; i ++ )
		{
			now = now + ( C / R ), R += F;
			ans = min( ans , now + X / R );
		}
		printf( "Case #%d: %.7lf\n" , ++ cc , ans );
	}
	return 0;
}
