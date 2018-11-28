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
#define INF 10000*10000*10000LL
stringstream ss;
#define two(x) ( 1LL<<x )
#define sq(x) ( (x)*(x) )
LL mod = 1000000007LL;

/**************************Code****************************/

int n, x, a[1<<20];

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		cin >> n >> x;
		for( int i = 0 ; i < n ; i ++ )
			cin >> a[i];
		sort( a , a+n );
		int i = 0, j = n-1, ans = 0;
		while( i <= j )
		{
			if( a[i] + a[j] <= x )
				i ++, j --, ans ++;
			else
				j --, ans ++;
		}
		cout << "Case #" << ++ cc << ": " << ans << endl;
	}
	return 0;
}
