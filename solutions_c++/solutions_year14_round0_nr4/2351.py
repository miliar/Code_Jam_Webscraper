#include <iostream>
#include <algorithm>
using namespace std;

int scoreWar(double* blockNaomi, double* blockKen, int N)
{
	int i, j;
	int score = N;
	bool used[1000];
	memset(used, 0, 1000*sizeof(bool));
	for (i = 0; i<N; i++)
	{
		double curBlock = blockNaomi[i];
		bool win = true;
		for (int j = 0; j<N; j++)
		{
			if (used[j])
				continue;
			if (blockKen[j]>curBlock)
			{
				used[j] = true;
				score--;
				win = false;
				break;
			}
		}
		if (win)
			break;
	}
	return score;
}

int scoreDWar(double* blockNaomi, double* blockKen, int N)
{
	int i, j;
	int score = 0;
	bool used[1000];
	memset(used, 0, 1000*sizeof(bool));
	for (i = 0; i<N; i++)
	{
		double curBlock = blockKen[i];
		for (int j = 0; j<N; j++)
		{
			if (used[j])
				continue;
			if (blockNaomi[j]>curBlock)
			{
				used[j] = true;
				score++;
				break;
			}
		}
	}
	return score;
}

int main()
{
	FILE* fp = fopen("D:\\workspace\\codejam\\D-large.in","r");
	FILE* fo = fopen("D:\\workspace\\codejam\\result.txt","w");
	int tSize, N;
	double blockNaomi[1000];
	double blockKen[1000];
	fscanf(fp,"%d\n", &tSize);

	for (int i = 1; i<=tSize; i++)
	{
		fscanf(fp,"%d\n", &N);
		memset(blockNaomi,0,1000*sizeof(double));
		memset(blockKen,0,1000*sizeof(double));
		for (int j = 0; j<N; j++)
		{
			if (j == N-1)
				fscanf(fp,"%lf\n", blockNaomi+j);
			else
				fscanf(fp,"%lf ", blockNaomi+j);
		}
		for (int j = 0; j<N; j++)
		{
			if (j == N-1)
				fscanf(fp,"%lf\n", blockKen+j);
			else
				fscanf(fp,"%lf ", blockKen+j);
		}

		sort(blockNaomi,blockNaomi+N);
		sort(blockKen,blockKen+N);

		int scoreW = scoreWar(blockNaomi, blockKen,N);
		int scoreD = scoreDWar(blockNaomi, blockKen,N);
		fprintf(fo,"Case #%d: %d %d\n",i,scoreD,scoreW);

		/*for (int j = 0; j<N; j++)
		{
			printf("%lf ", blockNaomi[j]);
		}
		printf("\n");
		for (int j = 0; j<N; j++)
		{
			printf("%lf ", blockKen[j]);
		}
		printf("\n");*/
	}
	fclose(fp);
	fclose(fo);
	system("pause");
	return 0;
}