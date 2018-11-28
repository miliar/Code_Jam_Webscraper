#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

const double EPS = 1e-9;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int N;
		cin >> N;
		double V, X;
		double mx = 0;
		vector<double> Vs, Xs;
		cin >> V >> X;
		for(int i = 0; i < N; i++) {
			double v, x;
			cin >> v >> x;
			Vs.push_back(v);
			Xs.push_back(x);

			mx = max(mx, V / v);
		}
		//cout << mx << endl;

		bool possible = false;
		double time = mx + 10000;

		if(N==1) {
			if(fabs(X - Xs[0]) < EPS)
				possible = true;
			time = V / Vs[0];
		}
		else {
			double Va, Vb;
			if(fabs(Xs[0] - Xs[1]) < EPS) {
				if(fabs(Xs[0] - X) < EPS)
					possible = true;
				else
					possible = false;
				time = V / (Vs[0] + Vs[1]);
			}
			else {
				possible = true;
				Va = ((X - Xs[1]) * V) / (Xs[0] - Xs[1]);
				Vb = V - Va;
				if(Va < -EPS || Vb < -EPS) {
					possible = false;
				}

//				cout << Va << " " << Vb << endl;
				time = max(Va / Vs[0], Vb / Vs[1]);
			}
		}

		if(possible)
			printf("Case #%d: %.10f\n", t+1, time);
		else
			printf("Case #%d: IMPOSSIBLE\n", t+1);
	}
}
