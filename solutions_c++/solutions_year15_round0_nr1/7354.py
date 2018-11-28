// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <io.h>

using namespace std;

int main(int argc, char* argv[])
{
	string filename;
	string fileout = "A-small-attempt.out";

	if (argc > 1)
		filename = argv[1];
	else
		filename = "A-small-attempt.in";

	FILE *fp = fopen(filename.c_str(), "r");
	FILE *fpout = fopen(fileout.c_str(), "w");

	if (fp == NULL)
		return 0;

	int nTestCase = 0, nItem;
	char sLevel[1024] = { 0 };
	int nLen = 0;
	int nPerson = 0;
	int nCount = 0;
	try
	{
		fscanf(fp, "%d", &nTestCase);

		for (int T = 0; T < nTestCase; T++)
		{
			fscanf(fp, "%d%s", &nItem, sLevel);
			nPerson = 0;
			nLen = strlen(sLevel);
			nCount = 0;

			for (int i = 0; i < nLen; i++)
			{
				if (i > nCount+nPerson && (sLevel[i] - 48) > 0)
					nPerson += (i - (nCount+nPerson));
				nCount += (sLevel[i] - 48);
			}
			
			fprintf(fpout, "Case #%d: %d\n", T + 1, nPerson);
			cout << "Case #" << T + 1 << ": " << nPerson << endl;
		}
	}
	catch (...)
	{
	
	}

	fclose(fp);
	fclose(fpout);

	return 0;
}

