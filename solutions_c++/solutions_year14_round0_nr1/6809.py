#include <cstdio>
#include <cstring>

using namespace std;

bool firstRow[16], secondRow[16];

void readCards(bool *row)
{
	memset(row, 0, sizeof(bool) * 16);

	int ans;
	scanf("%d", &ans);
	for (int i = 1; i <= 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			int card;
			scanf("%d", &card);
			if(i == ans)
			{
				row[card - 1] = true;
			}
		}
	}
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("magic.out", "w", stdout);

	int casesCount;
	scanf("%d", &casesCount);

	for (int currentCase = 1; currentCase <= casesCount; currentCase++)
	{
		readCards(firstRow);
		readCards(secondRow);

		int sol = -1;
		for (int i = 0; i < 16; i++)
		{
			if(firstRow[i] && secondRow[i])
			{
				sol = (sol == -1) ? i + 1 : -2;
			}
		}

		printf("Case #%d: ", currentCase);
		if(sol == -1)
		{
			printf("Volunteer cheated!");
		}
		else if(sol == -2)
		{
			printf("Bad magician!");
		}
		else
		{
			printf("%d", sol);
		}
		printf("\n");
	}

	return 0;
}