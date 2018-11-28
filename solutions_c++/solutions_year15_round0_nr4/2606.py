#include <stdio.h>

int main(){
	FILE * ent;
	FILE * saida;
	ent = fopen("entrada4.txt", "r");
	saida = fopen("saida4.txt", "w");
	int T, indl;
	int X, R, C;
	fscanf(ent, "%d", &T);
	for(indl=0; indl<T; indl++){
		fscanf(ent, "%d %d %d", &X, &R, &C);
		if(X==1) fprintf(saida, "Case #%d: GABRIEL\n", indl+1);
		if(X==2){
			if(R%2 && C%2) fprintf(saida, "Case #%d: RICHARD\n", indl+1);
			else fprintf(saida, "Case #%d: GABRIEL\n", indl+1);
		}
		if(X==3){
			if(R==1 || C==1) fprintf(saida, "Case #%d: RICHARD\n", indl+1);
			else if(R%3==0 || C%3==0) fprintf(saida, "Case #%d: GABRIEL\n", indl+1);
			else fprintf(saida, "Case #%d: RICHARD\n", indl+1);
		}
		if(X==4){
			if(R<=2 || C<=2) fprintf(saida, "Case #%d: RICHARD\n", indl+1);
			else if(R==3 && C==3) fprintf(saida, "Case #%d: RICHARD\n", indl+1);
			else fprintf(saida, "Case #%d: GABRIEL\n", indl+1);
		}
	}
	fclose(ent);
	fclose(saida);

}