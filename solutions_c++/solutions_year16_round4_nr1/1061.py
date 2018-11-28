// Cygwin clang++ 3.7.1 with -std=c++1z

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
// 1.58 is used

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
		UI N,R,P,S; cin >> N >> R >> P >> S;
		string candidate[3] = { "P", "R", "S" };
		string result;
		REP(j, 3) {
			REP(i, N) {
				string t;
				t = candidate[j];
				candidate[j] = "";
				for(char c: t) {
					switch(c) {
					case 'P':
						candidate[j] += "RS";
						break;
					case 'R':
						candidate[j] += "PS";
						break;
					case 'S':
						candidate[j] += "PR";
						break;
					}
				}
			}
			UI d = 1, num = (1 << N) / 2;
			string::iterator bb = candidate[j].begin();
			REP(i, N) {
				REP(j, num) {
					string::iterator b1 = bb+d*2*j, e1 = bb+d*2*j+d, b2 = bb+d*2*j+d, e2 = bb+d*2*j+2*d;
					if(!lexicographical_compare(b1, e1, b2, e2)) {
						swap_ranges(b1,e1,b2);
					}
				}
				d *= 2; num /= 2;
			}
			UI pp = 0, rr = 0, ss = 0;
			for(char c: candidate[j]) {
				switch(c) {
				case 'P':
					++pp;
					break;
				case 'R':
					++rr;
					break;
				case 'S':
					++ss;
					break;
				}
			}
//cerr << candidate[j] << endl;
			if(pp == P && rr == R && ss == S) { result = candidate[j]; }
		}
		if(result.size()) {
			cout << "Case #" << casenum+1 << ": " << result << endl;
		} else {
			cout << "Case #" << casenum+1 << ": " << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
