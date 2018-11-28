#include<stdio.h>
#include<conio.h>

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int totalCase, i=0, m=0, k=0, j, numberOfShyness, cur, shyness = 0;

	scanf("%d", &totalCase);

	for (i = 0; i < totalCase; i++){
		scanf("%d", &numberOfShyness);
		fgetc(stdin);
		for (j = 0; j <= numberOfShyness; j++){
			cur = fgetc(stdin) - 48;

			if (shyness > m){
				k += (shyness - m);
				m += (shyness - m);
			}
			m += cur;

			shyness++;
		}

		printf("Case #%d: %d\n", i+1, k);
		shyness = 0;
		m = 0;
		k = 0;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}