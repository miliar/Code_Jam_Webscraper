#include <cstdio>
#include <algorithm>

using namespace std;
double C,F,X;

double calc(int i){
	if(i<=0)i=0;
	double k=0;
	for(int j=0;j<=i;++j){
		k+=(double)1/((double)2+j*F);
	}


	return C*k+X/(2+(i+1)*F);
}

int main(){
	int T;
	scanf("%d",&T);

	for(int cnt=0;cnt<T;++cnt){


		scanf("%lf%lf%lf",&C,&F,&X);
		int i=X/C-2/F-2;
		
		double ans=min(min(calc(i),calc(i+1)),X/(double)2);

		printf("Case #%d: %.7lf\n",cnt+1,ans);

	}

	return 0;
}
