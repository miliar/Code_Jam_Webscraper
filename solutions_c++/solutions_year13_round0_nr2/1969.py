#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)

typedef vector<int> Row;
typedef vector< Row > Board;


const string YES = "YES";
const string NO = "NO";

string solve_case(const Board & b, const int N, const int M)
{
	vector<int> rowmax(N,0);
	vector<int> colmax(M,0);
	for (int i = 0; i < N; ++i)
	for (int j = 0; j < M; ++j) {
		if (rowmax[i] < b[i][j]) rowmax[i] = b[i][j];
		if (colmax[j] < b[i][j]) colmax[j] = b[i][j];
	}
	for (int i = 0; i < N; ++i)
	for (int j = 0; j < M; ++j) {
		if (b[i][j] < rowmax[i] && b[i][j] < colmax[j]) return NO;
	}

	return YES;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int N, M;
		in >> N >> M;
		Board b(N, Row(M,-1));
		for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			in >> b[i][j];

		string result = solve_case(b, N, M);
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//ifstream in("B-sample.in");
	//ofstream out("B-sample-out.txt");

	//ifstream in("B-small-attempt0.in");
	//ofstream out("B-small-out.txt");

	ifstream in("B-large.in");
	ofstream out("B-large-out.txt");

	solve(in,out);

	return 0;
}
