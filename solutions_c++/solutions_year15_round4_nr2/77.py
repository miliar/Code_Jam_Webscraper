#include <iostream>
#include <set>
#include <complex>
#include <cassert>
#include <vector>
#include <iomanip>

using namespace std;

const double eps = 1e-20;

int main() {
	cin.sync_with_stdio(false);
	
	int Te;
	cin >> Te;
	
	for(int T = 0; T < Te; ++T) {
		int N;
		double V, X;
		cin >> N >> V >> X;
		
		vector<pair<double, double>> a, b;
		double rate = 0.0;
		for(int i = 0; i < N; ++i) {
			double r, c;
			cin >> r >> c;
			if(c == X) {
				rate += r;
			} else if(c < X) {
				a.emplace_back(r, c);
			} else {
				b.emplace_back(r, c);
			}
		}
		
		while(!a.empty() && !b.empty()) {
			double& r1 = a.back().first;
			double& c1 = a.back().second;
			double& r2 = b.back().first;
			double& c2 = b.back().second;
			
			double d1 = X - c1;
			double d2 = c2 - X;
			assert(d1 > 0);
			assert(d2 > 0);
			
			if(d1 * r1 >= d2 * r2) {
				double R1 = r2 * d2 / d1;
				rate += R1 + r2;
				b.pop_back();
				r1 -= R1;
				if(r1 < 0) cerr << " ->> " << r1 << "\n";
				r1 = max(r1, 1e-40);
			} else {
				double R2 = r1 * d1 / d2;
				rate += R2 + r1;
				a.pop_back();
				r2 -= R2;
				if(r2 < 0) cerr << " ->> " << r2 << "\n";
				r2 = max(r2, 1e-40);
			}
		}
		
		if(rate == 0.0) {
			cout << "Case #" << T + 1 << ": IMPOSSIBLE\n";
		} else {
			cout << "Case #" << T + 1 << ": " << scientific << setw(10) << setprecision(10) << V / rate << '\n';
		}
	}
	
	return 0;
}
