#include <stdio.h>

using namespace std;

int main(){

int T;
scanf("%d\n",&T);

int o = 0;

while(o++<T){

	double C, F, X, t, p1=0.0;
	scanf("%lf %lf %lf",&C, &F, &X);
	double n=1.0, tNovo;
	t = X / 2.0;
	
	while(true){
		p1+= (C / (2.0+(n-1.0)*F));
		tNovo = p1 + (X/ (2.0+n*F));
		n++;
		if(tNovo > t)
			break;
		else
			t = tNovo;
	}
	
//printf("%f", n);
		
	printf("Case #%d: %.7lf\n",o,t);
}

return 0;
}
