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


long long solve_case(string s)
{
	long long p = 0, n = 0;
	for (size_t i = 0; i < s.size(); ++i) {
		if (s[i] == '+') {
			//p = p
			n = p + 1;
		} else {
			p = n + 1;
			//n = n;
		}
	}
	return p;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		//cout << "Case #" << t << endl;
		string s;
		in >> s; assert(1 <= s.size() && s.size() <= 100);
		//cout << ' ' << s << endl;

		long long result = solve_case(move(s));
		//cout << '\t' << result << endl;
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//ifstream in("B-sample.in");
	//ofstream out("B-sample-out.txt");

	//ifstream in("B-small-attempt0.in");
	//ofstream out("B-small-attempt0-out.txt");

	ifstream in("B-large.in");
	ofstream out("B-large-out.txt");

	solve(in,out);

	return 0;
}
