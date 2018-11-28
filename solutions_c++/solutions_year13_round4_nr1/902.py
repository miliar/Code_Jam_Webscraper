// gcc version 4.8.1 20130328 (prerelease) (GCC) at http://www.drangon.org/mingw/
// with -std=c++11

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
// 1.52 is used

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
#define REP(v, e) for(ULL v = 0ULL; v < e; ++v)
#define REP_(v, s, e) for(ULL v = s; v < e; ++v)
#define REPV(v, e) for(v = 0; v < e; ++v)
#define REPV_(v, s, e) for(v = s; v < e; ++v)

using namespace std;

template<class Integer>
inline boost::iterator_range< boost::range_detail::integer_iterator<Integer> >
IR(Integer first, Integer  last)
{ return boost::irange(first, last); }

int val(int N, int k)
{
	return k*N - (k * k - k) / 2;
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		ULL N, M; cin >> N >> M;
		vector<ULL> o(M),e(M),p(M);
		vector<ULL> on(N), en(N);
		ULL actual = 0;
		REP(i, M) {
			cin >> o[i] >> e[i] >> p[i];
			actual += val(N, e[i] - o[i]) * p[i];
			on[o[i]-1] += p[i];
			en[e[i]-1] += p[i];
		}
		ULL fake = 0;
		REP(i, N) {
			REP(j_, i + 1) {
				ULL j = i - j_;
				if(on[j] > 0 && en[i] > 0) {
					ULL num = min(on[j], en[i]);
					fake += val(N, j_) * num;
					on[j] -= num;
					en[i] -= num;
				}
			}
		}
		cout << "Case #" << casenum+1 << ": " << actual - fake << endl;
	}

	return 0;
}
