#include <stdio.h>
#include <iostream>

using namespace std;

main(){
	int ncases;
	double c,f,x;
	scanf("%d", &ncases);
	for ( int i=0 ; i < ncases; i++ ){
		scanf( "%lf %lf %lf", &c, &f, &x );
		//cout <<c <<" "<<f <<" "<< x <<endl;
		//printf("%lf %lf %lf\n",c, f, x);
		double construir, esperar, tiempo, pps;
		construir = esperar = tiempo = 0.0;
		pps = 2.0;
		for ( ;  ; ){
			construir = x/(pps+f)+c/pps;
			esperar = x / pps;
		//	printf("%lf %lf %lf\n",esperar,construir,tiempo);
			if(construir < esperar ){
				tiempo += c/pps;
				pps += f;
				
			} else{
				tiempo += esperar;
				break;
			}


		}

		printf("Case #%d: %.7lf\n",1+i,tiempo);
	} 
}