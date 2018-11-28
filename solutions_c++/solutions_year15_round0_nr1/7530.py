#include "stdio.h"
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	
	for(int t = 1; t <= T; t++)
	{
		int Smax;
		scanf("%d", &Smax);

		char S[1002];
		scanf("%s", S);

		int shyPeopleCount = 0, toAdd = 0;
		for(int i = 0; i <= Smax; i++)
		{
			if(shyPeopleCount < i)
			{
				toAdd++;
				shyPeopleCount++;
			}
			shyPeopleCount += (S[i] - '0');
		}

		printf("Case #%d: %d\n", t, toAdd);
	}

	return 0;
}
