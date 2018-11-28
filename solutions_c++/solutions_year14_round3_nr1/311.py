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
#define EPS 1e-6
#define INF 10000*100000
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
		LL p, q;
		char ch;
		cin >> p >> ch >> q;
		LL g = __gcd( p , q );
		p /= g;
		q /= g;
		if( q & ( q-1 ) )
			cout << "Case #" << ++ cc << ": impossible" << endl;
		else
		{
			int ans = 0;
			while( p < q )
			{
				p %= q;
				p *= 2;
				ans ++;
			}
			cout << "Case #" << ++ cc << ": " << ans << endl;
		}
	}
	return 0;
}

