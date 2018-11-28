/*
* File:   main.cpp
* Author: Sreekanth
*
* Created on Apr 12, 2014
*/

#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;


/*
*
*/

int main()
{
	freopen("I.in", "r", stdin);
	freopen("O.op", "w", stdout);

	int cases;
	scanf("%d", &cases);

	char dummy;
	scanf("%c", &dummy);

	int caserunning = 0;
	while (cases--)
	{
		int outswaps = 0;
		char previouschar;
		char currentchar;
		scanf("%c", &currentchar);
		previouschar = currentchar;
		while (currentchar != '\n')
		{
			if (previouschar != currentchar)
			{
				outswaps += 1;
			}
			previouschar = currentchar;
			scanf("%c", &currentchar);
		}
		if (previouschar == '-')
		{
			outswaps += 1;
		}
		
		printf("Case #%d: %d\n", ++caserunning, outswaps);


	}


	return 0;
}

