// CodeJamQB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

char lawn[100][100];
int N, M;
FILE * input;

#define FALSE 0
#define TRUE 1

int checkrow(int n, int m)
{
	char v = lawn[n][m];

	for(int i=0; i<M; i++)
		if( v < lawn[n][i])
			return FALSE;

	return TRUE;
}

int checkcol(int n, int m)
{
	char v = lawn[n][m];

	for(int i=0; i<N; i++)
		if( v < lawn[i][m])
			return FALSE;

	return TRUE;
}
char * check()
{
	for(int n=0;n< N; n++)
	{
		for(int m=0; m<M; m++)
		{
			if( checkrow(n,m) == FALSE && checkcol(n,m) == FALSE)
				return "NO";
		}
	}
	return "YES";
}
void readlawnd()
{	int tmp;
	fscanf(input, "%d %d ", &N, &M);

	for(int n=0; n<N; n++)
		for(int m=0; m<M; m++)
		{
			fscanf(input, "%d ", &tmp);
			lawn[n][m]=(char ) tmp;
		}

}


int _tmain(int argc, _TCHAR* argv[])
{
	int cases;



	input = _wfopen (argv[1],L"r");

	fscanf(input, "%d ", &cases);

	for(int i=1; i<= cases; i++)
	{
		readlawnd();
		printf("Case #%d: %s\n", i, check());
	}
	return 0;


}

