#include<cstdio>
#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
FILE *in = fopen("input5.in", "r");
FILE *out = fopen("output.out", "w");
int main(){
	int first[4][4], second[4][4], row1[4], row2[4];
	int i, j, T, test, one, two, magic, cnt = 0;
	fscanf(in, "%d", &T);
	test = T;
	while (T--){
		cnt = 0;
		fscanf(in, "%d", &one);
		for (j = 0; j < 4; j++){
			for (i = 0; i < 4; i++)
				fscanf(in, "%d", &first[j][i]);
		}
		for (j = 0; j < 4; j++)
			row1[j] = first[one - 1][j];
		fscanf(in, "%d", &two);
		for (j = 0; j < 4; j++){
			for (i = 0; i < 4; i++)
				fscanf(in, "%d", &second[j][i]);
		}
		for (j = 0; j < 4; j++)
			row2[j] = second[two - 1][j];
		for (i = 0; i < 4; i++){
			for (j = 0; j < 4; j++){
				if (row1[i] == row2[j]){
					magic = row1[i];
					cnt++;
				}
			}
		}
		fprintf(out, "Case #%d: ", test - T);
		if (cnt == 0) fprintf(out, "Volunteer cheated!\n");
		else if (cnt >= 2) fprintf(out, "Bad magician!\n");
		else fprintf(out, "%d\n", magic);
	}
	fcloseall();
	return 0;
}