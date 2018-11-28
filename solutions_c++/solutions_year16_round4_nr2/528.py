#include <iostream>
#include <algorithm>

using namespace std;

int T, N, K;
double ans;
double a[222], b[222], f[222][222];

double calc() {
	for (int i = 0; i <= K; ++i) {
		for (int j = 0; j <= K; ++j) {
			f[i][j] = 0;
		}
	}
	f[0][0] = 1;
	for (int i = 0; i < K; ++i) {
		for (int j = 0; j<= i; ++j) {
			f[i + 1][j] += f[i][j] * b[i];
			f[i + 1][j + 1] += f[i][j] * (1 - b[i]);
		}
	}
	return f[K][K / 2];
}

int main() {
	cin >> T;
	for (int _ = 1; _ <= T; ++_) {
		cin >> N >> K;
		for (int i = 1; i <= N; ++i) {
			cin >> a[i];
		}
		ans = 0.;
		sort(a + 1, a + N + 1);
		for (int i = 0; i <= K; ++i) {
			int tot = 0;
			for (int j = 1; j <= i; ++j) {
				b[tot++] = a[j];
			}
			for (int j = N - (K - i) + 1; j <= N; ++j) {
				b[tot++] = a[j];
			}
			ans = max(ans, calc());
		}
		cout << "Case #" << _  << ": " << (ans) << endl;
	}
	return 0;
}
