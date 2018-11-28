// Diva.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int solve(int caseNumber){

	int n; scanf("%d", &n);

	int alreadyStanding = 0;

	char line[1200];
	scanf("%s", line);


	int result = 0;
	for (int i = 0; i <= n; i++){

		int asdigit = line[i] - '0';

		if (i > 0)
		{	
			if (i > 0 && asdigit > 0)
			{
				int gap = i - alreadyStanding;
				if (gap > 0){
					result += gap;
					alreadyStanding += gap;
				}
			}
		}

		alreadyStanding += asdigit;
	}

	return result;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int t; scanf("%d", &t);
	int caseNumber = 1;
	while (t--) {
		printf("Case #%d: %d\n", caseNumber, solve(caseNumber));
		caseNumber++;
	}
	return 0;
}

