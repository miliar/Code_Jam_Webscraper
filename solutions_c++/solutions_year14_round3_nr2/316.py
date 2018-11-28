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

string s[128];
int mark[128], a[128];

int can( string s )
{
	memset( mark , 0 , sizeof mark );
	for( int i = 0 ; i < s.size() ; )
	{
		if( mark[ s[i]-'a' ] )
			return 0;
		mark[ s[i]-'a' ] = 1;
		int x = i;
		while( i < s.size() && s[i] == s[x] )
			i ++;
	}
	return 1;
}

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		int n;
		cin >> n;
		for( int i = 0 ; i < n ; i ++ )
			cin >> s[i], a[i] = i;
		int ans = 0;
		string str;
		do
		{
			str = "";
			for( int i = 0 ; i < n ; i ++ )
				str += s[ a[i] ];
			if( can( str ) )
				ans ++;
		}while( next_permutation( a , a+n ) );
		cout << "Case #" << ++ cc << ": " << ans << endl;
	}
	return 0;
}

