#include <stdio.h>
int main(void){
int t,T;
double C,F,X;// C es costo de granja / F es el incremento de velocidad / X es la meta
double velocidadActual;
double tiempo,tmp1,tmp2;
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
scanf("%d",&T);
for(t=1;t<=T;t++){
	scanf("%lf %lf %lf",&C,&F,&X);
	velocidadActual=2;
	tiempo=0;
	while(true){
		tmp1=X/velocidadActual;
		tmp2=X/(velocidadActual+F)+C/velocidadActual;
		if(tmp1<tmp2){
			tiempo+=tmp1;
			break;
		}
		else{
			tiempo+=C/velocidadActual;
			velocidadActual+=F;
		}
		//printf("Tiempo: %f\n",tiempo);
	}
	printf("Case #%d: %.7lf\n",t,tiempo);
//	printf("%lf %lf %lf",C,F,X);
}
getchar();
getchar();
return 0;
}
