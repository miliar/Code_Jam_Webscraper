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
#define DEBUG 0

using namespace std;

void output (int t, int res )
{
	printf ("Case #%d: ", t );
	if (res ){
		printf ("YES\n" );
	}else{
		printf ("NO\n" );
	} // end switch
}

int a[105][105];
int b[105][105];

void disp_b (int n, int m )
{
	rep (i, n ){
		rep (j, m ){
			cout << b[i][j];
		} // end rep
		cout << endl;
	} // end rep
	cout << endl;
}

bool more2 (int n, int m )
{
	rep (i, n ) rep (j, m ) b[i][j] = 100;

	vector<int> cut; cut.clear(); 
	rep (i, n ) rep (j, m ) cut.push_back (a[i][j] );
	sort (ALL (cut ) );
	cut.erase (unique (ALL (cut ) ), cut.end() );
	sort (ALL (cut ), greater<int>() );

	rep (c, cut.size() ){
		rep (i, n ){
			set<int,greater<int> > curr;
			rep (j, m ){
				curr.insert (a[i][j] );
			} // end rep
			rep (j, m ) b[i][j] = min (b[i][j], *curr.begin() );
		} // end rep
		rep (j, m ){
			set<int,greater<int> > curr;
			rep (i, n ){
				curr.insert (a[i][j] );
			} // end rep
			rep (i, n ) b[i][j] = min (b[i][j], *curr.begin() );
		} // end rep
#if DEBUG
	disp_b (n, m );
#endif
	} // end rep

	bool res = true;
	rep (i, n ){
		rep (j, m ){
			if (a[i][j] != b[i][j] ){
				res = false;
				break;
			} // end if
		} // end rep
	} // end rep
	
	return res;
}
bool calc (int n, int m )
{
	set<int> ans;
	ans.insert (a[0][0] ); ans.insert (a[n-1][0] );
	ans.insert (a[0][m-1] ); ans.insert (a[n-1][m-1] );
	bool res;

	if (n == 1 || m == 1 ){
		return true;
	}else
	if (n == 2 && m == 2 ){
		if ((a[0][0] == a[0][1] && a[1][0] == a[1][1] ) || (a[0][0] == a[1][0] && a[0][1] == a[1][1] ) ) return true;
		else return false;
	}else{
		return more2 (n, m );
	} // end if

	return false;
}

int main()
{
	freopen ("B-large.in", "r", stdin );
//	freopen ("input.B8", "r", stdin );
	freopen ("OUT.B", "w", stdout );
	int t;
	scanf ("%d", &t );
	for (int CASE = 1; CASE <= t; CASE++ ){
		memset (a, 0, sizeof (a ) );
		memset (b, 0, sizeof (b ) );
		int n, m;
		scanf ("%d %d", &n, &m );
		rep (i, n ){
			rep (j, m ){
				scanf ("%d", &a[i][j] );
			} // end rep
		} // end rep

		bool res = calc (n, m );
		output (CASE, res );

	} // end loop
		
	return 0;
}
