#include <cstdio>
#include <iostream>
using namespace std;

const double eps = 1e-8;
double sgn(double x) {
	if( x < -eps )
		return -1;
	return x > eps;
}

double V,Xt;
int ics = 0;
void SolveOne(double v,double r) {
	if( sgn(Xt-r) != 0 )
		printf("Case #%d: IMPOSSIBLE\n",++ics);
	else
		printf("Case #%d: %.9lf\n",++ics,V/v);
}

int main() {
	int T;
	scanf("%d",&T);
	while(T--) {
		int n;
		scanf("%d%lf%lf",&n,&V,&Xt);
		
		if( n == 1 ) {
			double v,r;
			scanf("%lf%lf",&v,&r);
			SolveOne(v,r);
		}
		else {
			double v1,r1,v2,r2;
			scanf("%lf%lf%lf%lf",&v1,&r1,&v2,&r2);
			if( sgn(r2-r1) == 0 )
				SolveOne(v1+v2,r1);
			else {
				if( sgn(Xt-r1) == 0 ) {
					SolveOne(v1,r1);
				}
				else if( sgn(Xt-r2) == 0) {
					SolveOne(v2,r2);
				}
				else {
					double rate = (Xt - r1) / (r2 - Xt);
					if( sgn(rate) < 0 )
						printf("Case #%d: IMPOSSIBLE\n",++ics);
					else {
						double va = V / ( 1 + rate );
						double vb = V * rate / ( 1 + rate );
						double t = max(va/v1,vb/v2);
						printf("Case #%d: %.9lf\n",++ics,t);
					}
				}
			}
		}
	}
	return 0;
}