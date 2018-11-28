#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;
#define NN 110

typedef long long ll;
int N, NP, NM, NZ;
double V, X;
double R[NN], RP[NN], RM[NN], RZ[NN];
double C[NN], CP[NN], CM[NN], CZ[NN];
double cmt, rmt;
double cpt, rpt;
double czt, rzt;

int main() {
	int t;
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%d%lf%lf", &N, &V, &X);
		NP = NM = NZ = 0;
		cmt = 0; rmt = 0;
		cpt = 0; rpt = 0;
		czt = 0; rzt = 0;
		for (int i = 0; i < N; ++i) {
			scanf("%lf%lf", &R[i], &C[i]);
			C[i] -= X;
			if (C[i] < 0) {
				cmt = (cmt*rmt+C[i]*R[i])/(rmt + R[i]);
				rmt += R[i];
				RM[NM] = R[i];
				CM[NM] = C[i];
				NM++;
			} else if (C[i] > 0) {
				cpt = (cpt*rpt+C[i]*R[i])/(rpt + R[i]);
				rpt += R[i];
				RP[NP] = R[i];
				CP[NP] = C[i];
				NP++;
			} else {
				rzt += R[i];
				RZ[NZ] = R[i];
				NZ++;
			}
		}
		if (NZ == 0 && (NM == 0 || NP == 0)) {
			printf("Case #%d: IMPOSSIBLE\n", ti+1);
			continue;
		}
		if (NM == 0 || NP == 0) {
			double ans = V/rzt;
			printf("Case #%d: %20.12lf\n", ti+1, ans);
			continue;
		}
		if (NP == 1 && NM == 1) {
			double ans = max(V*cmt/(cmt-cpt)/rpt, V*cpt/(cpt-cmt)/rmt);
			printf("Case #%d: %20.12lf\n", ti+1, ans);
			continue;
		}
		printf("Case #%d: UNSUPPORTED\n", ti+1);
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
