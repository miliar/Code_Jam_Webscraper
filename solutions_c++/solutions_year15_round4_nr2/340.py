#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
typedef long long LL;
typedef pair<int,int> PT;
const double EP=1e-9;

int TC, N;
double V, X, R[100], C[100];

int main() {
	scanf("%d", &TC);
	FOR(tc,1,TC+1) {
		scanf("%d%lf%lf", &N, &V, &X);
		FOR(n,0,N) scanf("%lf%lf", &R[n], &C[n]);
		printf("Case #%d: ", tc);
		if (N == 1) {
			if (fabs(C[0]-X) > EP) puts("IMPOSSIBLE"); else printf("%.10f\n", V/R[0]);
		} else if (N == 2) {
			if (fabs(C[0]-C[1]) < EP) {
				if (fabs(C[0]-X) > EP) puts("IMPOSSIBLE"); else printf("%.10f\n", V/(R[0]+R[1]));
			} else {
				double t2 = V*(X-C[0])/(R[1]*(C[1]-C[0]));
				double t1 = (V - R[1]*t2)/R[0];
				if (t1 + EP < 0.0 || t2 + EP < 0.0) puts("IMPOSSIBLE"); else printf("%.10f\n", fmax(t1, t2));
			}
		}
	}
}
