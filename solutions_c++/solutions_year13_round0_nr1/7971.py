// tictac.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fpin, *fpout;
	char buff[100], *ptr, board[4][4];
	int no_tests, err, status, offset;

	/* open output file */
	err = fopen_s(&fpout, "test.out", "w");
	if (err != 0)
	{
		printf("Unable to open output file\n");
		return(-1);
	}

	/* open input file */
	err = fopen_s(&fpin, "test.in", "r");
	if (err != 0)
	{
		printf("Unable to open input file\n");
		return(-2);
	}
	/* read in input file */
	fgets( buff, 99, fpin );
	sscanf_s(buff, "%d", &no_tests);
	printf("Number of tests: %d", no_tests);

	for (int i=0; i<no_tests; i++)
	{
		/* read in four lines, and blank line. */
		for (int j=0; j<4; j++)
		{
			fgets( buff, 99, fpin );
			/* skip leading spaces */
			for (offset=0; buff[offset] == ' '; offset++);
			for (int k=0; k<4; k++)
				board[j][k]=buff[k+offset];
		}
		fgets( buff, 99, fpin );  /* discard blank line */

		fprintf(fpout, "Case #%d: ", i+1);

		/* process board info, determine winner, draw or in progress */
		status=3;

		/* Check Ranks */
		if ((board[0][0] == 'X' || board[0][0] == 'T') && (board[0][1] == 'X' || board[0][1] == 'T') && (board[0][2] == 'X' || board[0][2] == 'T') && (board[0][3] == 'X' || board[0][3] == 'T'))
			status = 1;
		if ((board[1][0] == 'X' || board[1][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') && (board[1][2] == 'X' || board[1][2] == 'T') && (board[1][3] == 'X' || board[1][3] == 'T'))
			status = 1;
		if ((board[2][0] == 'X' || board[2][0] == 'T') && (board[2][1] == 'X' || board[2][1] == 'T') && (board[2][2] == 'X' || board[2][2] == 'T') && (board[2][3] == 'X' || board[2][3] == 'T'))
			status = 1;
		if ((board[3][0] == 'X' || board[3][0] == 'T') && (board[3][1] == 'X' || board[3][1] == 'T') && (board[3][2] == 'X' || board[3][2] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T'))
			status = 1;
		if ((board[0][0] == 'O' || board[0][0] == 'T') && (board[0][1] == 'O' || board[0][1] == 'T') && (board[0][2] == 'O' || board[0][2] == 'T') && (board[0][3] == 'O' || board[0][3] == 'T'))
			status = 2;
		if ((board[1][0] == 'O' || board[1][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') && (board[1][2] == 'O' || board[1][2] == 'T') && (board[1][3] == 'O' || board[1][3] == 'T'))
			status = 2;		
		if ((board[2][0] == 'O' || board[2][0] == 'T') && (board[2][1] == 'O' || board[2][1] == 'T') && (board[2][2] == 'O' || board[2][2] == 'T') && (board[2][3] == 'O' || board[2][3] == 'T'))
			status = 2;
		if ((board[3][0] == 'O' || board[3][0] == 'T') && (board[3][1] == 'O' || board[3][1] == 'T') && (board[3][2] == 'O' || board[3][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T'))
			status = 2;
		/* Check Rows */
		if ((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][0] == 'X' || board[1][0] == 'T') && (board[2][0] == 'X' || board[2][0] == 'T') && (board[3][0] == 'X' || board[3][0] == 'T'))
			status = 1;
		if ((board[0][1] == 'X' || board[0][1] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') && (board[2][1] == 'X' || board[2][1] == 'T') && (board[3][1] == 'X' || board[3][1] == 'T'))
			status = 1;
		if ((board[0][2] == 'X' || board[0][2] == 'T') && (board[1][2] == 'X' || board[1][2] == 'T') && (board[2][2] == 'X' || board[2][2] == 'T') && (board[3][2] == 'X' || board[3][2] == 'T'))
			status = 1;
		if ((board[0][3] == 'X' || board[0][3] == 'T') && (board[1][3] == 'X' || board[1][3] == 'T') && (board[2][3] == 'X' || board[2][3] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T'))
			status = 1;
		if ((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][0] == 'O' || board[1][0] == 'T') && (board[2][0] == 'O' || board[2][0] == 'T') && (board[3][0] == 'O' || board[3][0] == 'T'))
			status = 2;
		if ((board[0][1] == 'O' || board[0][1] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') && (board[2][1] == 'O' || board[2][1] == 'T') && (board[3][1] == 'O' || board[3][1] == 'T'))
			status = 2;
		if ((board[0][2] == 'O' || board[0][2] == 'T') && (board[1][2] == 'O' || board[1][2] == 'T') && (board[2][2] == 'O' || board[2][2] == 'T') && (board[3][2] == 'O' || board[3][2] == 'T'))
			status = 2;
		if ((board[0][3] == 'O' || board[0][3] == 'T') && (board[1][3] == 'O' || board[1][3] == 'T') && (board[2][3] == 'O' || board[2][3] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T'))
			status = 2;
		/* Check Diagonals */
		if ((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') && (board[2][2] == 'X' || board[2][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T'))
			status = 1;
		if ((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') && (board[2][2] == 'O' || board[2][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T'))
			status = 2;
		if ((board[0][3] == 'X' || board[0][3] == 'T') && (board[1][2] == 'X' || board[1][2] == 'T') && (board[2][1] == 'X' || board[2][1] == 'T') && (board[3][0] == 'X' || board[3][0] == 'T'))
			status = 1;
		if ((board[0][3] == 'O' || board[0][3] == 'T') && (board[1][2] == 'O' || board[1][2] == 'T') && (board[2][1] == 'O' || board[2][1] == 'T') && (board[3][0] == 'O' || board[3][0] == 'T'))
			status = 2;
		/* check for not completed */
		if (status == 3)
			for (int a=0; a<4; a++)
				for (int b=0; b<4; b++)
					if (board[a][b]=='.')
					{
						status=0;
						a=b=4;
					}

		switch (status) 
		{
		case 0:
			fprintf(fpout, "Game has not completed\n");
			break;

		case 1:
			fprintf(fpout, "X won\n");
			break;

		case 2:
			fprintf(fpout, "O won\n");
			break;

		case 3:
			fprintf(fpout, "Draw\n");
			break;
		
		}
	}

	printf("\n");
	return 0;
}

