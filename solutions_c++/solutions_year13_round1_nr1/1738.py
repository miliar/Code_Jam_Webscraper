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


void output (int t, int res )
{
	printf ("Case #%d: %d\n", t, res  );

}


int main()
{
	freopen ("A-small-attempt0.in", "r", stdin );
//	freopen ("input.A", "r", stdin );
	int CASE;
	scanf ("%d", &CASE );
	for (int c = 1; c <= CASE; c++ ){
		int r, t;
		scanf ("%d %d", &r, &t );
		int curr = 0;
		int k = 0;
		while (	curr + (r+2*k+1)*(r+2*k+1) - (r+2*k)*(r+2*k ) <= t ){
			curr += (r+2*k+1)*(r+2*k+1) - (r+2*k)*(r+2*k );
			k++;
		} // end while
		output (c, k );
	} // end for
	
	return 0;
}
