#include <stdio.h>

main(){
	int T, caso;
	long double C, F, X, tempo, V=2, cookies=0;
	
	//v= quantidade de cookie por seg;
	//c= preço da farm;
	//f= quantidade de cookies extras por farm;
	//x= quantidade de cookies pra "ganhar";
	
	scanf("%d", &T);
	
	for(caso=1;caso<=T;caso++){
		V=2;
		scanf("%llf %llf %llf", &C, &F, &X);
					
				
		if(X/V <=  (C/V + X/(V+F))){  //NAO compensa comprar farm;
			tempo=X/V;
		}
		if(X/V >  (C/V + X/(V+F))){		
			tempo=0;
			cookies=0;
	

			while(cookies < X){

				if((X-cookies)/V <=  (C/V + (X-cookies)/(V+F)))  {  //se nao compensa mais comprar farm, adiciona o tempo pra "ganhar" e sai do laço;
					tempo+=(X-cookies)/V;
					cookies+=(X-cookies);
					//printf("1 tempo %llf\n", tempo);
					break;
				}

				else if(((X-cookies)/V >  (C/V + (X-cookies)/(V+F)))){ //compra uma farm!
					tempo+=C/V;
					V+=F;
					//printf("2 tempo %llf\n", tempo);
				}
				else
					printf("laço infinito feio\n");

			}
		}

		printf("Case #%d: %.7llf\n", caso, tempo);
	}
}
