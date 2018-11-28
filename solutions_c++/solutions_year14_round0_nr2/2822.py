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

double solve( double C, double F, double X )
{
	double ret = 0.0;
	ll farmNum = 0;

	farmNum = ( (X - C)*F - 2*C >= 0 ) 
				? ceil( ((X - C)*F - 2*C) / (F*C) ) : 0;

	Rep(i, farmNum){
		ret += C / (F * i + 2);
	}
	ret += X / (F * farmNum + 2);

	return ret;
}

int main()
{
	ll T = 0;
	double C = 0, F = 0, X = 0;
	vector<double> ret;

	cin >> T;

	Rep(t, T){
		cin >> C >> F >> X;
		ret.push_back( solve(C, F, X) );
	}
	Rep(t, T){
		cout << "Case #" << t + 1 << ": ";
		printf("%.7f\n", ret[t]);
	}

	return 0;
}



