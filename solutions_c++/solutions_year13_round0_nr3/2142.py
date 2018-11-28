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
#define REP(v, e) for(UI v = 0U; v < e; ++v)
#define REP_(v, s, e) for(UI v = s; v < e; ++v)
#define REPV(v, e) for(v = 0; v < e; ++v)
#define REPV_(v, s, e) for(v = s; v < e; ++v)

using namespace std;

template<class Integer>
inline boost::iterator_range< boost::range_detail::integer_iterator<Integer> >
IR(Integer first, Integer  last)
{ return boost::irange(first, last); }

vector<string> fair = { "1", "4", "9", "121", "484" };

struct numeric_less
{
	bool operator()(const string &s1, const string &s2) const {
		return s1.size() < s2.size() ||
			(s1.size() == s2.size() && s1 < s2);
	}
};

void mygenerate(int len, const vector<pair<int,int>> &indices)
{
	bool valid = true;
	vector<int> v(len);
	for(auto &val : indices) {
		v[val.first * 2] += val.second * val.second;
		if(v[val.first * 2] > 9) { valid = false; break; }
	}
	REP(i, indices.size()) {
		for(auto j : IR<UI>(i+1, indices.size())) {
			v[indices[i].first+indices[j].first] += 2 * indices[i].second * indices[j].second;
			if(v[indices[i].first+indices[j].first] > 9) { valid = false; break; }
		}
		if(!valid) break;
	}
	if(valid) {
		string s;
		for(auto &val : v) {
			s.push_back(val+'0');
		}
		fair.push_back(s);
	}
}

void init_fair(size_t max_len)
{
	const UI N = (max_len + 1) / 2 + 1;
	REP(i_, N) {
		int i = i_ + 1; // 1 -> (max_len + 1) / 2
		if(i < 3) continue;
		if(i & 1) { // odd
			// 1xx0xx1 x can have 1 at most 6 positions
			//   1.0.1
			//   1.1.0.1.1
			//   1.1.1.0.1.1.1
			//   1.1.1.1.0.1.1.1.1
			// 1xx1xx1 x can have 1 at most 6 positions
			//   1.1.1
			//   1.1.1.1.1
			//   1.1.1.1.1.1.1
			//   1.1.1.1.1.1.1.1.1
			// 1xx2xx1 x can have 1 at most 2 positions
			//   1.2.1
			//   1.1.2.1.1
			// 2.2
			// 2.1.2

			const int X = (i - 1) / 2;
			// 2.2
			mygenerate(2*i-1, { {0,2}, {2*X,2} });
			// 1.0.1
			mygenerate(2*i-1, { {0,1}, {X,0}, {2*X,1} });
			// 1.1.1
			mygenerate(2*i-1, { {0,1}, {X,1}, {2*X,1} });
			// 1.2.1
			mygenerate(2*i-1, { {0,1}, {X,2}, {2*X,1} });
			// 2.1.2
			mygenerate(2*i-1, { {0,2}, {X,1}, {2*X,2} });

			for(auto ii : IR(1, X)) {
			// 1.1.0.1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {X,0}, {2*X-ii,1}, {2*X,1} });
			// 1.1.1.1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {X,1}, {2*X-ii,1}, {2*X,1} });
			// 1.1.2.1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {X,2}, {2*X-ii,1}, {2*X,1} });
			}

			for(auto ii : IR(1, X)) {
				for(auto jj : IR(ii+1, X)) {
			// 1.1.1.0.1.1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {jj,1}, {X,0}, {2*X-jj,1}, {2*X-ii,1}, {2*X,1} });
			// 1.1.1.1.1.1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {jj,1}, {X,1}, {2*X-jj,1}, {2*X-ii,1}, {2*X,1} });
				}
			}

			for(auto ii : IR(1, X)) {
				for(auto jj : IR(ii+1, X)) {
					for(auto kk : IR(jj+1, X)) {
			// 1.1.1.1.0.1.1.1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {jj,1}, {kk,1}, {X,0}, {2*X-kk,1}, {2*X-jj,1}, {2*X-ii,1}, {2*X,1} });
			// 1.1.1.1.1.1.1.1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {jj,1}, {kk,1}, {X,1}, {2*X-kk,1}, {2*X-jj,1}, {2*X-ii,1}, {2*X,1} });
					}
				}
			}

		} else { // even
			const int X = i  / 2;

			// 1xxxx1 x can have 1 at most 6 positions
			//   1..1
			//   1.1..1.1
			//   1.1.1..1.1.1
			//   1.1.1.1..1.1.1.1
			// 2.2

			// 1..1
			mygenerate(2*i-1, { {0,1}, {2*X-1,1} });
			// 2.2
			mygenerate(2*i-1, { {0,2}, {2*X-1,2} });

			for(auto ii : IR(1, X)) {
			// 1.1..1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {2*X-ii-1,1}, {2*X-1,1} });
			}

			for(auto ii : IR(1, X)) {
				for(auto jj : IR(ii+1, X)) {
			// 1.1.1..1.1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {jj,1}, {2*X-jj-1,1}, {2*X-ii-1,1}, {2*X-1,1} });
				}
			}

			for(auto ii : IR(1, X)) {
				for(auto jj : IR(ii+1, X)) {
					for(auto kk : IR(jj+1, X)) {
			// 1.1.1.1..1.1.1.1
				mygenerate(2*i-1, { {0,1}, {ii,1}, {jj,1}, {kk,1}, {2*X-kk-1,1}, {2*X-jj-1,1}, {2*X-ii-1,1}, {2*X-1,1} });
					}
				}
			}

		}
	}
#if 0
	sort(RNG(fair), numeric_less());
	for(auto & val : fair) {
		cout << val << endl;
	}
#endif
}

UI solve(const pair<string, string> &iv)
{
	auto it1 = lower_bound(RNG(fair), iv.first, numeric_less());
	auto it2 = lower_bound(RNG(fair), iv.second, numeric_less());
	UI result = it2 - it1;
	if(it2 != fair.end() && *it2 == iv.second) ++result;
	return result;
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	size_t max_len = 0;
	vector<pair<string,string>> iv(cases);
	for(auto & val : iv) {
		cin >> val.first >> val.second;
		max_len = max({max_len, val.first.size(), val.second.size()});
	}
	init_fair(max_len);
	for(auto & val : iv) {
		cout << "Case #" << &val - iv.data() + 1 << ": " << solve(val) << endl;
	}

	return 0;
}
