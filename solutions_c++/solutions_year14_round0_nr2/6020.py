// Standard I/O
#include <iostream>
#include <sstream>
#include <cstdio>
// Standard Library
#include <cstdlib>
#include <ctime>
#include <cmath>
// Template Class
#include <string>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <stack>
// Container Control
#include <algorithm>

using namespace std;

#define rep( i, n ) for( int i = 0; i < n; ++i )
#define reep( i, s, n ) for ( int i = s; i < n; ++i )

typedef vector<int>::iterator vi_itr;
typedef list<int>::iterator li_itr;

typedef pair<int, int> pii;
typedef list<int> li;
typedef vector<int> vi;
typedef vector< vector<int> > vii;

int main()
{
	int T;
	cin >> T;

	rep(n, T){
		double cur_cookie = 0, cps = 2.0;
		double C, F, X, time = 0.0;
		double ans = 1E10;
		
		cin >> C >> F >> X;
		while( ans > time ){
			ans = min(ans, time + X / cps);

			double tmp = C / cps;
			cps += F;
			time += tmp;
		}

		printf("Case #%d: %.10f\n", n+1, ans);
	}
}
