#include <stdio.h>

char num[10][6] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

int numLen[10] = { 4, 3, 3, 5, 4, 4, 3, 5, 5, 4 };
int flag[10];
int len = 0;
char str[2500];
char strFlag[2500];
char temp;

int DFS(int total){
	int i = 0, j = 0, k = 0;
	int lenflag = 0;
	char check[10] = {0};
	int count = 0;

	if (total != len){
		for (j = 0; j < 10;j++){
			count = 0;
			for (k = 0; num[j][k] != 0; k++){
				for (i = 0; str[i] != 0; i++){
					if (strFlag[i] != 1){
						if (num[j][k] == str[i]){
							check[count] = i;
							count++;
							break;
						}
					}
				}
			}
			if (count == numLen[j]){
				flag[j]++;
				for (i = 0; i < count; i++){
					strFlag[check[i]] = 1;
				}
				if (DFS(total + count)){
					return 1;
				}
				flag[j]--;
				for (i = 0; i < count; i++){
					strFlag[check[i]] = 0;
				}
			}
		}
	}
	else if(total == len) {
		return 1;
	}
	return 0;
}

int main(){
	FILE *Fin;
	FILE *Fout;
	int TestLoof = 0;
	int TestCount = 0;
	int i = 0, j = 0, k = 0;

	//Fin = fopen("input.txt", "r");
	Fin = fopen("A-small-attempt1.in", "r");
	Fout = fopen("output.txt", "w");

	fscanf(Fin, "%d", &TestCount);

	for (TestLoof = 1; TestLoof <= TestCount; TestLoof++){
		fscanf(Fin, "%c", &temp);
		fscanf(Fin, "%s", str);
		len = 0;
		for (i = 0; i < 10;i++){
			flag[i] = 0;
		}
		for (i = 0; str[i] != 0;i++){
			len++;
			strFlag[i] = 0;
		}
		DFS(0);
		fprintf(Fout, "Case #%d: ", TestLoof);
		for (i = 0; i < 10;i++){
			for (j = 1; j <= flag[i];j++){

				fprintf(Fout, "%d", i);
			}
		}
		fprintf(Fout, "\n");
	}
	fclose(Fout);
	fclose(Fin);

	return 0;
}

