#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>

void Input(int **pattern, int rows, int cols, FILE *f1){
	int temp;
	for(int row=0; row<rows; row++){
		for(int col=0; col<cols; col++){
			fscanf(f1, "%d", &temp);
			pattern[row][col] = temp;
		}
		fscanf(f1, "\n");
	}
	fscanf(f1,"\n");
}

void Output(int status, int case_num){
	FILE *f1;
	f1 = fopen("output.out", "a");
	switch(status){
	case 0: fprintf(f1, "Case #%d: YES\n",case_num+1);
			break;
	case 1: fprintf(f1, "Case #%d: NO\n",case_num+1);
			break;
	}
	fclose(f1);
}

int Status(int **pattern, int rows, int cols){
	int *high_row;
	int *high_col;
	high_row = new int[rows];
	high_col = new int[cols];
	int stat;
	for(int j=0; j<cols; j++){
		high_col[j] = 0;
	}
	for(int i=0; i<rows; i++){
		high_row[i] = 0;
		for(int j=0; j<cols; j++){
			if(pattern[i][j] > high_row[i]){
				high_row[i] = pattern[i][j];
			}
			if(pattern[i][j] > high_col[j]){
				high_col[j] = pattern[i][j];
			}
		}
	}
	stat = 0;
	for(int i=0; i<rows; i++){
		for(int j=0; j<cols; j++){
			if((pattern[i][j] < high_col[j])&&(pattern[i][j]< high_row[i])){
				stat = 1;
				i=rows;
				j=cols;
			}
		}
	}

	delete[] high_row;
	delete[] high_col;

	return stat;
}


int main(){
	int **pattern;
	pattern = new int*[100];
	for(int i=0; i<100; i++){
		pattern[i] = new int[100];
	}
	int num_cases;
	int st;
	int N, M;
	FILE *f1;


	f1 = fopen("B-large.in", "r");
	fscanf(f1, "%d\n", &num_cases);
	for(int i=0; i<num_cases; i++){
		fscanf(f1, "%d %d\n", &N, &M);
		Input(pattern, N, M, f1);
		Output(Status(pattern, N, M),i);
	}
	fclose(f1);


	for(int i=0; i<100; i++){
		delete[] pattern[i];
	}
	delete[] pattern;
	return 0;
}