#include <stdio.h>

int main()
{
	int testN;
	scanf_s("%d", &testN);

	for (int test = 1; test <= testN; ++test)
	{
		int result = 0;
		int currentStandPeople = 0;
		int sMax = 0;
		char check;

		scanf_s("%d", &sMax);

		// 0번째 사람 체크
		if (getchar() == '0')
		{
			++result;
			++currentStandPeople;
		}

		for (int i = 1; i <= sMax; ++i)
		{
			check = getchar();
			if (check == '0')
			{
				if (currentStandPeople < i)
				{
					++currentStandPeople;
					++result;
				}
			}
			else
			{
				currentStandPeople += check - '0';
			}
		}

		getchar();

		printf("Case #%d: %d\n", test, result);
	}
}