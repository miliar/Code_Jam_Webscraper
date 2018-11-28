#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}

int diners[5000];
int answers[100];
int nbDiners;
int nbMinutes;
int total;
int maxPan;
int maxIndex;
int bestMinutes;

void eat()
{
	int newNbDinners = 0;
	for (int i = 0; i < nbDiners; i++)
	{
		diners[i]--;
		if (diners[i] > 0)
		{
			newNbDinners++;
			diners[newNbDinners - 1] = diners[i];
		}
	}
	nbDiners = newNbDinners;
}

void split()
{
	int nbMoves = 0;
	if (diners[maxIndex] == 9)
	{
		if (rand() % 2 == 0)
		{
			nbMoves = 5;
		}
		else
		{
			nbMoves = 3;
		}
	}
	else
	{
		nbMoves = diners[maxIndex] / 2;
	}
	diners[maxIndex] -= nbMoves;
	nbDiners++;
	diners[nbDiners - 1] = nbMoves;
}

void getMaxPan()
{
	maxPan = 0;
	for (int i = 0; i < nbDiners; i++)
	{
		if (diners[i] > maxPan)
		{
			maxPan = diners[i];
			maxIndex = i;
		}
	}
}

void process()
{
	freopen("B-small-attempt6.in", "r", stdin);
	freopen("B-small-attempt6.out", "w", stdout);

	int testcase;
	scanf("%d", &testcase);
	for (int case_id = 1; case_id <= testcase; case_id++)
	{
		maxPan = 0;
		nbDiners = 0;
		nbMinutes = 0;
		bestMinutes = 20000;
		scanf("%d", &nbDiners);
		for (int i = 0; i < nbDiners; i++)
		{
			scanf("%d", &diners[i]);
		}

		while (nbDiners > 0)
		{
			getMaxPan();

			int u = nbMinutes + maxPan;
			if (u < bestMinutes)
			{
				bestMinutes = u;
			}

			//if ((maxPan / 2) >= nbDiners)
			if (maxPan > 1)
			{
				split();
			}
			else
			{
				//printf("EAT\n");
				eat();
			}
			nbMinutes++;
		}

		if (nbMinutes >= bestMinutes)
		{
			nbMinutes = bestMinutes;
		}

		//printf("%d\n", nbMinutes);
		total += nbMinutes;
		fflush(stdout);

		if ((answers[case_id - 1] == 0) || (answers[case_id - 1] > nbMinutes))
		{
			answers[case_id - 1] = nbMinutes;
		}
	}

	total = 0;
}

int main()
{
	for (int i = 0; i <= 30000; i++)
	{
		process();
	}
	int t = 0;
	for (int case_id = 1; case_id <= 100; case_id++)
	{
		printf("Case #%d: ", case_id);
		printf("%d\n", answers[case_id - 1]);
		t += answers[case_id - 1];
	}
	//printf("Total: %d\n", t);

	return 0;
}

