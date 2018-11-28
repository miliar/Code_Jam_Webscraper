#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>


using namespace std;

double getP(double pk[], int k) {
	double res = 0;
	for (int i = 0; i < 1 << k; i++) {
		if (__popcnt(i) == k / 2) {
			double t = 1;

			for (int j = 0; j < k; j++) {
				if ((1 << j) & i) {
					t *= pk[j];
				}
				else {
					t *= 1 - pk[j];
				}
			}

			res += t;
		}
	}
	return res;
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ti++) {
		int n, k;
		cin >> n >> k;
		double p[20];
		for (int i = 0; i < n; i++) {
			cin >> p[i];
		}
		double mp = 0;
		for (int i = 0; i < 1 << n; i++) {
			if (__popcnt(i) == k) {
				double pk[20];
				int cnt = 0;
				for (int j = 0; j < 16; j++) {
					if ((1 << j) & i) {
						pk[cnt++] = p[j];
					}
				}
				double pv = getP(pk, k);
				if (pv > mp)
					mp = pv;
			}
		}

		cout << "Case #" << ti << ": " << mp << endl;
	}
}