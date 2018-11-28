#include<cstdio>

int main(){
	int q_casos, pick;
	int resto[4] = {0};
	scanf("%d", &q_casos);
	//printf("%d\n", q_casos);
	for(int i=0; i < q_casos; i++){
		int cartas[8] = {0};
		int hits = 0;
		int found = 0;
		//printf("Inicializou\n");
		//printf("%d\n",pick);
		for(int k = 0; k < 2; k++){
			scanf("%d", &pick);
			for(int j = 0; j < 4; j++){
				if(j == pick - 1){
					//printf("hitou\n");
					scanf("%d %d %d %d", &cartas[k*4], &cartas[k*4 + 1], &cartas[k*4 + 2], &cartas[k*4 + 3]);
				}
				else
					scanf("%d %d %d %d", &resto[0], &resto[1], &resto[2], &resto[3]);
				//printf("Leu cartas\n");
			}
			//printf("Leu matriz\n");
		}
		for(int k = 0; k < 4; k++){
			for(int j = 0; j < 4; j++){
				if(cartas[k] == cartas[4 + j]){
					hits++;
					//printf("%d %d %d\n", hits, cartas[k], cartas[4 + j]);
					found = cartas[k];
					//printf("Comparou\n");
				}
				//printf("Avançou\n");
			}
		}
		if(hits == 1)
			printf("Case #%d: %d\n",i+1, found);
		else if(hits == 0)
			printf("Case #%d: Volunteer cheated!\n",i+1);
		else
			printf("Case #%d: Bad magician!\n",i+1);			
	}
	return 0;
}
