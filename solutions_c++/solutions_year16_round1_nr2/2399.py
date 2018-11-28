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
#include <boost/range/adaptor/reversed.hpp>

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

bool check(UI v1, UI v2) { return v1 == 0 || v1 == v2; }

bool checkrow(vector<vector<UI>> &grid, vector<UI> &t, UI row)
{
	REP(i, t.size()) {
		if(!check(grid[row][i], t[i])) return false;
	}
	return true;
}

bool checkcol(vector<vector<UI>> &grid, vector<UI> &t, UI col)
{
	REP(i, t.size()) {
		if(!check(grid[i][col], t[i])) return false;
	}
	return true;
}

void out(ostream &os, vector<vector<UI>> &t) {
	os << "---" << endl;
	for(auto &v : t) {
		for(auto &vv: v) {
			os << ' ' << vv;
		}
		os << endl;
	}
	os << "---" << endl;
}

std::vector<UI> solve2(UI n, vector<vector<UI>> &grid, vector<vector<UI>> &table, vector<bool> &row, vector<bool> &col, vector<bool> &used)
{
	const UI N = row.size();
//cout << n << endl;
	if(n == 2*N-1) {
		vector<UI> result(N);
		REP(i, N) {
			if(!row[i]) {
				REP(j, N) {
					result[j] = grid[i][j];
				}
				return result;
			}
			if(!col[i]) {
				REP(j, N) {
					result[j] = grid[j][i];
				}
				return result;
			}
		}
		return vector<UI>();
	} else {
		REP(i, 2*N-1) {
			if(!used[i]) {
				// try row
				REP(j, N) {
					if(!row[j] && checkrow(grid, table[i], j)) {
						vector<vector<UI>> grid_(grid);
						REP(k, N) {
							grid_[j][k] = table[i][k];
						}
						used[i] = true;
						row[j] = true;
//cout << i << ' ' << used[i] << ' ' << "row:" << j << endl;
//out(cout, grid_);
						auto res = solve2(n+1, grid_, table, row, col, used);
						if(res.size()) return res;
						used[i] = false;
						row[j] = false;
					}
				}
				// try col
				REP(j, N) {
					if(!col[j] && checkcol(grid, table[i], j)) {
						vector<vector<UI>> grid_(grid);
						REP(k, N) {
							grid_[k][j] = table[i][k];
						}
						used[i] = true;
						col[j] = true;
//cout << i << ' ' << used[i] << ' ' << "col:" << j << endl;
//out(cout, grid);
						auto res = solve2(n+1, grid_, table, row, col, used);
						if(res.size()) return res;
						used[i] = false;
						col[j] = false;
					}
				}
				return vector<UI>();
			}
		}
	}
	return vector<UI>();
}

std::vector<UI> solve(UI n, vector<vector<UI>> &grid, vector<vector<UI>> &table, vector<bool> &row, vector<bool> &col, vector<bool> &used, UI maxnum)
{
	const UI N = row.size();
	UI ii = 0;
	REP(i, 2*N-1) {
		if(table[i][N-1] == maxnum) {
			ii = i; break;
		}
	}
	// try row
	if(check(grid[N-1][0], table[ii][0]) && check(grid[N-1][N-1], table[ii][N-1])) {
		vector<vector<UI>> grid_(grid);
		REP(i, N) {
			grid_[N-1][i] = table[ii][i];
		}
		used[ii] = true;
		row[N-1] = true;
//out(cout, grid_);
		auto res = solve2(n+1, grid_, table, row, col, used);
		if(res.size()) return res;
		used[ii] = false;
		row[N-1] = false;
	}
	// try col
	if(check(grid[0][N-1], table[ii][0]) && check(grid[N-1][N-1], table[ii][N-1])) {
		vector<vector<UI>> grid_(grid);
		REP(i, N) {
			grid_[i][N-1] = table[ii][i];
		}
		used[ii] = true;
		col[N-1] = true;
//out(cout, grid_);
		auto res = solve2(n+1, grid_, table, row, col, used);
		if(res.size()) return res;
		used[ii] = false;
		col[N-1] = false;
	}
	return vector<UI>();
}

int main(void)
{
	ios_base::sync_with_stdio(false);

	UI cases; cin >> cases;
	cin.ignore();
	REP(casenum, cases) {
		UI N; cin >> N;
		UI minnum = 2500, maxnum = 0;
		vector<vector<UI>> table(2*N-1, vector<UI>(N));
		for(auto &val1 : table) {
			for(auto &val2 : val1) {
				cin >> val2;
				maxnum = max(val2, maxnum);
				minnum = min(val2, minnum);
			}
		}
		vector<vector<UI>> grid(N, vector<UI>(N));
		vector<bool> row(N), col(N), used(2*N-1);
		UI n = 0;
		REP(i, 2*N-1) {
			if(table[i][0] == minnum) {
				REP(j, N) {
					grid[0][j] = table[i][j];
				}
				used[i] = true;
				row[0] = true;
				++n;
				break;
			}
		}
//out(cout, grid);
		REP(i, 2*N-1) {
			if(!used[i] && table[i][0] == minnum) {
				REP(j, N) {
					grid[j][0] = table[i][j];
				}
				used[i] = true;
				col[0] = true;
				++n;
				break;
			}
		}
//out(cout, grid);
		auto result = solve(n, grid, table, row, col, used, maxnum);
		cout << "Case #" << casenum+1 << ":";
		REP(i, N) {
			cout << ' ' << result[i];
		}
		cout << endl;
	}

	return 0;
}
