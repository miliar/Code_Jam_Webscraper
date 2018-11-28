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


const long long INSOMNIA = -1;
const long long TOOLONG = -2;

long long solve_case(const long long N)
{
	assert(N >= 0);
	if (N == 0) return INSOMNIA;

	bool seen[10] = {};
	int remain = 10;
	for (int i = 1; i < numeric_limits<long long>::max() / N; ++i)
	{
		long long k = i*N;
		while (k != 0) {
			int d = k % 10; k /= 10;
			if (!seen[d]) {
				seen[d] = true;
				--remain;
				if (remain == 0)
					return i*N;
			}
		}
	}
	return TOOLONG;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int N;
		in >> N;

		long long result = solve_case(N);
		if (result == INSOMNIA)
			out << "Case #" << t << ": INSOMNIA" << endl;
		else if (result == TOOLONG)
			out << "Case #" << t << ": TOOLONG" << endl;
		else
			out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//ifstream in("A-sample.in");
	//ofstream out("A-sample-out.txt");
	//ifstream in("A-sample2.in");
	//ofstream out("A-sample2-out.txt");

	//ifstream in("A-small-attempt0.in");
	//ofstream out("A-small-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out.txt");

	solve(in,out);

	return 0;
}
