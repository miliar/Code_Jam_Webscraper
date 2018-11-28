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
//typedef Int<100> num;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)
#define FORi(i,n) for (int i = 0; i < (n); ++i)
template<class C>
void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }

const long long IMPOSSIBLE = -1;
const char HAPPY = '+';
const char PLAIN = '-';

long long solve_case(string s, const int k)
{
	const size_t n = s.size();
	assert(2 <= k && k <= n);

	int flips = 0;
	for (size_t i = 0; i <= n-k; ++i) {
		if (s[i] == PLAIN) {
			++flips;
			for (size_t j = i; j < i + k; ++j) s[j] = (s[j] == PLAIN ? HAPPY : PLAIN);
		}
	}
	
	//validate remainder
	for (size_t i = n - k + 1; i < n; ++i)
		if (s[i] == PLAIN)
			return IMPOSSIBLE;

	return flips;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		string s;
		in >> s;
		int k;
		in >> k;

		long long result = solve_case(move(s), k);
		if (result == IMPOSSIBLE)
			out << "Case #" << t << ": IMPOSSIBLE" << endl;
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
