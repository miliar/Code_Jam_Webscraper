#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <complex>

using namespace std;

#define REP(a,b) for (int a=0; a<(int)(b); ++a)
#define FOR(a,b,c) for (int a=(b); a<(int)(c); ++a)

const double EPS = 1e-6;

int n;
double V, X;
double R[101], T[101];

int Vi, Xi;
int Ri[101], Ti[101];

void read_input() {
	cin >> n;
	cin >> V >> X;
	Vi = (int)(V * 10000 + .5);
	Xi = (int)(X * 10000 + .5);
	REP(i, n) {
		cin >> R[i] >> T[i];
		Ri[i] = (int)(R[i] * 10000 + .5);
		Ti[i] = (int)(T[i] * 10000 + .5);
	}
}


void solve() {
	if (n == 1) {
		if (Xi == Ti[0]) {
			printf("%.9lf\n", V / R[0]);
		}
		else
			puts("IMPOSSIBLE");
		return;
	}

	//double den = R[1] * (T[0] - T[1]);
	if (Ti[0] == Ti[1]) {
		if (Xi == Ti[0]) {
			printf("%.9lf\n", V / (R[0] + R[1]));
		}
		else
			puts("IMPOSSIBLE");
	}
	else {
		if (Xi < min(Ti[0], Ti[1]) || Xi > max(Ti[0], Ti[1])) {
			puts("IMPOSSIBLE");
			return;
		}
		//double t1 = (V*T[0] - X*V) / den;
		//double t2 = (V - R[1] * t1) / R[0];
		double t1 = V*(X - T[0]) / (R[1] * (T[1] - T[0]));
		double t2 = V*(X - T[1]) / (R[0] * (T[0] - T[1]));
		//if (t1 < -EPS || t2 < -EPS)
		//	puts("IMPOSSIBLE");
		//else
		printf("%.9lf\n", max(t1, t2));
	}
}


int main(int argc, char* argv[]) {
	int nt, single_tc = 0;

	if (argc > 1) {
		sscanf(argv[1], "%d", &single_tc);
	}

	scanf("%d", &nt);
	for (int t = 1; t <= nt; ++t) {
		read_input();
		if (single_tc == 0 || single_tc == t) {
			printf("Case #%d: ", t);
			solve();
		}
	}

	return 0;
}