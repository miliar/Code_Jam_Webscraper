#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE	500

int GetInt(char *str, int *len, bool *bEndLine)
{
	int ipos = 0;
	while (str[ipos] != ' ' && str[ipos] != '\n')
		ipos++;
	char strZahl[20];
	strncpy(strZahl, str, ipos);
	strZahl[ipos] = 0;
	int iResult = atoi(strZahl);
	*len = ipos;
	if (str[ipos]=='\n')
		*bEndLine = true;
	else
		*bEndLine = false;
	return iResult;
}
double GetDouble(char *str, int *len, bool *bEndLine)
{
	int ipos = 0;
	while (str[ipos] != ' ' && str[ipos] != '\n')
		ipos++;
	char strZahl[50];
	strncpy(strZahl, str, ipos);
	strZahl[ipos] = 0;
	double dResult = atof(strZahl);
	*len = ipos;
	if (str[ipos]=='\n')
		*bEndLine = true;
	else
		*bEndLine = false;
	return dResult;
}
void GetString(char *str,char *strOut, int *len, bool *bEndLine)
{
	int ipos = 0;
	while (str[ipos] != ' ' && str[ipos] != '\n')
		ipos++;
	strncpy(strOut, str, ipos);
	strOut[ipos] = 0;
	*len = ipos;
	if (str[ipos]=='\n')
		*bEndLine = true;
	else
		*bEndLine = false;
}



int main(int argv, char *argc[])
{
	if (argv < 2)
		return -1;
	

	int iCountCases = 0;
	
	// read Input
	FILE *fInput = fopen(argc[1], "r");
	if (fInput == NULL)
		return -1;

	// output
	FILE *fOutput = fopen("output.txt", "w");
	if (fOutput == NULL)
	{
		fclose(fInput);
		return -1;
	}


	char strLine[MAX_LEN_LINE];
	// read first line
	if (fgets(strLine, MAX_LEN_LINE, fInput)==NULL)
	{
		// Fehler beim Lesen
		return -1;
	}

	iCountCases = atoi(strLine);

	int iField[100][100];
	int iRows, iCols;

	int iNewField[100][100];

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		//
		iRows = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iCols = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);

		for (int iR=0; iR<iRows; iR++)
		{
			fgets(strLine, MAX_LEN_LINE, fInput);
			ipos = 0;
			for (int iC=0; iC<iCols; iC++)
			{
				iField[iR][iC] = GetInt(&strLine[ipos], &ilen, &bEndLine);
				ipos += (ilen+1);
			}
		}

		// algorithm
		for (int iR=0; iR<iRows; iR++)
			for (int iC=0; iC<iCols; iC++)
				iNewField[iR][iC] = 100;

		for (int iR=0; iR<iRows; iR++)
		{
			int iMax = 0;
			for (int iC=0; iC<iCols; iC++)
			{
				if (iField[iR][iC]>iMax)
					iMax = iField[iR][iC];
			}
			for (int iC=0; iC<iCols; iC++)
			{
				if (iNewField[iR][iC] > iMax)
					iNewField[iR][iC] = iMax;
			}
		}
		for (int iC=0; iC<iCols; iC++)
		{
			int iMax = 0;
			for (int iR=0; iR<iRows; iR++)
			{
				if (iField[iR][iC]>iMax)
					iMax = iField[iR][iC];
			}
			for (int iR=0; iR<iRows; iR++)
			{
				if (iNewField[iR][iC] > iMax)
					iNewField[iR][iC] = iMax;
			}
		}
		
		int iSum = 0;
		for (int iR=0; iR<iRows; iR++)
		{
			for (int iC=0; iC<iCols; iC++)
			{
				if (iField[iR][iC] != iNewField[iR][iC])
					iSum++;
			}
		}
		
		// Ausgabe
		if (iSum==0)
			fprintf(fOutput, "Case #%d: YES\n", iCase);
		else
			fprintf(fOutput, "Case #%d: NO\n", iCase);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}