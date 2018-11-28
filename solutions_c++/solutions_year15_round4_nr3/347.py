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


template<typename C>
int SZ(const C& c) {
	return (int)c.size();
}

#define ALL(c) (c).begin(), (c).end()


class Solution {
public:
    void solve(std::istream& in, std::ostream& out) {
		int T; in >> T;
		for (int test = 1; test <= T; ++test) {
			int N; in >> N;
			vector<vector<int> > sentences(N);
			map<string, int> wtoi;
			string line;
			getline(in, line);
			for (vector<int>& sent : sentences) {
				getline(in, line);
				istringstream instr(line);
				string s;
				while (instr >> s) {
					if (!wtoi.count(s)) {
						int n = SZ(wtoi);
						wtoi[s] = n;
					}
					sent.push_back(wtoi[s]);
				}
			}
			int res = SZ(wtoi);
			for (int mask = 0; mask < (1 << (N-2)); ++mask) {
				vector<int> isLang(wtoi.size());
				int mmask = 4 * mask + 2;
				for (int i = 0; i < N; ++i)
					for (int iw : sentences[i]) {
						if (mmask & (1 << i))
							isLang[iw] |= 2;
						else
							isLang[iw] |= 1;
					}
				res = min(res, count(ALL(isLang), 3));
			}

			out << "Case #" << test << ": " << res << "\n";
		}
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
