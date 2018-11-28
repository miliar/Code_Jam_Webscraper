#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <queue>
#include <cmath>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>
#undef max
#undef min

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)
#define FORi(i,n) for (int i = 0; i < (n); ++i)
//template<class C>
//void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }


const char * solve_case(const int N, const int R, const int C)
{
	// solved analyzing each case by hand
	assert(1 <= N && N <= 4);
	assert(1 <= R && R <= 4);
	assert(1 <= C && C <= 4);
	if (N == 1) return "GABRIEL"; // any grid can be covered by 1x1's
	if (N == 2) {
		if ( (R*C)%N != 0 ) return "RICHARD"; // odd cell count cannot be covered by 1x2
		else return "GABRIEL";
	}
	if (N == 3) {
		if (R == 1 || C == 1) return "RICHARD"; // for 1xC, Rx1 Richard chooses L shaped
		if ( (R*C)%N != 0 ) return "RICHARD"; // grid not multiple of N 
		assert(R == 3 || C ==3);
		return "GABRIEL"; // 2x3 grid can be covered with any of the 2 3-ominos, so Gabriel fills the rest with the 1x3
	}
	if (N == 4) {
		if ( (R*C)%N != 0 ) return "RICHARD"; // grid not multiple of N 
		if ( R == 2 && C == 2 ) return "RICHARD"; // choose L shaped
		assert(R == 4 || C == 4);
		if (R <= 2 || C <= 2) return "RICHARD"; // choose cross-minus-1-tooth shaped
		return "GABRIEL"; // 3x4 can be covered starting with any one
	}
	return "FAIL";
	return "GABRIEL";
	return "RICHARD";
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int N, R, C; //N es X
		in >> N >> R >> C; 

		const char * result = solve_case(N, R, C);
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//ifstream in("D-sample.in");
	//ofstream out("D-sample-out.txt");

	ifstream in("D-small-attempt0.in");
	ofstream out("D-small-out.txt");

	//ifstream in("D-large.in");
	//ofstream out("D-large-out.txt");

	solve(in,out);

	return 0;
}
