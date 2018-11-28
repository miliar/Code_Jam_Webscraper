// gcc version 4.8.2 with -std=c++11

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
// 1.53 is used

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
inline auto
IR(Integer first, Integer  last) -> decltype(boost::irange(first, last))
{ return boost::irange(first, last); }

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		int N; cin >> N;
		vector<char> chars; char pc = ' ';
		vector<vector<int>> data(N);
		{
			string s; cin >> s;
			for(auto &c : s) {
				if(pc != c) {
					chars.push_back(c);
					data[0].push_back(1);
					pc = c;
				} else { ++(data[0].back()); }
			}
		}
//cout << "check"; for(auto & c : data[0]) { cout << ':' << c; } cout << endl;
//cout << "check"; for(auto & c : chars) { cout << ':' << c; } cout << endl;
		bool invalid = false;
		for(auto i : IR(1, N)) {
			string s; cin >> s;
			int idx = 0;
			for(auto &c : s) {
				if(data[i].size() == 0) {
					if(chars[0] != c) { invalid = true; break; }
					data[i].push_back(1);
				} else if(chars[idx] != c) {
					++idx;
					if(idx >= chars.size() || chars[idx] != c) {
						invalid = true; break;
					}
					data[i].push_back(1);
				} else {
					++(data[i].back());
				}
			}
			if(idx != chars.size() - 1) { invalid = true; }
		}
		if(invalid) {
			cout << "Case #" << casenum+1 << ": " << "Fegla Won" << endl;
		} else {
			int result = 0;
			for(auto i : IR<size_t>(0, chars.size())) {
				int min_ = 101, max_ = 0;
				for(auto j : IR(0, N)) {
					min_ = min(min_, data[j][i]);
					max_ = max(max_, data[j][i]);
				}
				int tresult = 101;
				for(auto j : IR(min_, max_ + 1)) {
					int temp = 0;
					for(auto k : IR(0, N)) {
						temp += abs(j - data[k][i]);
					}
					tresult = min(tresult, temp);
				}
				result += tresult;
			}
			cout << "Case #" << casenum+1 << ": " << result << endl;
		}
	}

	return 0;
}
