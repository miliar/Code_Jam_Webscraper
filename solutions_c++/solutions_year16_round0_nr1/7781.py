#include <stdio.h>

int main(void)
{
	int t, n, temp1, temp2, k = 1, dab = 0;
	int numzero=0;
	int nums[10];

	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A-large.out","w");
	fscanf(fin, "%d", &t);

	for (int i = 1; i <= t; i++) {

		//scan n
		fscanf(fin, "%d",&n);
		//scanf("%d", &n);

		//reset num 0~9 to 0
		for (int j = 0; j < 10; j++) {
			nums[j] = 0;
		}

		k = 1;

		while (dab == 0) {
			if (n == 0) {
				break;
			}

			temp1 = k*n;
			temp2 = temp1;
			while(1){
				nums[temp2 % 10]++;

				if (temp2 >= 10) {
					temp2 /= 10;
				}
				else	break;
			} 

			k++;

			for (int l = 0; l < 10; l++) {
				if (nums[l] == 0)	numzero++;
				//printf("nums[%d] = %d\t", l, nums[l]);
			}
			//printf("\n");

			if (numzero == 0) {
				dab = temp1;
				break;
			}
			numzero = 0;
		}

		if( dab == 0) {
			fprintf(fout, "Case #%d:  INSOMNIA\n", i);
		}
		else {
			fprintf(fout, "Case #%d:  %d\n", i, dab);
		}
		dab = 0;
	}

		fclose(fin);
		fclose(fout);
	
}