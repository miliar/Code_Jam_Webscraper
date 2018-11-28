#include <cstdio>
#include <vector>

int main()
{
	int caseNum = 0;
	scanf("%d", &caseNum);
	for (int caseIndex = 0; caseIndex < caseNum; caseIndex++)
	{
		int answer1 = 0;
		scanf("%d", &answer1);
		answer1--;
		int cards[4][4];
		std::vector<int> list;

		for (int lineIndex = 0; lineIndex < 4; lineIndex++)
		{
			scanf("%d %d %d %d", &cards[lineIndex][0], &cards[lineIndex][1], &cards[lineIndex][2], &cards[lineIndex][3]);
		}

		for (int cardIndex = 0; cardIndex < 4; cardIndex++)
		{
			list.push_back(cards[answer1][cardIndex]);
		}

		int answer2 = 0;
		scanf("%d", &answer2);
		answer2--;
		for (int lineIndex = 0; lineIndex < 4; lineIndex++)
		{
			scanf("%d %d %d %d", &cards[lineIndex][0], &cards[lineIndex][1], &cards[lineIndex][2], &cards[lineIndex][3]);
		}

		std::vector<int> result;
		for (int cardIndex = 0; cardIndex < 4; cardIndex++)
		{
			if (find(list.begin(), list.end(), cards[answer2][cardIndex]) != list.end())
			{
				result.push_back(cards[answer2][cardIndex]);
			}
		}

		if (result.size() == 1)
		{
			printf("Case #%d: %d\n", caseIndex + 1, result[0]);
		}
		else if (result.size() == 0)
		{
			printf("Case #%d: Volunteer cheated!\n", caseIndex + 1);
		}
		else
		{
			printf("Case #%d: Bad magician!\n", caseIndex + 1);
		}
	}

	return 0;
}
