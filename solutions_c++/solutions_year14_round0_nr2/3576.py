#include<cstdio>
#include<vector>

using namespace std;

int main(){
	int Q;
	scanf("%d", &Q);
	for (int q = 0; q<Q; ++q) {
		double c,f,x;
		scanf("%lf %lf %lf", &c, &f, &x);
		long double r = 2.0;
		long double suc = 0.0;
		while(1) {
			double t = c/r;
			double T = x/r;
			double tt = x/(r+f);
			if (t+tt < T) {
				r+=f;
				suc+=t;
			} else {
				suc+=T;
				break;
			}
		}
		printf("Case #%d: %0.8Lf\n", q+1, suc);
	}
	return 0;
}
