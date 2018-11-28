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
#include "UnionFind.h"

#define	numberof(a)	(sizeof(a) / sizeof(a[0]))
#define	INF		(1000000)
#define Rep(i,n) for(int i = 0; i < (n); i++ )

using namespace std;

typedef vector< vector<int> > mat;
typedef pair<int, int> P;
typedef long long ll;
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

bool isPalindromes( ll num )
{
	stringstream ss("");
	string str = "";

	ss << num;
	ss >> str;
	ss.clear();
	ss.str("");

	const ll len = str.length();
	bool ok = true;
	for( int k = 0; k < len / 2; ++k ){
		if( str[k] != str[len - k - 1] ){
			ok = false;
			break;
		}
	}

	return ok;
}

ll solve( ll A, ll B )
{
	ll ret = 0;

	for( ll i = A; i <= B; ++i ){
		ll check = i;

		// is square?
		long double sqr = sqrt( static_cast<long double>(check) );
		if( ceil(sqr) != floor(sqr) ){
			continue;
		}

		// is palindromes?
		if( !isPalindromes(check) ){
			continue;
		}

		// is sqrt palindromes?
		ll check2 = ceil(sqr);
		if( !isPalindromes(check2) ){
			continue;
		}

		ret++;
	}

	return ret;
}

int main()
{
	int T = 0;
	ll A = 0, B = 0;
	vector< ll > ans;

	cin >> T;

	Rep(t, T){
		cin >> A >> B;
		ans.push_back( solve(A, B) );
	}
	Rep(t, T){
		cout << "Case #" << t + 1 << ": ";
		cout << ans[t] << endl;
	}

	// stop
	cin >> T;

	return 0;
}



