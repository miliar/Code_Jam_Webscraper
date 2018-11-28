#include <bits/stdc++.h>

using namespace std;

template<class T> inline bool _min(T& data, const T& comp) {
	if (comp < data) {
		data = comp;
		return true;
	}
	return false;
}

template<class T> inline bool _max(T& data, const T& comp) {
	if (data < comp) {
		data = comp;
		return true;
	}
	return false;
}

long double pos[256][256];

long double choice[256];
long double f[256];

long N, K;

long double calc(long d) {
	for (long i = 0; i < d; ++ i) {
		f[i] = choice[i];
	}
	for (long i = 0; i < K - d; ++ i) {
		f[i + d] = choice[N - i - 1];
	}
	memset(pos, 0, sizeof pos);
	pos[0][0] = 1 - f[0];
	pos[0][1] = f[0];
	for (long i = 1; i < K; ++ i) {
		pos[i][0] = pos[i - 1][0] * (1 - f[i]);
		pos[i][i + 1] = pos[i - 1][i] * f[i];
		for (long j = 1; j <= i; ++ j) {
			pos[i][j] = pos[i - 1][j] * (1 - f[i]) + pos[i - 1][j - 1] * f[i];
		}
	}
	return pos[K - 1][K >> 1];
}

int main(void) {
	ios::sync_with_stdio(false);

	long T;
	cin >> T;

	for (long t = 1; t <= T; ++ t) {
		cin >> N >> K;
		memset(f, 0, sizeof f);
		memset(choice, 0, sizeof choice);
		for (long i = 0; i < N; ++ i) {
			cin >> choice[i];
		}
		sort(choice, choice + N);
		long double ans = 0.L;
		for (long i = 0; i <= K; ++ i) {
			_max(ans, calc(i));
		}
		cout.setf(ios::fixed);
		cout.precision(12);
		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}
