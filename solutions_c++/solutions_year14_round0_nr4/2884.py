#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T, n;
	double tmp;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%d", &n);
		vector<double> naomi, ken;
		for (int j = 0; j < n; ++j) {
			scanf("%lf", &tmp);
			naomi.push_back(tmp);
		}
		for (int j = 0; j < n; ++j) {
			scanf("%lf", &tmp);
			ken.push_back(tmp);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		int dw = n, delta = 0, w = n;
		for (int j = 0; j < n; ++j) {
			if (naomi[j] < ken[j-delta]) {
				--dw;
				++delta;
			}
		}
		for (int j = 0, k = 0; j < n && k < n; ++j, ++k) {
			if (naomi[j] < ken[k]) {
				--w;
			} else {
				while (k < n && naomi[j] > ken[k]) {
					++k;
				}
				if (k != n) {
					--w;
				}
			}
		}

		printf("Case #%d: %d %d\n", i, dw, w);
	}
	return 0;
}