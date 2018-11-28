#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

#define IN_FILE "B-large.in"
#define OUT_FILE "B-large.out"

#define MAX_S	100

int solve(char* c, int size);

int main()
{
	int T, cur_tc, i, result;
	long long N;
	char c;
	char cakes[MAX_S];
	c = 0, i = 0;


	freopen(IN_FILE, "r", stdin);
	freopen(OUT_FILE, "w", stdout);

	scanf("%d\n", &T);	//number of test cases

	for (cur_tc = 0; cur_tc < T; cur_tc++)
	{
		printf("Case #%d: ", cur_tc + 1);
		i = 0;
		do {
			result = scanf("%c", &c);
			if (result != 1)	//EOF
			{
				c = '\n';	
			}
			if (c == '+')
			{
				cakes[i] = 1;
			}
			else if (c == '-')
			{
				cakes[i] = 0;
			}

			i++;
		} while (c != '\n');
		

		printf("%d\n", solve(cakes, i-1));
		
	}
}

int solve(char* c, int size)
{
	int opp, i, flips; // opp = opposite :D
	opp = 0;
	flips = 0;
	i = size;

	do {
		if (opp == 0)		// if (-)0 is bad
		{
			if (c[i-1] == 0)
			{
				flips++;
				opp = 1;
			}
		}
		if (opp == 1)		// if (+)1 is bad
		{
			if (c[i-1] == 1)
			{
				flips++;
				opp = 0;
			}
		}
		i--;
	} while (i != 0);

	return flips;
}