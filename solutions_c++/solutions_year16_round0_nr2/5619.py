// ProblemB.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string.h>


int main()
{
	int T;
	int N;
	char S[101];
	char currSymbol;
	char prevSymbol;
	int flipCount;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		scanf("%s", S);
		N = strlen(S);
		prevSymbol = '*';
		flipCount = 0;
		for (int j = N - 1; j >= 0; j--)
		{
			if (prevSymbol != S[j])
			{
				++flipCount;
				prevSymbol = S[j];
			}
		}
		if (S[N - 1] == '+')
			--flipCount;
		printf("Case #%d: %d\n", i + 1, flipCount);
	}
    return 0;
}

