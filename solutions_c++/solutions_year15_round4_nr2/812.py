#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

void Solve() {
	int n;
	double V;
	double T;
	scanf("%d%lf%lf", &n, &V, &T);
	double t[128];
	double s[128];
	for (int i=0; i<n; i++) {
		scanf("%lf%lf", s+i, t+i);
	}
	bool found = false;
	double bestT = 1e100;
	double s1 = 0.0;
	for (int i=0; i<n; i++) {
		if (fabs(t[i] - T) < 1e-5) {
			found = true;
			s1 += s[i];
		}
	}
	if (found) {
		double t = V / s1;
		bestT = min(bestT, t);
	}
	for (int i=0; i<n; i++) {
		if (fabs(t[i] - T) > 1e-5) {
			for (int j=i+1; j<n; j++) {
				if (fabs(t[j] - T) > 1e-5 && fabs(t[i] - t[j]) > 1e-5) {
					double vi = V * (T - t[j]) / (t[i] - t[j]);
					if (vi > 1e-8 && vi < V - 1e-8) {
						double vj = V - vi;
						double ti = vi / s[i];
						double tj = vj / s[j];
						bestT = min(bestT, max(ti, tj));
						found = true;
					}
				}
			}
		}
	}	
	if (found) {
		printf("%.12lf\n", bestT);
	} else {
		printf("IMPOSSIBLE\n");
	}
}

int main() {
	int nt;
	scanf("%d", &nt);
	for (int i=1; i<=nt; i++) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
