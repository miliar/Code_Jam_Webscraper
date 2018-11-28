#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;
#define MAX_LENGTH 1000

int main()
{
	int t, i, k, l, count;
	bool possible;
	char p[MAX_LENGTH+1] = {};
	scanf("%d\n", &t);
	for(i=1;i<=t;i++)
	{
		scanf("%s %d", p, &k);

		possible = true;
		count = 0;
		l = strlen(p);
		for(int j = 0; j < l-k+1; j++)
		{
			if(p[j] == '-')
			{
				for(int m = j; m < j+k; m++)
				{
					if(p[m] == '+')
						p[m] = '-';
					else
						p[m] = '+';
				}
				count++;
			}
		}
		for(int j = l-k+1; j < l; j++)
			if(p[j] == '-')
			{
				possible = false;
				break;
			}

		printf("Case #%d: ", i);
		if(possible)
			printf("%d", count);
		else
			printf("IMPOSSIBLE");
		printf("\n");
	}

	return 0;
}
