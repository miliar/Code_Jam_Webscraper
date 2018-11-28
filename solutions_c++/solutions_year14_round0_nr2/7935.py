#include <cstdio>
#include <algorithm>

using namespace std;

void resoud(){
	double C,F,X;
	scanf("%lf%lf%lf",&C,&F,&X);
	double tempsMin=X/2.,prod=2,temps=0;
	for (int i=1;;i++){
		temps+=C/prod;
		prod+=F;
		double t=temps+X/prod;
		if (tempsMin<t)
			break;
		tempsMin=t;
	}
	printf("%.12f\n",tempsMin);
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		printf("Case #%d: ",i);
		resoud();
	}
	return 0;
}
