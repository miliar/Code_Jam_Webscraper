#include <algorithm>
#include <complex>
#include <cstdlib>
#include <iomanip>
#include <istream>
#include <map>
#include <ostream>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
// Powered by caide (code generator, tester, and library code inliner)


class IntRange {
	int left, right;
public:
	IntRange(int left_, int right_);
	IntRange begin() const;
	IntRange end() const;
	int operator*() const;
	bool operator==(const IntRange& that) const;
	bool operator!=(const IntRange& that) const;
	IntRange& operator++();
};

IntRange range(int n);


template<typename C>
int SZ(const C& c) {
	return (int)c.size();
}


class Solution {
public:
    void solve(std::istream& in, std::ostream& out) {
		int T; in >> T;
		for (int test = 1; test <= T; ++test) {
			int R, C; in >> R >> C;
			vector<string> m(R);
			for (string& s : m)
				in >> s;
			int res = solve(m);
			out << "Case #" << test << ": ";
			if (res < 0)
				out << "IMPOSSIBLE\n";
			else
				out << res << "\n";
		}
    }

	int solve(const vector<string>& s) {
		const int m = SZ(s), n = SZ(s[0]);
		auto isValid = [&](int ci, int cj) {
			return ci >= 0 && ci < m && cj >= 0 && cj < n;
		};
		int res = 0;
		for (int i : range(m)) for (int j : range(n)) if (s[i][j] != '.') {
			int dx[] = { -1, 0, 1, 0 };
			int dy[] = { 0, 1, 0, -1 };
			char dirc[] = { '^', '>', 'v', '<' };
			set<int> okDirs;
			int curDir = -1;
			for (int dir = 0; dir < 4; ++dir) {
				int ci = i, cj = j;
				do {
					ci += dx[dir];
					cj += dy[dir];
				} while (isValid(ci, cj) && s[ci][cj] == '.');
				if (isValid(ci, cj))
					okDirs.insert(dir);
				if (dirc[dir] == s[i][j])
					curDir = dir;
			}
			if (okDirs.empty())
				return -1;
			if (!okDirs.count(curDir))
				++res;
		}
		return res;
	}
};

void solve(std::istream& in, std::ostream& out)
{
    out << std::setprecision(12);
    Solution solution;
    solution.solve(in, out);
}
#include <fstream>
#include <iostream>

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    istream& in = cin;

    ostream& out = cout;
    solve(in, out);
    return 0;
}


#include <functional>
#include <cstdarg>


IntRange range(int n) {
	return IntRange(0, n);
}


IntRange::IntRange(int left_, int right_)
	: left(min(left_, right_))
	, right(right_)
{}

IntRange IntRange::begin() const {
	return *this;
}

IntRange IntRange::end() const {
	return IntRange(right, right);
}

int IntRange::operator*() const {
	return left;
}

bool IntRange::operator==(const IntRange& that) const {
	return left == that.left;
}

bool IntRange::operator!=(const IntRange& that) const {
	return !operator==(that);
}


IntRange& IntRange::operator++() {
	++left;
	return *this;
}
