#include <stdio.h>
#include <stdlib.h>



void computa(long long int N, int instancia){
	
	if(N == 0) {
		printf("Case #%d: INSOMNIA\n",instancia);
	}
	else {
		long long int resultado = N;
		long long int ultimo;	
		int cont = 0;
		int i = 1;
		int dig[10] = {0,0,0,0,0,0,0,0,0,0};
		while(cont < 10){
			resultado = N* i;
			ultimo = resultado;
			while(ultimo != 0){
				if(dig[ultimo % 10] == 0){
					cont++;
					dig[ultimo % 10] = 1;
				}
				ultimo /= 10;
			}
			i++;
		}
		printf("Case #%d: %lld\n",instancia,resultado);
	}
}




int main(){
	int T;
	long long int N;
	while(scanf("%d",&T) != EOF) {
		for(int i=0;i<T;i++){
			scanf("%lld",&N);
			computa(N,i+1);	
		}
	
	}
}
