// jam2-lawnmover.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <string.h>
#include <tchar.h>
#define _CRT_SECURE_NO_WARNINGS

//------------------------------------------------------------------------------------------------
bool solveBoard( int n, int m, int board[128][128] )
{
	char maxRow   [128]; memset(maxRow    , 0, n);
	char maxColumn[128]; memset(maxColumn , 0, m);
	
	//-- calc max row/col
	for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	{
		int curItem = board[i][j];
		if( maxRow   [i] < curItem ) maxRow[i] = curItem;
		if( maxColumn[j] < curItem ) maxColumn[j] = curItem;
	}

	//-- check for each i,j is either max(i,*) or max(*,j)
	for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	{
		int curItem = board[i][j];
		if( curItem != maxRow[i]	&&
			curItem != maxColumn[j] )
			return false;
	}

	return true;
}
//------------------------------------------------------------------------------------------------
int main(int argc, char* argv[])
{
	FILE *in = argc>1 ? fopen(argv[1],"r") : stdin;
	FILE *out= argc>2 ? fopen(argv[2],"w")  : stdout;

	if(in==NULL || out==NULL)
	{
		printf("Error in params");
		return 0;
	}

	//-- read solutions
	int nSolutions = 0;	
	fscanf(in,"%d\n",&nSolutions);
	{
		for(int s=0;s<nSolutions;s++)
		{
			//-- parse dimensions
			int n=0,m=0;
			fscanf(in,"%d %d\n",&n,&m);

			//-- parse board
			int board[128][128];

			for(int i=0;i<n;i++)
			{
				for(int j=0;j<m;j++)
					fscanf(in,"%d",&(board[i][j]));

				fscanf(in,"\n");
			}

			//-- process board
			bool res=solveBoard(n,m,board);

			//-- register output
			fprintf(out,"Case #%d: %s\n",s+1, res ? "YES" : "NO" );
		}
	}

	fclose(in);
	fclose(out);

	return 0;
}