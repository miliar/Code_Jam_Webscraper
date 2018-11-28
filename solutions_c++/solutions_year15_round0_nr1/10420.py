#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <fstream>
#include <math.h>

using namespace std;

string* LoadFile(ifstream inFile);

int main()
{
	FILE * pOutFile;
	ifstream inFile;
	int numCases = 0;

	inFile.open("in.txt");
	pOutFile = fopen("out.txt", "w");
	if (inFile.is_open())
	{
		inFile >> numCases;
		
		for (int i = 0; i < numCases; i++)
		{
			int maxShy = -1;
			int numShy[1000];
			int shyNumber = -1;
			int numStanding = 0;
			int numFriends = 0;
			int plus = 0;

			inFile >> maxShy;
			inFile >> shyNumber;
			numShy[0] = shyNumber / int(pow(10.0, maxShy));
			for (int j = 1; j < maxShy + 1; j++)
			{
				int number = shyNumber %  int(pow(10.0, maxShy - (j-1)));
				numShy[j] = number / int(pow(10.0, maxShy-j));
			}

			for (int j = 0; j < maxShy + 1; j++)
			{
				plus = j - numStanding;
				if (plus > 0)
				{
					numFriends += plus;
					numStanding += plus;
				}
				numStanding += numShy[j];
			}
			fprintf(pOutFile,"Case #%i: %i\n",i+1,numFriends);

		}
	}
	else
	{
		fprintf(pOutFile, "Error");
	}
	inFile.close();
	fclose(pOutFile);
	
}