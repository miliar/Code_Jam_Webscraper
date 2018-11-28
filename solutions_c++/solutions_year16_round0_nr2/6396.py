#include <stdio.h>

int main(){
	FILE *Fin;
	FILE *Fout;
	int TestLoof = 0;
	int TestCount = 0;
	char str[200];
	char temp = 0;
	int flag = 0;
	int i = 0, j = 0, k = 0;
	int len = 0;
	int count = 0;
	Fin = fopen("B-large.in", "r");
	Fout = fopen("output.txt", "w");

	fscanf(Fin, "%d", &TestCount);

	for (TestLoof = 1; TestLoof <= TestCount; TestLoof++){
		flag = 0;
		len = 0;
		i = 0;
		count = 1;

		fscanf(Fin, "%c", &temp);
		fscanf(Fin, "%s", str);

		while (str[i++]!=0){ len++; }

		temp = str[0];
		for (i = 1; i < len; i++){
			if (temp != str[i]){
				if (temp == '+'){
					temp = '-';
				}
				else{
					temp = '+';
				}
				flag = 1;
				count++;
			}
		}
		if (str[len-1]=='+'){
			count--;
		}
		
		fprintf(Fout, "Case #%d: ", TestLoof);
		fprintf(Fout, "%d\n", count);
	}
	fclose(Fout);
	fclose(Fin);

	return 0;
}