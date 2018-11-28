#include <iostream>
#include <vector>
void solvecase(int caseNumber)
{
	int row; scanf_s("%d", &row);
	int card;
	
	std::vector<int> firstrow;

	for (auto i = 1; i <= 4; i++)
	for (auto j = 1; j <= 4; j++)
	{
		scanf_s(" %d", &card);
		if (i == row)
		{
			firstrow.push_back(card);
		}
		else
		{
			continue;
		}
	}
	//Second card showing
	int found = 0;
	scanf_s("%d", &row);
	for (auto i = 1; i <= 4; i++)
	for (auto j = 1; j <= 4; j++)
	{
		scanf_s("%d", &card);
		if (i == row)
		{
			if (std::find(firstrow.begin(), firstrow.end(), card) != firstrow.end())
			if (found == 0)
				found = card;
			else
				found = -1;
		}
		else
		{
			continue;
		}
	}

	switch (found)
	{
		case 0:  printf("Volunteer cheated!");  break;
		case -1: printf("Bad magician!"); break;
		default: printf("%d", found);
	}


}
int main() {
	int t; scanf_s("%d", &t);
	int counter = 0;
	while (t--)
	{
		printf("CASE #%d: ", ++counter);
		solvecase(counter);
		printf("\n");
	}
	return 0;
}