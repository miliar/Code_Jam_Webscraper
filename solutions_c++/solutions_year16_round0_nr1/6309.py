#include <stdio.h>

int main(){
	FILE *Fin;
	FILE *Fout;
	int TestLoof = 0;
	int TestCount = 0;
	int numFlag[10] = { 0 };
	int flag = 0;
	int num = 0;
	long long int temp=0;
	int count = 0;
	int ten = 10;
	int i = 0, j = 0, k = 0;
	Fin = fopen("A-large.in", "r");
	Fout = fopen("output.txt", "w");

	fscanf(Fin,"%d",&TestCount);

	for (TestLoof = 1; TestLoof <= TestCount; TestLoof++){
		num = 0;
		flag = 0;
		count = 0;
		temp = 0;
		for (i = 0; i < 10;i++){
			numFlag[i] = 0;
		}

		fscanf(Fin, "%d", &num);

		temp = num;
		if (num != 0){
			for (i = 1; count != 10; i++){
				temp = i*num;
				j = 1;
				while (temp / ten != 0){ temp /= 10; j++; }
				temp = i*num;
				for (k = 0; k < j; k++){
					if (numFlag[temp % 10] == 0){
						count++;
						numFlag[temp % 10] = 1;
					}
					temp /= 10;
				}
				temp = i*num;
			}
		}

		fprintf(Fout,"Case #%d: ",TestLoof);
		if (num != 0){
			fprintf(Fout, "%lld\n", temp);
		}
		else {
			fprintf(Fout, "INSOMNIA\n");
		}
	}
	fclose(Fout);
	fclose(Fin);

	return 0;
}