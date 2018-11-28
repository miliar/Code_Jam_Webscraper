#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

#define	For(i,a,b)				for(int i=(a);i<(b);++i)
#define	rep(i,n)				For(i,0,(n))

const double EPS = 1e-6;

string solve()
{
	try {
		int N;
		long double V, X;

		cin >> N >> V >> X;

		vector<long double> R(N), C(N);
		rep(i, N)
			cin >> R[i] >> C[i];

		long double res = 0;

		if(N == 1) {
			if(abs(X - C[0]) > EPS)
				throw -1;

			res = V / R[0];
		} else { // N == 2
			if(X < min(C[0], C[1]) - EPS || max(C[0], C[1]) + EPS < X)
				throw -1;

			if(abs(C[0] - C[1]) < EPS)
				res = V / (R[0] + R[1]);
			else
				res = max((C[1] - X) * V / (C[1] - C[0]) / R[0], (X - C[0]) * V / (C[1] - C[0]) / R[1]);
		}

		stringstream ss;
		ss << fixed << setprecision(10) << res;
		return ss.str();
	} catch(...) {
		return "IMPOSSIBLE";
	}
}

int main()
{
	int T;

	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}
