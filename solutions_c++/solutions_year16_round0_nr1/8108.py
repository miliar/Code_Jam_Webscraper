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


void AppendDigits(int recentNo, std::vector<int>& passed)
{
	for (; recentNo > 0; recentNo /= 10)
	{
		if (std::find(passed.begin(), passed.end(), recentNo % 10) == passed.end())
		{
			passed.push_back(recentNo % 10);
		}
		
	}
	return;
}


/*
*
*/

int main()
{
	freopen("I.in", "r", stdin);
	freopen("O.op", "w", stdout);

	int cases;
	scanf("%d", &cases);
	int caserunning = 0;
	while (cases--)
	{
		int startNo;
		int recentNo;
		std::vector<int> passed;
		std::vector<int> visited;

		scanf("%d", &startNo);		
		int counter = 1;
		while (passed.size() < 10)
		{
			recentNo = startNo * counter;
			if (std::find(visited.begin(), visited.end(), recentNo) != visited.end())
			{
				break;
			}
			visited.push_back(recentNo);
			AppendDigits(recentNo , passed);
			counter++;

		}


		if (passed.size() == 10)
		{
			printf("Case #%d: %d\n", ++caserunning, recentNo);
		}
		else
		{
			printf("Case #%d: INSOMNIA\n", ++caserunning);
		}		

	}


	return 0;
}

