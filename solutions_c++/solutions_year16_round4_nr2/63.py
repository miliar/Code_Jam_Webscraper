#include <algorithm>
#include <iostream>
#include <iomanip>

using namespace std;

int n, k;
double p[202];
double X[202][202];

int main() {
//	cin.sync_with_stdio(false);
//	cin.tie(nullptr);
	
	int tc;
	cin >> tc;
	for(int ti = 1; ti <= tc; ++ti) {
		cin >> n >> k;
		vector<double> asd(n);
		for(int i = 0; i < n; ++i) {
			cin >> asd[i];
		}
		sort(asd.begin(), asd.end());
		double best = 0.0;
		for(int spl = 0; spl <= k; ++spl) {
			for(int i = 0; i < spl; ++i) {
				p[i] = asd[i];
			}
			for(int i = spl; i < k; ++i) {
				p[i] = asd[asd.size() - 1 - (i - spl)];
			}
			X[0][0] = 1.0;
			for(int i = 1; i <= k; ++i) {
				for(int j = 0; j <= i; ++j) {
					X[i][j] = 0.0;
					if(j) X[i][j] += p[i - 1] * X[i - 1][j - 1];
					if(j < i) X[i][j] += (1 - p[i - 1]) * X[i - 1][j];
				}
			}
			best = max(best, X[k][k / 2]);
		}
		
		cout << "Case #" << ti << ": " << setprecision(16) << fixed << best << '\n';
	}
	
	return 0;
}
