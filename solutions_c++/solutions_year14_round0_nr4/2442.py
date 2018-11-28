// DeceitfulWar.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int T = 0;
	int N = 0;
	double arrPlayer1[1000];
	double arrPlayer2[1000];
	int iDWar = 0;
	int iOptWar = 0;
	double temp = 0;

	FILE* fpin = fopen("C:\\GCJ\\D-large.in", "r");
	FILE* fpout = fopen("C:\\GCJ\\D-large.out", "w");

	if(NULL == fpin || NULL == fpout )
		return 0;

	fscanf(fpin, "%d", &T);

	for (int tc = 0; tc<T; tc++)
	{
		fscanf(fpin, "%d", &N);

		for (int i=0; i<N; i++)
		{
			fscanf(fpin, "%lf", &arrPlayer1[i]);			
		}

		for (int i=0; i<N; i++)
		{
			fscanf(fpin, "%lf", &arrPlayer2[i]);			
		}

		for (int i=0; i<N; i++)
		{
			for (int j=i+1; j<N; j++)
			{
				if (arrPlayer1[i]> arrPlayer1[j])
				{
					temp = arrPlayer1[i];
					arrPlayer1[i] = arrPlayer1[j];
					arrPlayer1[j] = temp;	
				}
			}
		}

		for (int i=0; i<N; i++)
		{
			for (int j=i+1; j<N; j++)
			{
				if (arrPlayer2[i]> arrPlayer2[j])
				{
					temp = arrPlayer2[i];
					arrPlayer2[i] = arrPlayer2[j];
					arrPlayer2[j] = temp;	
				}
			}
		}
			
		int index = 0;
		for (int i=0; i<N; i++)
		{
			for (int j=index; j<N; j++)
			{
				if (arrPlayer1[i] > arrPlayer2[j])
				{
					index = j+1;
					iDWar++;
					break;				
				}
			}
		}

		index = N-1;
		for (int i=N-1; i>=0; i--)
		{
			for (int j=index; j>=0; j--)
			{
				if (arrPlayer1[i] > arrPlayer2[j])
				{
					iOptWar++;
					break;				
				}
				else
				{
					index = j-1;
					break;
				}
			}
		}


		fprintf(fpout, "Case #%d: %d %d\n", tc+1, iDWar, iOptWar);
		iDWar = 0;
		iOptWar = 0;
	}
	
	fclose(fpin);
	fclose(fpout);
	return 0;
}
