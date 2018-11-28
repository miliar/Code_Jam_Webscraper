#include <algorithm>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <queue>
#include <set>
#include <vector>

using namespace std;

typedef long double ld;

#define EPS 1e-15

ld R[101];
ld C[101];

void solve()
{
	cout << fixed << setprecision(9);
	int N;
	ld V, X;
	cin >> N >> V >> X;
	for (int i=0; i<N; i++) {
		cin >> R[i] >> C[i];
	}
	if (N == 1) {
		if (X == C[0]) {
			cout << (V / R[0]);
		} else {
			cout << "IMPOSSIBLE";
		}
		return;
	}
	// N == 2
	if (C[0] + EPS < X && C[1] + EPS < X) {
		cout << "IMPOSSIBLE";
		return;
	} else if (C[0] - EPS > X && C[1] - EPS > X) {
		cout << "IMPOSSIBLE";
		return;
	}
	//V1 = V(X - C0) / (C1 - C0)
	if (fabs(C[0] - C[1]) < EPS) {
		if (fabs(C[0] - X) < EPS) {
			cout << V / (R[0] + R[1]);
		} else {
			cout << "IMPOSSIBLE";
		}
		return;
	}
	ld V0 = V * (X - C[1]) / (C[0] - C[1]);
	if (V0 + EPS < 0.0 || V0 - EPS > V) {
		cout << "IMPOSSIBLE";
		return;
	}
	ld T = V0 / R[0];
	T = max(T, (V - V0) / R[1]);
	cout << T;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	for (int tn=1; tn<=t; tn++) {
		cout << "Case #" << tn << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}