#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include <math.h>


typedef struct INPUT 
{
	char tmp[4];
	char map[4][4]; //input n	
} INPUT;

void main()
{
	int n, j, i,k, cnt;
	INPUT *p;
	char c[5];
	
	scanf("%d\n", &n);

	p = (INPUT*)malloc(sizeof(INPUT)*n*4);
	k = 0;
	for(i=0; i<n*4; i++)
	{
		scanf("%s", c);
		strcpy(p[i].tmp, c);
	}

	for(k=0; k<n; k++){
		for(i=4*k; i<4*k+4; i++){
		
			p[k].map[i%4][0] = p[i].tmp[0];
			p[k].map[i%4][1] = p[i].tmp[1];
			p[k].map[i%4][2] = p[i].tmp[2];
			p[k].map[i%4][3] = p[i].tmp[3];
		
		}
	}
	/*
	printf("=====================\n");
	
	for(k=0;k<n;k++){
		for(i=0; i<4; i++){	
			printf("%c%c%c%c\n", p[k].map[i][0],p[k].map[i][1],p[k].map[i][2],p[k].map[i][3]);			
		}
		printf("\n");
	}
	*/
	printf("=====================\n");
	bool found = false;
	bool found2 = false;
	bool found3 = false;
	char winner;
	char winner2;
	char winner3;
	int continuos = 0;
	int continuos2 = 0;
	int continuos3 = 0;
	bool dotExist = false;
	for(i=0; i<n; i++){
		printf("CASE #%d :", i+1);
		for(j=0;j<4;j++){
			if(continuos == 3){
				break;
			}
			if(continuos2 == 3){
				break;
			}
			for(k=0;k<3;k++){
				if((p[i].map[j][k] == p[i].map[j][k+1] || p[i].map[j][k+1] == 'T') && p[i].map[j][k] != '.'){					
					continuos++;
					winner = p[i].map[j][k];
				}else{
					continuos = 0;
				}
				if(p[i].map[j][k] == '.'){
					dotExist = true;
				}
			}

			for(k=0;k<3;k++){
				if((p[i].map[k][j] == p[i].map[k+1][j] || p[i].map[k][j] == 'T') && p[i].map[k][j] != '.'){					
					continuos2++;
					winner2 = p[i].map[k][j];
				}else{
					continuos2 = 0;
				}

				if(p[i].map[j][k] == '.'){
					dotExist = true;
				}
			}



			if(continuos == 3){
				printf(" %c WIN\n", winner);
				found = true;
				break;
			}
			if(continuos2 == 3){
				printf(" %c WIN\n", winner2);
				found2 = true;
				break;
			}
			
			
		}
		for(k =0;k<3;k++){
			if((p[i].map[k][k] == p[i].map[k+1][k+1] || p[i].map[k+1][k+1] == 'T') && p[i].map[k][k] != '.'){					
				continuos3 ++;
				winner3 = p[i].map[k][k];
			}else{
				continuos3 = 0;
			}
		}
		if(continuos3 == 3){
			printf(" %c WIN\n", winner3);
			found3 = true;
		}else{
			found3 = false;
		}
		continuos3 = 0;

		for(k =0;k<3;k++){
			if((p[i].map[k][3-k] == p[i].map[k+1][2-k] || p[i].map[k+1][2-k] == 'T') && p[i].map[k][3-k] != '.'){					
				continuos3 ++;
				winner3 = p[i].map[k][3-k];
			}else{
				continuos3 = 0;
			}
		}
		if(continuos3 == 3){
			printf(" %c WIN\n", winner3);
			found3 = true;
		}


		if(found == false && found2 == false && found3 == false && dotExist == false){
			printf("DRAW\n");			
		}else if(found == false && found2 == false && found3 == false && dotExist == true){
			printf("GAME IS NOT COMPLETE\n");			
		}

		continuos = 0;
		continuos2 = 0;
		continuos3 = 0;
		dotExist = false;
		found = false;
		found2 = false;
		found3 = false;
	}

}






