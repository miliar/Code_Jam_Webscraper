#include <stdio.h>
#include<stdlib.h>
#include<string.h>


int main()
{
	int N;
	int M[1000]; 

	FILE *fp;
	FILE *fpread;
	fopen_s(&fp, "out1.out", "wt+");
	fopen_s(&fpread, "in.in", "r");
	fscanf_s(fpread, "%d", &N);

	for (int Case = 1; Case <= N; Case++)
	{
		int NN;
		fscanf_s(fpread, "%d", &NN);
		for (int i = 0; i < NN; i++)
		{
			fscanf_s(fpread, "%d", &M[i]);
			
		}
		int RES1 = 0;
		int RES2 = 0;
		int Max = 0;
		for (int i =1; i < NN; i++)
		{
			if (M[i - 1]>M[i])
				RES1 += M[i - 1] - M[i];
			if (M[i - 1] - M[i]>Max)
				Max = M[i - 1] - M[i];
		}
		for (int i = 0; i < NN-1; i++)
		{
			if (M[i]>Max)
				RES2 += Max;
			else
				RES2 += M[i];
		}


		fprintf(fp, "Case #%d: %d %d\n", Case,RES1,RES2);
		
	}
	fclose(fp);
	fclose(fpread);
	system("Pause");
	return 0;
}