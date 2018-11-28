#include <stdio.h>
#include <stdlib.h>

int cmpfunc (const void * a, const void * b)
{
	if (*(double*)a > *(double*)b)
		return 1;
	if (*(double*)a == *(double*)b)
		return 0;
	if (*(double*)a < *(double*)b)
		return -1;
}


main(){
	int T, N, casos, i, firstN, firstK, lastN, lastK, pts1, pts2;
	double Na[2000], Ken[2000];
	scanf("%d", &T);
	
	for(casos=1;casos<=T;casos++){

		scanf("%d", &N); //quantidade de madeirinha

		for(i=0;i<N;i++)
			scanf("%lf", &Na[i]);
		for(i=0;i<N;i++)
			scanf("%lf", &Ken[i]);			

			
		qsort(Na, N, sizeof(double), cmpfunc);	
		qsort(Ken, N, sizeof(double), cmpfunc);

/*
		for(i=0;i<N;i++)
			printf("%.2f ", Na[i]);
		printf("\n");
		
		for(i=0;i<N;i++)
			printf("%.2f ", Ken[i]);			
		printf("\n");
*/
		
		//leu os pesos das madeiras dos dois e ordenou;	
			
		pts1=0;
		pts2=0;	
		firstN=0;
		firstK=0; 
		lastN=N-1; 
		lastK=N-1;
		
		//melhor estrategia pra WAR:

		for(i=0;i<N;i++){
			if(Na[firstN] > Ken[firstK]){
				lastN--;
				firstK++;
				pts1++;
			}
			else{
				firstN++;
				firstK++;
			}
		}
		
		
		firstN=0;
		firstK=0; 
		lastN=N-1; 
		lastK=N-1;
		//melhor estrategia pra Deceitful WAR:

		for(i=0;i<N;i++){
			if(Na[firstN] > Ken[firstK]){
				firstN++;
				firstK++;
				pts2++;	
			}
			else{
				firstN++;
				lastK--;
			}
		}
		
		printf("Case #%d: %d %d\n", casos, pts2, pts1);		
	}
}
