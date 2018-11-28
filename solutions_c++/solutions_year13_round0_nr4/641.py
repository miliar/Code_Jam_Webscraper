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
#include <boost/dynamic_bitset.hpp>
using boost::dynamic_bitset;

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

deque<int> solve(const vector<int> &required, const vector<vector<int>> &got, set<dynamic_bitset<>> &visited, dynamic_bitset<>& open, vector<int> & keys)
{
	if(visited.count(open)) return {};
	if(open.count() == required.size()) return { -1 };
//cerr << "OPENED_COUNT: " << open.count() << endl;
	REP(i, required.size()) {
		if(!open[i] && keys[required[i]] > 0) {
//cerr << "OPEN: " << i << endl;
			open.set(i);
			--keys[required[i]];
			REP(j, got[i].size()) {
				++keys[got[i][j]];
			}
			auto t = solve(required, got, visited, open, keys);
			if(t.size()) {
				if(t.back() == -1) {
					t.back() = i+1;
				} else t.push_front(i+1);
				return t;
			}
			REP(j, got[i].size()) {
				--keys[got[i][j]];
			}
			++keys[required[i]];
			open.reset(i);
		}
	}
	visited.insert(open);
	return {};
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI K, N; cin >> K >> N;
		vector<int> keys(200);
		REP(i, K) { UI t; cin >> t; ++keys[t-1]; }
		vector<int> required(N);
		vector<vector<int>> got;
		REP(i, N) {
			cin >> required[i]; --required[i];
			UI t; cin >> t;
			vector<int> got_(t);
			for(auto &val : got_) {
				cin >> val; --val;
			}
			got.push_back(got_);
		}

		dynamic_bitset<> open(N);
		set<dynamic_bitset<>> visited;
		cout << "Case #" << casenum+1 << ":";
		auto result = solve(required, got, visited, open, keys);
		if(result.size()) {
			for(auto &val: result) {
				cout << ' ' << val;
			}
		} else {
			cout << " IMPOSSIBLE";
		}
		cout << endl;
	}

	return 0;
}
