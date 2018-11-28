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
#include <ttmath/ttmath.h>

using namespace std;
using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)

inline long long reverse(long long n)
{
	assert(n >= 0);
	long long m = 0;
	while (n != 0) {
		int c = n % 10; n /= 10; m = m*10 + c;
	}
	return m;
}

inline long long pw10(int k)
{
	long long r = 1; while (k--) r *= 10; return r;
}
inline bool palin(long long n) { return reverse(n) == n; }

vector<long long> enumerate(int base_digits)
{
	vector<long long> result;
	for (int a = 0; a <= base_digits; ++a)
	{
		//int n = rand();
		//cout << n << '\t' << reverse(n) << endl;
		//cout << a << '\t' << pw10(a) << endl;
		long long b = pw10(a/2);
		long long bb = b*(a%2?10:1);
		for (long long u = bb/10; u < bb; ++u) {
			long long n = u*b + reverse(u)%b;
			//cout << n << endl;
			assert(palin(n));
			if (palin(n*n)) {
				//cout << n << '\t' << n*n << endl;
				result.push_back(n*n);
			}
		}
	}
	//for (long long n = 1; n < 1000000; n++) {
	//	//if (palin(n)) cout << n << ' ';
	//	if (palin(n) && palin(n*n)) 
	//		cout << n << '\t' << n*n << endl;
	//}
	return result;
}

int solve_case_small(long long A, long long B, const vector<long long> & fairsquares)
{
	assert(!fairsquares.empty() && 1 <= A && A <= B && B <= fairsquares.back());

	vector<long long>::const_iterator iA = lower_bound(fairsquares.begin(), fairsquares.end(), A);
	assert(iA == fairsquares.end() || (A <= *iA && (iA == fairsquares.begin() || *(iA-1) < A)));
	assert(iA != fairsquares.end());

	vector<long long>::const_iterator iB = upper_bound(fairsquares.begin(), fairsquares.end(), B);
	assert(iB == fairsquares.end() || (B < *iB && (iB == fairsquares.begin() || *(iB-1) <= B)));
	assert(iB != fairsquares.end());

	return distance(iA,iB);
}

void solve(istream & in, ostream & out)
{
	const vector<long long> fairsquares = enumerate(8);

	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		long long A, B;
		in >> A >> B;

		int result = solve_case_small(A,B,fairsquares);
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//ifstream in("C-sample.in");
	//ofstream out("C-sample-out.txt");

	//ifstream in("C-small-attempt0.in");
	//ofstream out("C-small-out.txt");

	ifstream in("C-large-1.in");
	ofstream out("C-large-1-out.txt");

	solve(in,out);

	return 0;
}
