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


void output (int t  )
{
	printf ("Case #%d: ", t  );

}

int card[2][4][4];

int main()
{
//	freopen ("input.A", "r", stdin );
//	freopen ("output.txt", "w", stdout );
	int t;
	scanf ("%d", &t );
	for (int T = 1; T <= t; T++ ){
		memset (card, 0, sizeof (card ) );
		int a, b;
		scanf ("%d", &a );
		a--;
		set<int> select; select;
		rep (i, 4 ) rep (j, 4 ){
			scanf ("%d", &card[0][i][j] );
			if (i == a ) select.insert (card[0][i][j] );
		} // end rep
		scanf ("%d", &b );
		b--;
		vector<int> res; res.clear();
		rep (i, 4 ) rep (j, 4 ){
			scanf ("%d", &card[1][i][j] );
			if (i == b ){
				if (select.count (card[1][i][j] ) ){
					res.push_back (card[1][i][j] );
				} // end if
			} // end if
		} // end rep

		output (T );
		if (res.size() == 1 ){
			printf ("%d\n", res[0] );
		}else
		if (res.empty() ){
			printf ("Volunteer cheated!\n" );
		}else{
			printf ("Bad magician!\n" );
		} // end if
	} // end for
		
	return 0;
}
