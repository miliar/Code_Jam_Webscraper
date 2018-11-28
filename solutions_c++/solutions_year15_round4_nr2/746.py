#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; ++casenum) {
		int N;
		double V, X;
		cin >> N >> V >> X;
		double R[N], C[N];
		bool above = false;
		bool equal = false;
		bool bellow = false;
		forn(n, N) {
			cin >> R[n] >> C[n];
			if (C[n] > X) above = true;
			else if (C[n] < X) bellow = true;
			else equal = true;
		}
		bool possible = false;
		double t = 0.0;
		if (equal || (above && bellow)) {
			possible = true;
			if (N == 1) {
				t = V / R[0];
			//} else if (N == 2) {
			//	double V0 = (X * V - V * C[1]) / (C[0] - C[1]);
			//	double V1 = V - V0;
			//	t = max(V0 / R[0], V1 / R[1]);
			} else {
				double Na = 0.0, Nb = 0.0, Da = 0.0, Db = 0.0, Ne = 0.0, De = 0.0;
				forn(n, N) {
					if (C[n] > X) {
						Na += R[n] * C[n];
						Da += R[n];
					} else if (C[n] < X) {
						Nb += R[n] * C[n];
						Db += R[n];
					} else {
						Ne += R[n] * C[n];
						De += R[n];
					}
				}
				if (Da == 0.0 || Db == 0.0) {
					t = V / De;
				} else {
					// try equals above
					double Xa = (Na + Ne)/(Da + De);
					double Xb = Nb/Db;
					double Ra = Da + De;
					double Rb = Db;
					double Va = (X * V - V * Xb) / (Xa - Xb);
					double Vb = V - Va;
					t = max(Va / Ra, Vb / Rb);
					Xa = Na/Da;
					Xb = (Nb + Ne)/(Db + De);
					Ra = Da;
					Rb = Db + De;
					Va = (X * V - V * Xb) / (Xa - Xb);
					Vb = V - Va;
					double x = max(Va / Ra, Vb / Rb);
					t = min(x, t);
				}
			}
		}
		
		cout << "Case #" << casenum << ": ";
		if (possible) {
			printf("%0.9f", t);
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}

