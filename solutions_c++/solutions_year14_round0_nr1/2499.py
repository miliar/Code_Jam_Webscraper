#include <stdio.h>

int main(){
	FILE *fi = fopen("A-small-attempt0.in", "r");
	FILE *fo = fopen("output.txt", "w");
	int T;
	
	fscanf(fi,"%d", &T);

	for (int k = 1; k <= T;k++){
		int card[17] = { 0, };
		int map[4][4] = { 0, };
		int n;
		fscanf(fi,"%d", &n);
		
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++)
				fscanf(fi,"%d", &map[i][j]);
		}

		for (int j = 0; j < 4; j++){
			card[map[n - 1][j]]++;
		}
		fscanf(fi,"%d", &n);

		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++)
				fscanf(fi,"%d", &map[i][j]);
		}
		for (int j = 0; j < 4; j++){
			card[map[n - 1][j]]++;
		}
		int two = 0;
		for (int i = 1; i <= 16; i++){
			if (two != 0 && card[i] == 2){
				fprintf(fo,"Case #%d: Bad magician!\n",k);
				two = 100;
				break;
			}
			if (card[i] == 2)
				two = i;
		}
		if (two == 0){
			fprintf(fo,"Case #%d: Volunteer cheated!\n", k);
		}
		else if (two != 100){
			fprintf(fo,"Case #%d: %d\n",k,two);
		}
	}

	return 0;
}