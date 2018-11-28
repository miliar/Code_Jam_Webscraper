#include <bits/stdc++.h>
using namespace std;

#define TRACE(x) cout << #x << " = " << x << endl

const double EPS = 1e-9;

const int MAXN = 5;

int N; // works only for N = 2
double V, X;

double R[MAXN];
double C[MAXN];


// intersection of x+y=V and C1x + C2y = X*V
double solve() {
	if (N == 1) {
		// solve x = V and C1x = X
		if (C[1] != X) return -1; // no solution
		return V / R[1];
	}
	
	// respective volumes
	//TRACE(X);
	//TRACE(C[2]);
	//TRACE(V);
	//TRACE(C[1]);
	// solve (C1-C2)x = XV - C2V
	if (C[1] == C[2]) {
		if (X != C[2])
			return -1;
		return V / (R[1] + R[2]);
	}
	
	if (X < C[2] && C[1] > C[2])
		return -1;
	if (X > C[2] && C[1] < C[2])
		return -1;
	
	if (abs(X - C[2]) > abs(C[1] - C[2]))
		return -1;
	
	double x = V * (X - C[2]) / (C[1] - C[2]);
	double y = V - x;
	
	//if (x < -EPS || y < -EPS)
	//	return -1; // no solution
		
	double t1 = x / R[1];
	double t2 = y / R[2];
	
	return max(t1, t2);
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> N >> V >> X;
		for (int i = 1; i <= N; i++) {
			//TRACE(i);
			cin >> R[i] >> C[i];
			//TRACE(R[i]);
			//TRACE(C[i]);
		}
		cout << "Case #" << icase << ": ";
		// solve line intersection
		double res = solve();
		if (res != -1)
			cout << fixed << setprecision(9) << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
