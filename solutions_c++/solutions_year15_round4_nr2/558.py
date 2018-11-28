//Author: net12k44
#include <bits/stdc++.h>
using namespace std;

const int limit = 100 + 5;
double r[limit];
double c[limit];
int n;
double V, X;
const double ep = 1e-9;
const char* cc = "IMPOSSIBLE";

bool equal(double x, double y){
	return fabs(x-y) < ep;
}

double special(){
	double dau = 0, cuoi = V/r[0];
	while (dau+ep < cuoi){
		double mid = (dau+cuoi)/2;
		if ( (r[0]+r[1])*mid < V ) dau = mid; else cuoi = mid;
	}
	return cuoi;
}

void solve(){
	scanf("%d %lf %lf",&n, &V, &X);
	for(int i = 0; i < n; ++i) scanf("%lf %lf",&r[i],&c[i]);

	if (n==1){
		if (!equal(c[0], X)) printf("%s\n", cc);
		else printf("%.9f\n", V/r[0]);
	} else if (n == 2){
		if (equal(c[0], c[1])) {
			if (equal(c[1], X))
				printf("%.9f\n", V/(r[0]+r[1]));
			else
				printf("%s\n", cc);
		} else {
			double d = r[0]*r[1]*c[1] - r[0]*c[0]*r[1];
			double dx = V*r[1]*c[1] - r[1]*V*X;
			double dy = r[0]*V*X - r[0]*c[0]*V;
			if (dx/d < -ep || dy/d < -ep)
				printf("%s\n",cc);
			else
				printf("%.9f\n", max(dx/d, dy/d));
		}
	}

}

int main(){
	int test; scanf("%d\n",&test);
	for(int t = 1; t <= test; ++t){
		printf("Case #%d: ",t);
		solve();
	}

}



