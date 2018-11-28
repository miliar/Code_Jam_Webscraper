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
template<class C>
void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }

typedef vector< vector<char> > grid;
const int IMPOSSIBLE = -1;
const char BLANK = '.';
const char UP = '^';
const char RIGHT = '>';
const char DOWN = 'v';
const char LEFT = '<';

int solve_case(const grid & s, const int R, const int C)
{
	grid borderU(R, vector<char>(C,0));
	grid borderR(R, vector<char>(C,0));
	grid borderD(R, vector<char>(C,0));
	grid borderL(R, vector<char>(C,0));
	bool allBlank = true;
	FOR(i,R) {
		size_t j = 0;
		for (; j < C && s[i][j] == BLANK; ++j) {}
		if (j < C) { allBlank = false; }
		if (j < C) { ++borderL[i][j]; }
		j = C;
		for (; j > 0 && s[i][j-1] == BLANK; --j) {}
		if (j > 0) { ++borderR[i][j-1]; }
	}
	if (allBlank) return 0;
	FOR(j,C) {
		size_t i = 0;
		for (; i < R && s[i][j] == BLANK; ++i) {}
		if (i < R) { ++borderU[i][j]; }
		i = R;
		for (; i > 0 && s[i-1][j] == BLANK; --i) {}
		if (i > 0) { ++borderD[i-1][j]; }
	}
	int res = 0;
	FOR(i,R) FOR(j,C) { 
		if (borderU[i][j] &&
			borderR[i][j] &&
			borderD[i][j] &&
			borderL[i][j]) return IMPOSSIBLE;
		if (borderU[i][j] && s[i][j] == UP) ++res; 
		else if (borderR[i][j] && s[i][j] == RIGHT) ++res; 
		else if (borderD[i][j] && s[i][j] == DOWN) ++res; 
		else if (borderL[i][j] && s[i][j] == LEFT) ++res; 
	}
	return res;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int R, C;
		in >> R >> C;
		grid b(R, vector<char>(C));
		FOR(i,R) FOR(j,C) { in >> b[i][j]; }


		int result = solve_case(b, R, C);
		if (result < 0)
			out << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		else
			out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//ifstream in("A-sample.in");
	//ofstream out("A-sample-out.txt");

	//ifstream in("A-small-attempt0.in");
	//ofstream out("A-small-attempt0-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out.txt");

	solve(in,out);

	return 0;
}
