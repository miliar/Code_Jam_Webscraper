// Cygwin g++ 5.3.0 with -std=c++1z

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

template<typename F>
void bits(UI n, UI k, F f)
{
	ULL s = (1ULL << k) - 1ULL, e = ~((1ULL << n) - 1ULL);
	while(!(s&e)) {
		f(n, k, s);
		ULL st = s & -s;
		ULL rp = s + st;
		ULL ns = rp & -rp;
		s = rp | (((ns / st) >> 1) - 1);
	}
}

long double calc(vector<long double> &pick)
{
	UI k = pick.size();
	long double result = 0;
	bits(k, k/2, [&result, &pick](UI nn, UI kk, UI ss) {
		long double t = 1;
		REP(i, nn) {
			if(ss&(1<<i)) {
				t *= pick[i];
			} else {
				t *= (1-pick[i]);
			}
		}
		result += t;
	});
	return result;
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI N, K; cin >> N >> K;
		vector<long double> p(N);
		for(auto &val : p) { cin >> val; }
		long double result = 0;
		bits(N, K, [&result,&p](UI n, UI k, UI s) {
			vector<long double> pick;
			REP(i, n) {
				if(s&(1<<i)) pick.push_back(p[i]);
			}
//			cerr << "PICK: "; for(auto val: pick) { cerr << val << ','; } cerr << endl;
			auto temp = calc(pick);
			result = max(result, temp);
		});
		cout << "Case #" << casenum+1 << ": " << result << endl;
	}

	return 0;
}
