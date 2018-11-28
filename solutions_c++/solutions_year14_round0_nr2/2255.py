#include<algorithm>
#include<cassert>
#include<complex>
#include<map>
#include<iomanip>
#include<sstream>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define CLR(x) memset((x), 0, sizeof(x))
#define SQR(a) ((a)*(a))
#define DEBUG 1
typedef long long LL;
typedef long double LD;
//typedef pair<int, int> P;
//typedef vector<int> VI;
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FORE(it, (x)) cerr <<*it <<", "; cout <<endl; }}
using namespace std;
template<typename T> void mini(T&a4, T b4) {
	a4 = min(a4, b4);
}
template<typename T> void maxi(T&a4, T b4) {
	a4 = max(a4, b4);
}

void Cookie_Clicker_Alpha() {

	cout << setprecision(15) << fixed;

	double C, F, X;
	cin >> C >> F >> X;

	int N = ceil((F * X - 2 * C) / (C * F) - 1);

	double output;
	if (N > 0) {
		double reciprocal = 0.5;

		FOR(i,1,N)
			reciprocal += (double) 1 / (2 + i * F);

		output = C * reciprocal;

		output += (double) (X - C) / (2 + N * F);
	} else
		output = (double) X / 2;

	cout << output << endl;

}

