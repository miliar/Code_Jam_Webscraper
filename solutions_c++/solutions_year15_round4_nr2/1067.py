#include <iostream>
#include <vector>
#define forn(i, s, n) for (int i = (s); i < (n); i++)
#define sI(N) scanf("%d", &N)
using namespace std;

int getNum() {
	string s;
	cin >> s;
	//cout << s << endl;
	s.replace(s.find("."), 1, "");
	return atoi(s.c_str());
}

int main() {
	int T, t;
	sI(T);
	forn(t, 1, T + 1) {
		int N;
		sI(N);
		int V, X;
		int Vi;
		double r, c;
		V = getNum();
		X = getNum();
		//printf("%d %f %f %d %d\n", N, r, c, V, X);
		int R[N], C[N];
		for (int i = 0; i < N; i++) {
			R[i] = getNum();
			C[i] = getNum();
			//printf("%f %f\n", R[i], C[i]);
		}
		bool impossible = false;
		double ans;
		if (N == 1) {
			if (C[0] != X) {
				impossible = true;
			} else {
				ans = (double) V / R[0];
			}
		} else {
			int mnC = min(C[0], C[1]);
			int mxC = max(C[0], C[1]);
			//printf("%d %d %d\n", mnC, mxC, X);
			if (mnC > X || mxC < X) {
				impossible = true;
			} else {
				if (mxC == mnC) {
					ans = (double) V / (R[0] + R[1]);
				} else if (mxC == X) {
					//printf("here... %d %d %d %d %d %f\n", V, C[0], R[0], C[1], R[1], (double)V/R[1]);
					if (mxC == C[0]) {
						ans = (double) V / R[0];
					} else {
						ans = (double) V / R[1];
					}
				} else if (mnC == X) {
					//printf("here... %d %d %d %d %d %f\n", V, C[0], R[0], C[1], R[1], (double)V/R[1]);
					if (mnC == C[0]) {
						ans = (double) V / R[0];
					} else {
						ans = (double) V / R[1];
					}
				} else {
					long long int tmp = (long long int) V * (X - mnC);
					double v2 = (double) tmp / (mxC - mnC); 
					double v1 = V - v2;
					if (mnC == C[0]) {
						ans = max((double) v1 / R[0], (double) v2 / R[1]);
					} else {
						ans = max((double) v1 / R[1], (double) v2 / R[0]);
					}
				}
			}
		}
		if (impossible) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		} else {
			printf("Case #%d: %.9f\n", t, ans);
		}
	}
	return 0;
}