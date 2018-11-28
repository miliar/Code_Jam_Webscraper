#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int nc; cin >> nc;
	for (int cs = 1; cs <= nc; cs++) {
		int n, k; cin >> n >> k;
		double p[n];
		for (int i = 0; i < n; i++) cin >> p[i];

		double bestProb = 0;
		for (int combo = 0; combo < (1 << n); combo++) {
			if (__builtin_popcount(combo) != k) continue;
			double prob = 0;
			double p2[k];
			int xx = 0;
			for (int i = 0; i < n; i++) {
				if ((combo & (1 << i)) > 0) {
					p2[xx] = p[i];
					xx++;
				}
			}

			for (int z = 0; z < (1 << k); z++) {
				if (__builtin_popcount(z) != k/2) continue;
				double prob2 = 1;
				for (int i = 0; i < k; i++) {
					if ((z & (1 << i)) == 0) {
						prob2 *= 1.0 - p2[i];
					} else {
						prob2 *= p2[i];
					}
				}
				prob += prob2;
			}
			if (prob > bestProb) {
				bestProb = prob;
			}
		}

		cout << "Case #" << cs << ": " << setprecision(16) << fixed << bestProb << endl;
	}
}
