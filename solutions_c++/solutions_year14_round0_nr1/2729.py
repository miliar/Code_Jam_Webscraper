#include <stdio.h>
#include <stdlib.h>

int test, tt, count[20];
int now, answer, i, j;

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--)
	{
		printf("Case #%d: ", ++tt);
		for (i = 1; i <= 16; i++)
			count[i] = 0;
		scanf("%d", &answer);
		for (i = 1; i <= 4; i++)
			for (j = 1; j <= 4; j++)
			{
				scanf("%d", &now);
				if (i == answer)
					count[now]++;
			}
		scanf("%d", &answer);
		for (i = 1; i <= 4; i++)
			for (j = 1; j <= 4; j++)
			{
				scanf("%d", &now);
				if (i == answer)
					count[now]++;
			}
		answer = 0;
		for (i = 1; i <= 16; i++)
			if (count[i] == 2)
			{
				if (answer == 0)
					answer = i;
				else
					answer = -1;
			}
		if (answer == 0)
			printf("Volunteer cheated!\n");
		else if (answer == -1)
			printf("Bad magician!\n");
		else
			printf("%d\n", answer);
	}
	
	return 0;
}
