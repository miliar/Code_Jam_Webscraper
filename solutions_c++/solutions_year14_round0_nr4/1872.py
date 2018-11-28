// codejamQualD.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

void Sort(double* arr, int count, int order = 1) // order 1 => from min to max, -1 => from max to min
{
	if(order == 1)
		for(int j=0;j<count-1;j++)
			for(int i=0;i<count-1-j;i++)
			{
				if(arr[i]>arr[i+1])
				{
					double temp=arr[i];
					arr[i]=arr[i+1];
					arr[i+1]=temp;
				}
			}
	else
		for(int j=0;j<count-1;j++)
			for(int i=0;i<count-1-j;i++)
			{
				if(arr[i]<arr[i+1])
				{
					double temp=arr[i];
					arr[i]=arr[i+1];
					arr[i+1]=temp;
				}
			}
}

int CountScoreModifiedWar(double *naomi, double *ken, int count) // same order (rising)
{
	if(naomi[count-1]<ken[0]) return 0; // NAOMI CANT WIN A SINGLE ROUND
	if(ken[count-1]<naomi[0]) return count; // NAOMI WINS EVERY ROUND
	/*int score = count;
	for(int i=count-1;i>=0;i--)
		if(naomi[count-1]<=ken[i]) score--;
		else break;
	for(int i=0;i<count-1;i++)
		if(naomi[i]<=ken[0]) score--;
		else break; */
	int score = 0;
	for(int i=0;i<count;i++)
	{
		if(naomi[i]<ken[i])
		{
			naomi[i]=-1;
			ken[count-1]=-1;
			Sort(naomi,count);
			Sort(ken,count);
		}
		else score++;
	}	
	return score;
}

int CountScoreNormalWar(double *naomi, double *ken, int count) // both arrays should be in the same (rising) order
{
	int lastKenBlock = 0;
	int scoreASC = 0;
	for(int i = 0; i < count ; i++)
	{
		bool found = false;
		for(int j=lastKenBlock; j<count; j++)
		{
			if(ken[j]>=naomi[i])
			{
				found = true;
				lastKenBlock = j+1;
				break;
			}
		}
		if(!found)
		{
			scoreASC = count-i;
			break;
		}
	}

	return scoreASC;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* in = fopen("inputD.in","r");
	FILE* out = fopen("outputD.out","w");

	int caseCount=0, blockCount = 0;
	double *blocksKen, *blocksNaomi;
	fscanf(in,"%d",&caseCount);

	for(int i=0;i<caseCount;i++)
	{
		fscanf(in,"%d",&blockCount);
		blocksKen = new double[blockCount];
		blocksNaomi = new double[blockCount];
		for(int j=0;j<blockCount;j++)
			fscanf(in,"%lf",&blocksNaomi[j]);
		for(int j=0;j<blockCount;j++)
			fscanf(in,"%lf",&blocksKen[j]);

		Sort(blocksNaomi,blockCount);
		Sort(blocksKen,blockCount);
		int normalScore = CountScoreNormalWar(blocksNaomi,blocksKen,blockCount);
		int modifiedScore = CountScoreModifiedWar(blocksNaomi,blocksKen,blockCount);

		fprintf(out,"Case #%d: %d %d\n",i+1,modifiedScore,normalScore);

		delete [] blocksKen;
		delete [] blocksNaomi;
	}
	fclose(in); fclose(out);
	return 0;
}

