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

	int x1;
	unsigned long long lR, lA;

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		

		int ipos = 0;
		lR = 0;
		while (strLine[ipos]>='0' && strLine[ipos]<='9')
		{
			lR *= 10;
			lR += strLine[ipos]-'0';
			ipos++;
		}
		ipos++;
		lA = 0;
		while (strLine[ipos]>='0' && strLine[ipos]<='9')
		{
			lA *= 10;
			lA += strLine[ipos]-'0';
			ipos++;
		}
		//int ilen;
		//bool bEndLine;
		// x1
		//x1 = GetInt(&strLine[ipos], &ilen, &bEndLine);
		//ipos += (ilen+1);
		
		// algorithm
		unsigned int iRes = 0;
		unsigned long long lAAll = 0;
		while (lAAll<=lA)
		{
			iRes++;
			lAAll += 2*lR + 4*(unsigned long long)iRes - 3;
			//lAAll += lR;
			//lAAll += lR;

			if (iRes%1000000==0)
				printf("\r%d", iRes);
		}
		iRes--;
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: %d\n", iCase, iRes);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}