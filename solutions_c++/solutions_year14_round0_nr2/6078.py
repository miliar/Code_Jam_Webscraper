#include<cstdio>
#include<algorithm>
using namespace std;

int main(){

	int runs;
	scanf("%d",&runs);
	for( int r = 1; r <= runs; r++){	
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		double v = 2.0, ans = 0, res = X/v;
		for( int i = 0; i  < (int)(X/C); i++){
			double t = C / v;
			ans += t;
			res = min( res , ans + X/v );
			v += F;
			res = min( res , ans + X/v );
		}
		printf("Case #%d: %.7lf\n", r, res);
	}

	return 0;
}
