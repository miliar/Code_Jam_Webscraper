// Cygwin clang++ 3.4.2 with -std=c++1y

#include <iostream>
#include <sstream>
#include <iomanip>

#include <iterator>

#include <algorithm>
#include <numeric>
#include <utility>
#include <limits>

#include <string>

#include <vector>
#include <deque>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>

#include <tuple>
#include <initializer_list>

#include <cmath>

// Boost library can be retrieved from http://www.boost.org/
// 1.55 is used

#pragma GCC diagnostic ignored "-Wconversion"
#include <boost/range/irange.hpp>
#include <boost/range/iterator_range.hpp>
#pragma GCC diagnostic warning "-Wconversion"

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned short US;
typedef unsigned char UC;

#define RNG(v) (v).begin(), (v).end()
#define REP(v, e) for(UI v = 0U; v < e; ++v)
#define REP_(v, s, e) for(UI v = s; v < e; ++v)
#define REPV(v, e) for(v = 0; v < e; ++v)
#define REPV_(v, s, e) for(v = s; v < e; ++v)

using namespace std;

template<class Integer>
inline boost::iterator_range< boost::range_detail::integer_iterator<Integer> >
IR(Integer first, Integer  last)
{ return boost::irange(first, last); }

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI N; double V, X; cin >> N >> V >> X;
		double result = 0; bool possible = false;
		if(N == 1) {
			double R0, C0; cin >> R0 >> C0;
			if(abs(X - C0) <= 10e-6) {
				possible = true;
				result = V / R0;
			}
		} else { // N == 2;
			double R0, C0; cin >> R0 >> C0;
			double R1, C1; cin >> R1 >> C1;
			if(C0 > C1) { swap(R0, R1); swap(C0, C1); }
			if(C0 == C1 && X == C0) {
				possible = true;
				result = V/(R0+R1);
			} else if(X == C0) {
				possible = true;
				result = V/R0;
			} else if(X == C1) {
				possible = true;
				result = V/R1;
			} else if(C0< X && X < C1) {
				possible = true;
				double p0 = (C1-X)/(C1-C0);
				result = max(V*p0/R0, V*(1-p0)/R1);
			}
		}
		if(possible) {
			cout << "Case #" << casenum+1 << ": " << setprecision(20) << result << endl;
		} else {
			cout << "Case #" << casenum+1 << ": " << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
