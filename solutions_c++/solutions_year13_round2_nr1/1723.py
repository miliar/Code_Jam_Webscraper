#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

long int motes[101];
int main()
{
	int caseNum = 1;
	FILE *input, *output;
	if((input = fopen("test","r"))==NULL)
	{
		printf("can't open file\n");
		exit(0);
	}
	output = fopen("output","w");


	int T;
	fscanf(input,"%d",&T);
	while(T--)
	{
		long int A,N;
		fscanf(input,"%d %d",&A,&N);
		for(int i = 0;i<N;i++)
		{
			fscanf(input,"%d",&motes[i]);
		}
		long int operation = N;
		sort(motes,motes+N);
		long int i = 0;
		long int add = 0;
		for(;i<N;i++)
		{
			if(motes[i]<A)
			{
				A+=motes[i];
				operation--;
			}
			else{break;}
		}
		long int maxAdd = operation;			//try to reduce it
		long int gain[102] = {0};
		//get add array
		long int smallestGain = 0;
		long int j = 1;
		for(j = 1;j<=maxAdd;j++)
		{
			gain[j] = gain[j-1]+1;
			A = A*2-1;
			while(A>motes[i]&&i<N)
			{
				A+=motes[i];
				gain[j]--;
				i++;
			}
			if(gain[j]<smallestGain)
			{
				smallestGain = gain[j];
			}
		}
		fprintf(output,"Case #%d: %d\n",caseNum++, operation+smallestGain);
	}
	return 0;
}