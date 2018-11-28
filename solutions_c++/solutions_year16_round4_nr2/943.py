#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 300;
int n, k;
long double d[MAXN], d2[MAXN], dyn[MAXN][MAXN];

long double compute_prob()
{
	dyn[0][0] = 1;
	dyn[1][0] = 0;
	for (int i = 1; i <= k; ++i) {
		dyn[0][i] = dyn[0][i - 1] * (1 - d2[i - 1]);
		for (int j = 1; j <= i; ++j) {
			dyn[j][i] = dyn[j - 1][i - 1] * d2[i - 1] + dyn[j][i - 1] * (1 - d2[i - 1]);
		}
		for (int j = i + 1; j <= k; ++j) {
			dyn[j][i] = 0;
		}
		long double sum = 0;
		for (int j = 0; j <= k; ++j) {
			sum += dyn[j][i];
		}
		for (int j = 0; j <= k; ++j) {
			dyn[j][i] /= sum;
		}
	}
	return dyn[k / 2][k];
}

void solve()
{
	cin >> n >> k;
	for (int i = 0; i < n; ++i) {
		cin >> d[i];
	}
	double best_prob = 0, prob;
	for (int msk = 0; msk < (1 << n); ++msk) {
		int cnt0 = 0;
		for (int i = 0; i < n; ++i) {
			if (msk & (1 << i)) {
				d2[cnt0++] = d[i];
			}
		}
		if (cnt0 != k) {
			continue;
		}
		prob = compute_prob();
		if (prob > best_prob) {
			best_prob = prob;
		}
	}
	cout << fixed << setprecision(10) << best_prob << endl;
}

int main()
{
	int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
}
