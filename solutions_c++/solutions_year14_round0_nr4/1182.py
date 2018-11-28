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

int a[1024], b[1024], m1[1024], m2[1024];

int main()
{
	int t, cc = 0, n;
	cin >> t;
	while( t -- )
	{
		double x;
		cin >> n;
		for( int i = 0 ; i < n ; i ++ )
			cin >> x, a[i] = x * 1000000 + EPS;
		for( int i = 0 ; i < n ; i ++ )
			cin >> x, b[i] = x * 1000000 + EPS;
		int y = 0, z = 0;
		for( int i = 0 ; i < n ; i ++ )
			m1[i] = m2[i] = 0;
		for( int i = 0 ; i < n ; i ++ )
		{
			int mn_a = -1, mn_b = -1, mx = -1;
			for( int j = 0 ; j < n ; j ++ )
				if( !m1[j] && ( mn_a == -1 || a[mn_a] > a[j] ) )
					mn_a = j;
			for( int j = 0 ; j < n ; j ++ )
				if( !m2[j] && ( mn_b == -1 || b[mn_b] > b[j] ) )
					mn_b = j;
			for( int j = 0 ; j < n ; j ++ )
				if( !m1[j] && a[j] > b[mn_b] && ( mx == -1 || a[mx] > a[j] ) )
					mx = j;
			if( mx == -1 )
				break;
			else
				m1[mx] = m2[mn_b] = 1, y ++;
		}
		for( int i = 0 ; i < n ; i ++ )
			m1[i] = m2[i] = 0;
		for( int i = 0 ; i < n ; i ++ )
		{
			int mx_a = -1, mx_b = -1, mn_b = -1;
			for( int j = 0 ; j < n ; j ++ )
			{
				if( !m1[j] && ( mx_a == -1 || a[mx_a] < a[j] ) )
					mx_a = j;
				if( !m2[j] && ( mx_b == -1 || b[mx_b] < b[j] ) )
					mx_b = j;
				if( !m2[j] && ( mn_b == -1 || b[mn_b] > b[j] ) )
					mn_b = j;
			}
			if( a[mx_a] > b[mx_b] )
				m1[mx_a] = m2[mn_b] = 1, z ++;
			else
				m1[mx_a] = m2[mx_b] = 1;
		}
		cout << "Case #" << ++ cc << ": " << y << " " << z << endl;
	}
	return 0;
}
