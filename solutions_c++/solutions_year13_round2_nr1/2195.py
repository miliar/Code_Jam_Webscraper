#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX_LEN_LINE	1000

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

	int iOwn;
	int iSize;
	vector <int> iMote;
	int iRest;
	int iResult;

	int iCase;
	for (int i=0; i<iCountCases; i++)
	{
		iCase = i+1;

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		int ipos = 0;
		int ilen;
		bool bEndLine;
		// x1
		iOwn = GetInt(&strLine[ipos], &ilen, &bEndLine);
		ipos += (ilen+1);
		iSize = GetInt(&strLine[ipos], &ilen, &bEndLine);

		if (fgets(strLine, MAX_LEN_LINE, fInput) == NULL)
			return 0;
		
		ipos = 0;
		iMote.clear();
		for (int j=0; j<iSize; j++)
		{
			iMote.push_back(GetInt(&strLine[ipos], &ilen, &bEndLine));
			ipos += (ilen+1);
		}
		sort(iMote.begin(), iMote.end());

		// algorithm
		iResult = 0;
		iRest = iSize;
		ipos = 0;

		//if (iCase==6)
		//	iCase = iCase;

		if (iOwn==1)
			iResult = iSize;
		else
		{
			for (int j=0; j<iSize; j++)
			{
				if (iOwn>iMote[j])
				{
					iOwn += iMote[j];
				}
				else
				{
					int iRaise = 0;
					int iH = iOwn;
					while (iH<=iMote[j])
					{
						iH *= 2;
						iH--;
						iRaise++;
					}
					if (iRaise < (iSize-j))
					{
						iResult += iRaise;
						iOwn = iH + iMote[j];
					}
					else
					{
						iResult += (iSize-j);
						j = iSize;
					}
				}
			}
		}

		
		
		// Ausgabe
		fprintf(fOutput, "Case #%d: %d\n", iCase, iResult);

		iCase++;
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}