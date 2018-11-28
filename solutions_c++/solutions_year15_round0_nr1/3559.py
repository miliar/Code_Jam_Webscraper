#include <stdio.h>
FILE * in = fopen("A-large.in" , "r");
FILE * out = fopen("A-large.out" , "w");

int nS;
int S[1001];
char szInput[2000];
int T;
int nOutput;

void Input()
{
	fscanf(in, "%d %s", &nS, &szInput);
	
	for(int i=0; i<=nS; i++)
	{
		S[i] = szInput[i] - '0';
	}
}

void Process()
{
	int nSum = S[0];
	nOutput = 0;
	for(int i=1; i<=nS; i++)
	{
		if (S[i]>0 && nSum<i)
		{
			nOutput += (i-nSum);
			nSum = i + S[i];
		}
		else
		{
			nSum += S[i];
		}
	}
}

void Output()
{
	fprintf(out, "Case #%d: %d\n", T, nOutput);
}

int main()
{
	int nNumOfCase;

	fscanf(in, "%d", &nNumOfCase);	

	for(T = 1; T<=nNumOfCase; T++)
	{
		Input();
		Process();
		Output();
	}
	return 0;
}
