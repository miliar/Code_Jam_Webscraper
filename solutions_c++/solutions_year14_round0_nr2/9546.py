// ConsoleApplication1.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//


#include <stdio.h>
#include <cstdlib>

int main()
{
	int T = 0;

	FILE *fin;
	FILE *fout;
	fin = fopen("B-small-attempt0.in", "r");
	fout = fopen("B-small-attempt0.out", "w");
	fscanf(fin, "%d", &T);
	
//	printf("%d\n", T);
	
	float C, F, X, answer = 0.00000f, candidate = 0.00000f;

	for (int i = 0; i < T; i++) {				

		float base = 2.00000f;

		fscanf(fin, "%f %f %f", &C, &F, &X);

//		printf("%f %f %f\n", C, F ,X);

		// N equals number of farms
		int N = 0;
		answer = X / (base + 0 * F);
		while (true)
		{
			candidate = 0.00000f;

			N = N + 1;
			for (int i = 0; i < N; i++){
				candidate = candidate + C / (base + (float)(i * F));		
			}
			candidate = candidate + X / (base + (float)(N * F));

			/*
			printf("\nN: %d", N);
			printf("\nanswer: %f", answer);
			printf("\ncandidate: %f", candidate);
			*/
			if (candidate <= answer)
				answer = candidate;
			else 
				break;

			/*
			N=0	candidate = X / base ;
			N=1 candidate = C / base + X / (base + 1 * F);
			N=2 candidate = C / base + C / (base + 1 * F) + X / (base + 2 * F);
			N=3 candidate = C / base + C / (base + 1 * F) + C / (base + 2 * F) + X / (base + 3 * F);
			*/
		}

		
		fprintf(fout, "Case #%d: ", i + 1);
			fprintf(fout, "%.7f\n", answer);
	}


	fclose(fin);
	fclose(fout);

//	getchar();
	return 0;
}


