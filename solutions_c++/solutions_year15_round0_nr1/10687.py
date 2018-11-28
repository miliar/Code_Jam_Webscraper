#include <stdio.h>
#include <stdlib.h>

int main(){
	int n, sMax, friends, atual, temp;
	char *vet, a;

	FILE *file = fopen("A-small-attempt5.in", "r");
	FILE *out = fopen("out", "w");

	fscanf(file, "%d", &n);

	for (int i = 0; i < n; i++){
		fscanf(file, "%d ", &sMax);

		vet = (char*) malloc(sizeof(char) * sMax+1);
		fscanf(file, "%s", vet);

		friends = 0;

		a = vet[0];
		temp = atoi(&a);

		for (int j = 1; j < sMax+1; j++){
			a     = vet[j];
			atual = atoi(&a);
			
			if (atual != 0 && temp >= j){
				temp += atual;
			}else if (atual != 0){
				friends += j - temp;
				temp += friends + atual;
			}
		}
		fprintf(out, "Case #%d: %d\n", i+1, friends);
	}

	fclose(file);
	fclose(out);

	return 0;
}