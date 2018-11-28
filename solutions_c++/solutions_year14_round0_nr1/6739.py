#include <stdio.h>
#include <vector>
using namespace std;

void main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int chose[2];
	int deck1[4][4];
	int deck2[4][4];
	scanf("%d", &T);
	int number_card = 0;
	for (int i=0; i<T; i++)
	{
		int count = 0;
		scanf("%d", &chose[0]);
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				scanf("%d", &deck1[j][k]);
			}
		}
		scanf("%d", &chose[1]);
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				scanf("%d", &deck2[j][k]);
			}
		}
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (deck1[chose[0] - 1][j] == deck2[chose[1] - 1][k])
				{
					count++;
					number_card = deck1[chose[0] - 1][j];
				}
			}
		}
		switch (count)
		{
			case 0: 
				printf("Case #%d: Volunteer cheated!\n",i+1);
				break;
			case 1:
				printf("Case #%d: %d\n",i+1,number_card);
				break;
			default:
				printf("Case #%d: Bad magician!\n", i+1);
		}
	}
}