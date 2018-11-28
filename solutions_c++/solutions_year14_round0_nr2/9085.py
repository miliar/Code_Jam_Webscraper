#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
double X,c,f;
const double eps = 1e-10;


int main(){
	int T;
	scanf("%d\n",&T);
	for(int p=1;p<=T;p++){
		scanf("%lf %lf %lf\n",&c,&f,&X);
		
//		double res = backtrack(2.0,0.0);
		double fn = X/2.0;
		double newfn;
		for(int n=1;n<10e8;++n){
//				printf("%.4f\n",fn);
			newfn = fn + X/(2.0 + n*f) + c/(2.0 + (n-1)*f) - X/(2.0+(n-1)*f);
			if(newfn > fn)
				break;
			fn = newfn;
		}
		
		printf("Case #%d: %.7f\n",p,fn);
	}
	return 0;
}
