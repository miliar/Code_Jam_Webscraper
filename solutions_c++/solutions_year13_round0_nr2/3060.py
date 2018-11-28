#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int
	T;

int check_lawn(int h[100][100], int rowmax[100], int colmax[100], int N, int M)
{
	for (int j = 0; j < N; j++)
      for (int k = 0; k < M; k++)
         if (h[j][k] != MIN(rowmax[j], colmax[k]))
            return (0);

   return (1);
}

int main(int argc, char *argv[])
{
   FILE
	   *fpi = fopen("B-large.in", "r"),
	   *fpo = fopen("B-large.out", "w");

	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		int
         h[100][100],
         rowmax[100] = { 0 },
         colmax[100] = { 0 },
         c,
         N,
         M;

		fscanf(fpi, "%d", &N);
		fscanf(fpi, "%d", &M);

		for (int j = 0; j < N; j++)
         for (int k = 0; k < M; k++)
            {
   			fscanf(fpi, "%d", &c);
            h[j][k] = c;
            rowmax[j] = MAX(rowmax[j], c);
            colmax[k] = MAX(colmax[k], c);
            }

      fprintf(fpo, "Case #%d: %s\n", i + 1, check_lawn(h, rowmax, colmax, N, M) ? "YES" : "NO");
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
