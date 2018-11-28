#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int readRow(FILE *fstream, int *rows) {
	fscanf(fstream, "%d %d %d %d", rows, rows+1, rows+2, rows+3);
	return 0;
}

int readMatrix(FILE *fstream, int *outRows, int outN) {
	int *rows = (int*)malloc(4*sizeof(int));
	for(int j=0; j<4; j++) {
		if(j+1 == outN) {
			readRow(fstream, outRows);
		} else {
			readRow(fstream, rows);
		}
	}
	free(rows);
	return 0;
}

int check(int *rows1, int *rows2) {
	int *map = (int*)malloc(16*sizeof(int));
	memset(map, 0, 16*sizeof(int));
	for(int i=0; i<4; i++) {
		map[rows1[i]-1]++;
	}
	for(int i=0; i<4; i++) {
		map[rows2[i]-1]++;
	}
	int result = 0;
	int idx = 0;
	for(int i=0; i<16; i++) {
		if(map[i] == 2) {
			result ++;
			idx = i;
		}
	}
	free(map);
	if(result == 1) {
		return idx+1;
	} else if(result > 1) {
		return -1;
	} else {
		return -2;
	}
}

int main() {
	FILE *fout = fopen("small1.out", "w");
	FILE *fstream = fopen("A--small-attempt3.in", "r");
	/*FILE *fstream = fopen("input00.txt", "r");*/
	int N;
	fscanf(fstream, "%d", &N);

	int *rows1 = (int*)malloc(4*sizeof(int));
	int *rows2 = (int*)malloc(4*sizeof(int));
	for(int i=0; i<N; i++) {
		int n1;
		fscanf(fstream, "%d", &n1);
		readMatrix(fstream, rows1, n1);
		int n2;
		fscanf(fstream, "%d", &n2);
		readMatrix(fstream, rows2, n2);
		int ret = check(rows1, rows2);
		if(ret > 0) {
			printf("Case #%d: %d\n", i+1, ret);
			fprintf(fout, "Case #%d: %d\n", i+1, ret);
		} else if(ret == -1) {
			printf("Case #%d: %s\n", i+1, "Bad magician!");
			fprintf(fout, "Case #%d: %s\n", i+1, "Bad magician!");
		} else if(ret == -2) {
			printf("Case #%d: %s\n", i+1, "Volunteer cheated!");
			fprintf(fout, "Case #%d: %s\n", i+1, "Volunteer cheated!");
		}
		else{
			printf("### error!\n");
			fprintf(fout, "### error!\n");
		}
	}
	free(rows1);
	free(rows2);
	fclose(fstream);
	fclose(fout);
	return 0;
}

