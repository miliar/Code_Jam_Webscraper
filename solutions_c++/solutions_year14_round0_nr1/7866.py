#include <stdio.h>
#include <stdlib.h>
int mat[4][4];
int sec[4][4];

int main(){
	FILE * ent;
	FILE * saida;
	ent = fopen("Magic.txt", "r");
	saida = fopen ("saida1.txt", "w");

	int T;
	fscanf(ent,"%d", &T);
	int n, i, j, cont;
	int firstrow, secrow;
	bool cheated, stupid;
	int nsol;
	int answer;
	for(cont=0; cont<T; cont++){
		fscanf(ent, "%d", &firstrow);
		for(i=0; i<4; i++){
			for(j=0; j<4; j++)
				fscanf(ent, "%d", &mat[i][j]);
		}
		fscanf(ent, "%d", &secrow);
		for(i=0; i<4; i++){
			for(j=0; j<4; j++)
				fscanf(ent, "%d", &sec[i][j]);
		}
		nsol = 0;
		cheated= true;
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				if(mat[firstrow-1][i]==sec[secrow-1][j]){
					nsol++;
					cheated=false;
					answer = mat[firstrow-1][i];
				}
			}
		}
		if(nsol>1) stupid = true;
		else stupid = false;
		fprintf(saida, "Case #%d: ", cont+1);
		if(cheated) fprintf(saida, "Volunteer cheated!\n");
		else if(stupid) fprintf(saida, "Bad magician!\n");
		else fprintf(saida, "%d\n",answer);
	}
	system("pause");
}