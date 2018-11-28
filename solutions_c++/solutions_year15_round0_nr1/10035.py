////////////////////////////////////////////////////////////////////
// This source code is for Visual C++ 2010 Express
////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <stack>
#include <functional>
#include <iomanip>
#include <string>
#include <cstring>
#include <deque>
#include <math.h>
//#include "UnionFind.h"

#define	numberof(a)	(sizeof(a) / sizeof(a[0]))
#define	INF		(1000000)
#define Rep(i,n) for(int i = 0; i < (n); i++ )

using namespace std;

typedef vector< vector<int> > mat;
typedef pair<int, int> P;
typedef long long ll;
typedef unsigned long long ull;
struct Point{
	ll x;
	ll y;
	Point() {};
	Point( ll xx, ll yy ) : x(xx), y(yy) {};
};

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

ll solve( string audience, ll Smax )
{
	ll invite_num = 0;
	ll standup_sum = 0;

	Rep(S, Smax + 1){
		ll people = audience[S] - '0';// people in S_i

		if( people == 0 ) continue;

		if( standup_sum >= S ){
			// do nothing
		}
		else{
			// invite
			invite_num += S - standup_sum;
			standup_sum += invite_num;
		}

		// add
		standup_sum += people;
	}

	return invite_num;
}

int main()
{
	ll T = 0;
	vector<ll> result;

	cin >> T;

	Rep(t, T){
		ll Smax = 0;
		string str = "";

		cin >> Smax;
		cin >> str;

		result.push_back( solve(str, Smax) );
	}

	Rep(t, T){
		cout << "Case #" << t + 1 << ": " << result[t] << endl;
	}

	return 0;
}



