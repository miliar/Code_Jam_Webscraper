// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdio.h"

int main(){

	int numeroCasos;
	double cookiesPS, custoFazenda, ganhoFazenda, limiteVitoria;
	double resultado;

	scanf("%d", &numeroCasos);
	for(int t = 0; t < numeroCasos; t++){

		cookiesPS = 2;
		resultado = 0;

		scanf("%lf %lf %lf", &custoFazenda, &ganhoFazenda, &limiteVitoria);

		while(true){
			if(limiteVitoria/cookiesPS < custoFazenda/cookiesPS + limiteVitoria/(cookiesPS + ganhoFazenda)){
				resultado += (limiteVitoria/cookiesPS);
				break;
			}
			else{
				resultado += (custoFazenda/cookiesPS);
				cookiesPS += ganhoFazenda;
			}
		}

		printf("Case #%d: %.7lf\n", t + 1, resultado);
	}
	
	return 0;
}

