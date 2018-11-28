// app.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <Windows.h>  //#include <stdio.h>

// Given 2 rows of Y numbers.... see if there is a COMMON number in them or not!
void find_em(int y, int *first, int *second)
{
	int magic_num = 0;
	int num_found = 0;

	for (int i=0; i < y; i++) for (int j=0; j < y; j++) if (first[i] == second[j]) { magic_num = first[i]; num_found++; }

	if (0 == num_found)      _tprintf(TEXT("Volunteer cheated!"));
	else if (1 == num_found) _tprintf(TEXT("%d"), magic_num);
	else                     _tprintf(TEXT("Bad magician!"));
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T_test_cases = 0;

	FILE *fp = stdin;
	if (argc > 1) fp = _tfopen(argv[1], TEXT("r"));
	if (NULL == fp) return 1;

	int x=4;  int y=4;

	/* WHO CARES.... ONLY LOOK AT THE ROW THAT IS PICKED!!!	
	int **first_arrange = new int*[x];
	int **second_arrange = new int*[x];
	for (int i = 0; i < x; i++) first_arrange[i]  = new int[y];
	for (int i = 0; i < x; i++) second_arrange[i] = new int[y];
	*/
	int *first_arrange = new int[x];
	int *second_arrange = new int[x];
	
	_ftscanf(fp, TEXT("%d"), &T_test_cases);
	for (int i = 1; i <= T_test_cases; i++)
	{
		_tprintf(TEXT("Case #%d: "), i);
		
		int who_cares;

		int first_row = 0;
		_ftscanf(fp, TEXT("%d"), &first_row);
		for (int j = 0; j < x; j++)
		{
			if (first_row == (j+1)) for (int k = 0; k < y; k++) _ftscanf(fp, TEXT("%d"), &(first_arrange[k]));
			else                    for (int k = 0; k < y; k++) _ftscanf(fp, TEXT("%d"), &who_cares);
		}
		int second_row = 0;
		_ftscanf(fp, TEXT("%d"), &second_row);
		for (int j = 0; j < x; j++)
		{
			if (second_row == (j+1)) for (int k = 0; k < y; k++) _ftscanf(fp, TEXT("%d"), &(second_arrange[k]));
			else                     for (int k = 0; k < y; k++) _ftscanf(fp, TEXT("%d"), &who_cares);
		}

		find_em(y, first_arrange, second_arrange);
		_tprintf(TEXT("\n"));
	}

	/*
	for (int i = 0; i < x; i++) delete [] second_arrange[i];
	for (int i = 0; i < x; i++) delete [] first_arrange[i];
	delete [] second_arrange;
	delete [] first_arrange;
	*/
	delete [] second_arrange;
	delete [] first_arrange;

	if (stdin == fp) fclose(fp);
	return 0;
}

