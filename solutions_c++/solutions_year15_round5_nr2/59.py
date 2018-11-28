#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

typedef long long int64;

int main() {
	int nT;
	cin >> nT;
	for (int nc = 1; nc <= nT; ++nc) {
		int n, k;
		cin >> n >> k;
		vector<int> sum(n - k + 1);
		for (int i = 0; i < n - k + 1; ++i) {
			cin >> sum[i];
		}
		//x0,x2,...,xk-1
		//sum x_i = sum[0]
		vector<int> who(n);
		vector<int> by(n);
		for (int i = 0; i < k; ++i) {
			who[i] = i;
			by[i] = 0;
		}
		for (int i = k; i < n; ++i) {
			who[i] = who[i - k];
			by[i] = by[i - k] + sum[i - k + 1] - sum[i - k];
		}
		vector<int> mi(k, 0), mx(k, 0);
		for (int i = 0; i < n; ++i) {
			mi[who[i]] = min(mi[who[i]], by[i]);
			mx[who[i]] = max(mx[who[i]], by[i]);
		}
		//sum x0,...,xk-1 = sum[0]

		int64 L = -1, R = 1 << 28;
		while (L + 1 < R) {
			int64 M = (L + R) >> 1;
			//[a,a+M]
			//ka
			int64 aL = 0, aR = 0;

			bool ok = true;

			for (int i = 0; i < k; ++i) {
				aL += -mi[i];
				aR += -mx[i] + M;
				if (-mi[i] > -mx[i] + M) {
					ok = false;
					break;
				}
			}
			if (!ok) {
				L = M;
				continue;
			}
			//we want sum[0] in [ka+aL,ka+aR]
			int64 S = sum[0] - aL;
			aR -= aL;
			//[ka,ka+aR] sum[0] in
			//ka<=S
			int64 r = S / k + 2;
			while (r * k > S)
				--r;
			//S<=ka+aR ka>=S-aR
			int64 l = (S - aR) / k - 2;
			while (l * k < S - aR)
				++l;
			if (l <= r) {
				R = M;
			} else {
				L = M;
			}
		}
		printf("Case #%d: %d\n", nc, (int) R);
	}
	return 0;
}
