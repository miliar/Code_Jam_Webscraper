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


void output (int t, double res ){
	printf ("Case #%d: %lf\n", t, res  );

}
double solve (double C, double F, double X ){
	double currF = 2.;
	double curr = 0., next = 0.;

	curr = X/currF;
	while (true ){
		next += C/currF;
		currF += F;
//		cerr << "curr: " << curr << " next: " << next + X/currF << endl;
		if (curr < next + X/currF ){
			return curr;
		} // end if
		curr = next + X/currF;
	} // end while
}

int main(){
//	freopen ("input.B", "r", stdin );
//	freopen ("output.txt", "w", stdout );
	int T;
	scanf ("%d", &T );
	for (int t = 1; t <= T; t++ ){
		double C, F, X;
		scanf ("%lf %lf %lf", &C, &F, &X );
		double res = solve (C, F, X );
		output (t, res );
	} // end for
		
	return 0;
}
