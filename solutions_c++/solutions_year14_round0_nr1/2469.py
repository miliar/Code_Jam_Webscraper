#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

#define INFILE fp_in
#define OUTFILE fp_out

FILE *fp_in, *fp_out;


void solve(int T){
	int table[5][5];
	int line;
	int arr[2][4];
	int same[10];
	int cnt = 0;

	fscanf(INFILE, "%d", &line);

	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			fscanf(INFILE, "%d", &table[i][j]);
		}
	}
	for (int i = 0; i < 4; i++){
		arr[0][i] = table[line - 1][i];
	}
	

	fscanf(INFILE, "%d", &line);

	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			fscanf(INFILE, "%d", &table[i][j]);
		}
	}
	for (int i = 0; i < 4; i++){
		arr[1][i] = table[line - 1][i];
	}

	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			if (arr[0][i] == arr[1][j]){
				same[cnt] = arr[0][i];
				cnt++;
			}
		}
	}

	if (cnt == 0){
		fprintf(OUTFILE, "Case #%d: Volunteer cheated!\n", T + 1);
	}
	else if (cnt == 1){
		fprintf(OUTFILE, "Case #%d: %d\n", T + 1, same[0]);
	}
	else{
		fprintf(OUTFILE, "Case #%d: Bad magician!\n", T + 1);
	}
}

int main(){
	

	int T, line;

	fp_in = fopen("A-small-attempt0.in","r");
	fp_out = fopen("A-small-attempt0.out", "w");
	fscanf(INFILE, "%d", &T);
	
	for (int i = 0; i < T; i++){
		solve(i);
	}

}