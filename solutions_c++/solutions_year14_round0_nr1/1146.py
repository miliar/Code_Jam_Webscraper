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

int a[5][5], b[5][5], cnt[32];

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		int n, m, id = 0, all = 0;
		memset( cnt , 0 , sizeof cnt );
		cin >> n;
		for( int i = 1 ; i <= 4 ; i ++ )
			for( int j = 1 ; j <= 4 ; j ++ )
				cin >> a[i][j];
		cin >> m;
		for( int i = 1 ; i <= 4 ; i ++ )
			for( int j = 1 ; j <= 4 ; j ++ )
				cin >> b[i][j];
		for( int i = 1 ; i <= 4 ; i ++ )
		{
			cnt[ a[n][i] ] |= 1;
			cnt[ b[m][i] ] |= 2;
		}
		for( int i = 1 ; i <= 16 ; i ++ )
			if( cnt[i] == 3 )
				all ++, id = i;
		cout << "Case #" << ++ cc << ":";
		if( !all )
			cout << " Volunteer cheated!" << endl;
		else if( all > 1 )
			cout << " Bad magician!" << endl;
		else
			cout << " " << id << endl;
	}
	return 0;
}
