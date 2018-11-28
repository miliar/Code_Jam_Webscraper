#include <bits/stdc++.h>
using namespace std;

void solve(){
	int n, k;
	cin >> n >> k;
	vector<long double> p(n);
	for (int i = 0; i < n; i++) {
		cin >> p[i];
	}

	vector<int> masks;
	for (int mask = 0; mask < (1 << k); mask++) {
		int w = 0;
		for (int i = 0; i < k; i++) {
			w += (mask >> i) & 1;
		}
		if (w != k / 2) {
			continue;
		}
		masks.push_back(mask);
	}

	long double bestp = 0;

	for (int mask = 0; mask < (1 << n); mask++) {
		int w = 0;
		for (int i = 0; i < n; i++) {
			w += (mask >> i) & 1;
		}
		if (w != k) {
			continue;
		}
		vector<int> memb;
		for (int i = 0; i < n; i++) {
			if (mask & (1 << i)) {
				memb.push_back(i);
			}
		}
		long double sump = 0.0;
		for (int j = 0; j < masks.size(); j++) {
			int smask = masks[j];
			long double pp = 1.0;
			for (int i = 0; i < k; i++) {
				if (smask & (1 << i)) {
					pp *= p[memb[i]];
				}
				else {
					pp *= (1.0 - p[memb[i]]);
				}
			}
			sump += pp;
		}
		if (sump > bestp) {
			bestp = sump;
		}
	}
	printf("%0.8Lf", bestp);
}

int main(){
#ifdef HELTHAZAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		printf("Case #%d: ", t);
		// cout << "Case #" << t << ": ";
		solve();
		// cout << endl;
		printf("\n");
	}
}
