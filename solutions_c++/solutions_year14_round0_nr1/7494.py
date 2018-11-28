#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

void solver(int numCase)
{
	int guessRow[2], i, j;
	int card[2][4][4];
	
	// read inputs
	for (int k = 0; k < 2; k++)
	{
		scanf("%i", &guessRow[k]);
		guessRow[k]--; // start from index 0
		for (i = 0; i < 4; i++)
		{
			for (j = 0; j < 4; j++)
				scanf("%i", &card[k][i][j]);
		}
	}

	int numSol = 0, sol;
	// check how many numbers appear in the guess
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			if (card[0][guessRow[0]][i] == card[1][guessRow[1]][j])
			{
				sol = card[0][guessRow[0]][i];
				numSol++;
			}				
		}
	}

	if (numSol == 0)
		printf("Case #%i: Volunteer cheated!\n", numCase);
	else if (numSol == 1)
		printf("Case #%i: %i\n", numCase, sol);
	else
		printf("Case #%i: Bad magician!\n", numCase);
}

int main()
{
	int numCase, cases;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%i", &cases);
	for (numCase = 1; numCase <= cases; numCase++)
		solver(numCase);

	return 0;
}