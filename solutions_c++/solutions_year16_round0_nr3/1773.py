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
#include <ttmath/ttmath.h>
#undef max
#undef min

using namespace std;
using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)
#define FORi(i,n) for (int i = 0; i < (n); ++i)
//template<class C>
//void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }

long long pw[11][20];
bool pw_init()
{
	for (long long b = 2; b <= 10; ++b) {
		long long n = 1;
		for (int k = 0; k < 20; ++k) {
			pw[b][k] = n;
			n *= b;
		}
	}
	return true;
}
bool pw_inited = pw_init();

void solve_case(const unsigned int N, const unsigned int J, ostream&out)
{
	assert(N % 2 == 0);

	unsigned int k = N / 2;
	for (unsigned int j = 0; j < min(J,1u<<(k-2)); ++j) {
		unsigned long long jc = (1ULL << (k - 1)) + (j << 1) + 1;
		jc = (jc << k) + jc;

		UInt<10> x(jc);
		string s = x.ToString(2);
		out << s;
		for (unsigned int b = 2; b <= 10; ++b) {
			long long d = pw[b][k] + 1;
			out << ' ' << d;
			//check
			UInt<10> y; y.FromString(s, b);
			assert(y%d == 0);
			UInt<10> z = y / d;
			assert(y == z*d);
			//cout << x << " = " << d << " * " << z << endl;

		}
		out << '\n';
	}

	//cout << min(J, 1u << (k - 2)) << endl;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		unsigned int N, J;
		in >> N >> J; assert(N%2 == 0);

		out << "Case #" << t << ":" << endl;
		solve_case(N, J, out);
	}
}


int main()
{
	//ifstream in("C-sample.in");
	//ofstream out("C-sample-out.txt");

	//ifstream in("C-small-attempt0.in");
	//ofstream out("C-small-attempt0-out.txt");

	ifstream in("C-large.in");
	ofstream out("C-large-out.txt");

	solve(in,out);

	return 0;
}
