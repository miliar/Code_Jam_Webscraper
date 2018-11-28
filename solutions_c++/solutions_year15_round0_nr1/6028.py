#define _CRT_SECURE_NO_DEPRECATE

//重要:文件要放在源文件的文件夹里面.
/*
fin = fopen("data.in", "r");
fout = fopen("data.out", "w");

fscanf(fin, "%d", &temp);
fprintf(fout, "%d", temp);

fclose(fin);
fclose(fout);
*/


#include <stdio.h>

int main(){
	FILE *fin, *fout;
	fin = fopen("A-large.in", "r");
	fout = fopen("data.out", "w");

	int T = 0, k = 1;
	fscanf(fin, "%d", &T);
	while (T)
	{
		char s[1000000] = { 0 };
		int smax = 0;
		int count = 0;
		int i = 0, j = 0, n = 0, x = 0;

		fscanf(fin, "%d", &smax);
		fgetc(fin);
		for (i = 0; i <= smax; i++){
			s[i] = fgetc(fin);
		}

		for (i = 1; i <= smax; i++)
		{
			n = n + (s[i - 1] - '0');//前面有多少人站起来了
			if (n < i)
			{
				count = count + (i - n);
				x = i - n;
			}
			if (x)
			{
				n = n + x;
				x = 0;
			}

		}

		fprintf(fout, "Case #%d: %d", k, count);
		k++;
		T--;
		if (T){
			fprintf(fout, "\n");
		}
	}

	fclose(fin);
	fclose(fout);

	return 0;
}
