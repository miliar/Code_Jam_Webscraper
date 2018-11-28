#include <stdio.h>
#include <stdlib.h>

int main(void){
	int num, sum, done, unfinished;
	int j, k, q;
	char array[4][5]; //because %s will append a '/0' token as termination
	char tok[2] = {'X', 'O'};

	scanf("%d", &num);
	for (int i=0; i<num; i++){
		done = 0;
		for (j=0; j<4; j++)
			scanf("%s", array[j]);
		
		printf("Case #%d: ", i+1);

		for (q=0; q<2; q++){
			//horizontal
			for (j=0; j<4; j++){
				sum = 0;
				for(k=0; k<4; k++){		
					if((array[j][k] == tok[q]) || (array[j][k] == 'T')){
						sum+=1;		
					}
				}
				if (sum == 4){
					printf("%c won\n", tok[q]);
					done = 1;
					break;
				}
			}
			if(done == 1)
				break;
			
			//vertical
			for (j=0; j<4; j++){
				sum = 0;
				for(k=0; k<4; k++){
					if((array[k][j] == tok[q]) || (array[k][j] == 'T')){
						sum+=1;		
					}
				}
				if (sum == 4){	
					printf("%c won\n", tok[q]);
					done = 1;
					break;
				}
			}	
			if(done == 1)
				break;

			//diagonal - 1
			sum = 0;
			for(k=0; k<4; k++)
				if((array[k][k] == tok[q]) || (array[k][k] == 'T'))
					sum+=1;

			if (sum == 4){
				printf("%c won\n", tok[q]);
				done = 1;
				break;
			}

			//diagonal - 2
			sum = 0;
			for(k=0; k<4; k++)
				if((array[k][3-k] == tok[q]) || (array[k][3-k] == 'T'))
					sum+=1;

			if (sum == 4){	
				printf("%c won\n", tok[q]);
				done = 1;
				break;
			}

		}

		//check if unfinished
		unfinished = 0;
		for(k=0; k<4; k++)
			for(j=0; j<4; j++)
				if(array[k][j] == '.')
					unfinished = 1;

		if ((done != 1) && (unfinished == 1))
			printf("Game has not completed\n");

		if ((done != 1) && (unfinished == 0))
			printf("Draw\n");

	}


}
