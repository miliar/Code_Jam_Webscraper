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


#include <iostream>

class Solution {
public:
    void solve(std::istream& in, std::ostream& out) {
		int T; in >> T;
		for (int test = 1; test <= T; ++test) {
			int N;
			double V, X;
			in >> N >> V >> X;
			vector<double> R(N), C(N);
			for (int i = 0; i < N; ++i)
				in >> R[i] >> C[i];
			auto deq = [&](double x, double y) {
				return x == y;
			};
			out << "Case #" << test << ": ";

			if (N == 1) {
				if (C[0] == X) {
					out << (V / R[0]) << "\n";
				} else {
					out << "IMPOSSIBLE\n";
				}
				continue;
			}

			if ((C[0] < X && C[1] < X) ||
				(C[0] > X && C[1] > X))
			{
				out << "IMPOSSIBLE\n";
			} else if (deq(C[0], C[1])) {
				if (deq(C[0], X)) {
					out << (V / (R[0] + R[1])) << "\n";
				} else {
					out << "IMPOSSIBLE\n";
				}
			} else {
				double t0 = (X - C[1]) / (C[0] - C[1]) * V / R[0];
				double t1 = (V - R[0] * t0) / R[1];
				if (t0 < -1e-7 || t1 < -1e-7) {
					out << "IMPOSSIBLE\n";
				} else {
					out << max(t0, t1) << "\n";
				}
			}
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
