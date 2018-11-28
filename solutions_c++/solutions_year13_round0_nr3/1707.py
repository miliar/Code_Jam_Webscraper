#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>	// require sort next_permutation count __gcd reverse etc.
#include <cstdlib>	// require abs exit atof atoi 
#include <cstdio>		// require scanf printf
#include <functional>
#include <numeric>	// require accumulate
#include <cmath>		// require fabs
#include <climits>
#include <limits>
#include <cfloat>
#include <iomanip>	// require setw
#include <sstream>	// require stringstream 
#include <cstring>	// require memset
#include <cctype>		// require tolower, toupper
#include <fstream>	// require freopen
#include <ctime>		// require srand
#define rep(i,n) for(int i=0;i<(n);i++)
#define ALL(A) A.begin(), A.end()
#define EPS 1e-8
#define DEBUG 1

using namespace std;

typedef long long ll;



const ll ans[] = {
1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004,
100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404,
10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001,
1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 
1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321,
4000008000004, 4004009004004 };

void output (int t, ll res )
{
	printf ("Case #%d: %d\n", t, res );

}

int main()
{
	freopen ("C-large-1.in", "r", stdin );
	freopen ("OUT.C", "w", stdout );
	vector<ll> num; num.clear();
	int n = sizeof (ans ) / sizeof (ans[0] );
	rep (i, n ){
		num.push_back (ans[i] );
	} // end rep

	int t;
	scanf ("%d", &t );
	for (int CASE = 1; CASE <= t; CASE++ ){
		bool ma = false, mb = false;
		ll a, b;
		scanf ("%ld %ld", &a, &b );
		vector<ll>::iterator it1 = lower_bound (ALL (num ), a );
		vector<ll>::iterator jt1 = lower_bound (ALL (num ), b );
		if (*it1 == a ){
			ma = true;
		} // end if
		if (*jt1 == b ){
			mb = true;
		} // end if
		ll res = (jt1 - num.begin() );
		res -= (it1 - num.begin() );
		if ((ma && mb ) || (!ma && mb ) ){
			res++;
		} // end if
		output (CASE, res );
	} // end loop
	return 0;
}
