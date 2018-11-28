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

using namespace std;

typedef long long ll;


void output (int t )
{
	printf ("Case #%d: ", t );

}

bool is_pow2 (ll b ){
	ll res = 1LL;
	if (res == b ) return true;
	for (; res <= b; res <<= 1 ){
		if (res == b ) return true;
	} // end for

	return false; 
}

int main()
{
	int T;
	scanf ("%d", &T );
	for (int t=1; t<=T; t++ ){
		ll a, b;
		scanf ("%ld/%ld", &a, &b );
		ll g = (ll)__gcd (a, b );
		a /= g; b /= g;
		int res = 0;
		if (!is_pow2 (b ) ){
			res = -1;
		}else{
			while (a < b ){
				a *= 2LL;
				ll g = (ll)__gcd (a, b );
				a /= g, b /= g;
				res++;
			} // end while
		} // end if
		output (t );
		if (res != -1 ){
			cout << res << endl;
		}else{
			cout << "impossible" << endl;
		} // end if
	} // end for
		
	return 0;
}
