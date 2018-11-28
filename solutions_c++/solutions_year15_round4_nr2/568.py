#include <bits/stdc++.h>

using namespace std;

int T, N;
double V, X;
double R[2], C[2];

double solveSingle(double r, double c) {
	if (fabs(c - X) > 1e-9) {
		return -1.0;
	}
	double t = V / r;
	return t;
}

double combine(double r0, double c0, double r1, double c1) {
	if (c0 < X - 1e-9 && c1 < X - 1e-9) {
		return -1.0;
	}
	if (c0 > X + 1e-9 && c1 > X + 1e-9) {
		return -1.0;
	}
	
	long double v0 = (long double) V * (X - c1) / (c0 - c1);
	long double v1 = V - v0;
	long double t0 = v0 / r0;
	long double t1 = v1 / r1;
	long double ret = max(t0, t1);
	return ret;
}

double solveDouble() {
	double ans = -1.0;
	double s1 = solveSingle(R[0], C[0]);
	double s2 = solveSingle(R[1], C[1]);
	if (ans < -1e-8 || s1 < ans) {
		ans = s1;
	}
	if (ans < -1e-8 || s2 < ans) {
		ans = s2;
	}
	
	if (fabs(C[0] - C[1]) < 1e-8) {
		double s = solveSingle(R[0] + R[1], C[0]);
		if (ans < -1e-8 || s < ans) {
			ans = s;
		}
		return ans;
	}
	double s3 = combine(R[0], C[0], R[1], C[1]);
	if (ans < -1e-8 || s3 < ans) {
		ans = s3;
	}
	
	double s4 = combine(R[1], C[1], R[0], C[0]);
	if (ans < -1e-8 || s4 < ans) {
		ans = s4;
	}
	
	return ans;
}

int main() {
	freopen("date.in", "r", stdin);
	freopen("date.out","w", stdout);
	cin.sync_with_stdio(false);
	
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N >> V >> X;
		for (int i = 0; i < N; i++) {
			cin >> R[i] >> C[i];
		}
		double ans = -1.0;
		if (N == 1) {
			ans = solveSingle(R[0], C[0]);
		} else {
			ans = solveDouble();
		}
		cout << "Case #" << t << ": ";
		if (ans < -1e-8) {
			cout << "IMPOSSIBLE\n";
		} else {		
			cout << fixed << setprecision(10) << ans << '\n';
		}
		
		cerr << "Test " << t << '\n';
	}
	
	return 0;
}
