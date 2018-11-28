#include <cstdio>
#include <cmath>

using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		long double C,F,X;
		scanf("%Lf %Lf %Lf",&C,&F,&X);
		int n = ceil(X/C - 2/F - 1);
		if(n < 0) n=0;
		long double time=0;
		for(int j=0;j<n;j++){
			time += C/(2+j*F);
		}
		time += X/(2+n*F);
		printf("Case #%d: %.7Lf\n",i+1,time);
	}
	return 0;
}
