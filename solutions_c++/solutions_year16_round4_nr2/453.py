#include <bits/stdc++.h>

using namespace std;

int N, K;

double memo[210][210];
double foo(vector<double> & P) {
	for(int a = 0; a <= K; ++a)
		for(int b = 0; b <= K; ++b)
			memo[a][b] = 0;
	memo[0][0] = 1;
	for(int n = 0; n < K; ++n) {
		for(int a = 0; a <= n + 1; ++a) {
			int b = (n + 1) - a;
			memo[a][b] = 0;
			if(a != 0)
				memo[a][b] += memo[a - 1][b] * P[n];
			if(b != 0)
				memo[a][b] += memo[a][b - 1] * (1 - P[n]);
		}
	}
	return memo[K / 2][K / 2];
}


void solve(int t) {
	cin >> N >> K;
	vector<double> P(N);
	for(int n = 0; n < N; ++n)
		cin >> P[n];
	double ans = 0;
	sort(P.begin(), P.end());
	for(int k = 0; k <= K; ++k) {
		vector<double> V;
		for(int i = 0; i < k; ++i)
			V.push_back(P[i]);
		for(int i = N - K + k; i < N; ++i)
			V.push_back(P[i]);
		ans = max(ans, foo(V));
	}
	printf("Case #%d: ", t);
	cout << fixed << setprecision(10) << ans << '\n';
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
		solve(t);
}
