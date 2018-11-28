#include <iostream>
#include <stdlib.h>

int compare(const void* a, const void* b)
{
	int result = 0;
	if((*(double*)a > *(double*)b)) result = 1;
	else if((*(double*)a < *(double*)b)) result = -1;
	else result = 0;

	return result;
}

int main()
{
	
	//FILE* file = fopen("C:\\Users\\RezaulAkram\\Desktop\\D-large.in","r");;
	//FILE* opfile = fopen("C:\\Users\\RezaulAkram\\Desktop\\opfile.txt","w");
	
	FILE* file = stdin;
	FILE* opfile = stdout;

	int T = 0;
	fscanf(file, "%d",&T);

	for(int i = 0 ; i < T; i++)
	{
		int N = 0;

		fscanf(file,"%d", &N);

		double* Naomi	= new double[N];
		double* Ken		= new double[N];
		int* KenAv	= new int[N];
		int* _NaomiAv	= new int[N];

		memset(KenAv, 0x0, sizeof(int) * N);

		memset(_NaomiAv, 0x0, sizeof(int) * N);

		for(int j = 0; j < N; j++)
		{
			fscanf(file,"%lf", &Naomi[j]);
		}

		for(int j = 0; j < N; j++)
		{
			fscanf(file,"%lf", &Ken[j]);
		}

		int KenWon = 0;
		int _NaomiWon = 0;
		//qsort(Naomi, N, sizeof(double), compare);
		//qsort(Ken, N, sizeof(double), compare);

		for(int j = 0; j < N; j++)
		{
			int minId = -1;
			int minId2 = -1;
			double minValue = DBL_MAX;
			double minValue2 = DBL_MAX;
			for(int k = 0;k < N; k++)
			{
				if(KenAv[k] == 1) continue;

				if(Ken[k] > Naomi[j])
				{
					if((Ken[k] - Naomi[j]) < minValue)
					{
						minValue = (Ken[k] - Naomi[j]);
						minId = k;
					}
				}
				else
				{
					if(Ken[k]< minValue2)
					{
						minValue2 = Ken[k];
						minId2 = k;
					}
				}
				
			}
			if(minId >= 0)
			{
				KenAv[minId] = 1;
				KenWon++;
			}
			else
				KenAv[minId2] = 1;
		}
		for(int j = 0; j < N; j++)
		{
			int _minId = -1;
			int _minId2 = -1;
			double _minValue = DBL_MAX;
			double _minValue2 = DBL_MAX;

			for(int k = 0;k < N; k++)
			{
				if(_NaomiAv[k] == 1) continue;

				if(Ken[j] < Naomi[k])
				{
					if( Naomi[k] - (Ken[j]) < _minValue)
					{
						_minValue = ( Naomi[k] - Ken[j]);
						_minId = k;
					}
				}
				else
				{
					if(Naomi[k]< _minValue2)
					{
						_minValue2 = Naomi[k];
						_minId2 = k;
					}
				}
				
			}
			if(_minId >= 0)
			{
				_NaomiAv[_minId] = 1;
				_NaomiWon++;
			}
			else
				_NaomiAv[_minId2] = 1;
		}

		fprintf(opfile, "Case #%d: %d %d\n", (i+1),_NaomiWon,(N - KenWon));

		delete(Naomi);
		delete(Ken);
		delete(KenAv);
		delete(_NaomiAv);
	}
}