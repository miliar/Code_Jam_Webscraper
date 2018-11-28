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

const pair<UI,UI> guard = { numeric_limits<UI>::max(), numeric_limits<UI>::max() };

pair<UI,UI> scan(const vector<string> &table, UI R, UI C, UI r, UI c, char dir)
{
	switch(dir) {
	case '^':
		while(r>0) {
			--r;
			if(table[r][c] != '.') return { r, c };
		}
		break;
	case '<':
		while(c>0) {
			--c;
			if(table[r][c] != '.') return { r, c };
		}
		break;
	case '>':
		while(c<C-1) {
			++c;
			if(table[r][c] != '.') return { r, c };
		}
		break;
	case 'v':
		while(r<R-1) {
			++r;
			if(table[r][c] != '.') return { r, c };
		}
		break;
	}
	return guard;
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	REP(casenum, cases) {
		UI R, C; cin >> R >> C;
		UI result = 0;
		vector<string> table(R);
		for(auto i: IR(0U, R)) {
			cin >> table[i];
		}
		bool possible = true;
		for(auto i: IR(0U, R)) {
			for(auto j: IR(0U, C)) {
				if(table[i][j] != '.' && scan(table, R, C, i, j, table[i][j]) == guard) {
					++result;
					if(scan(table, R, C, i, j, '^') == guard &&
							scan(table, R, C, i, j, '<') == guard &&
							scan(table, R, C, i, j, '>') == guard &&
							scan(table, R, C, i, j, 'v') == guard) {
						possible = false;
					}
				}
			}
		}

		if(!possible) {
			cout << "Case #" << casenum+1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << casenum+1 << ": " << result << endl;
		}
	}

	return 0;
}
