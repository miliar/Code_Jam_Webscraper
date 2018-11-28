#include <stdio.h>
#include <vector>
int main()
{
	int T;
	int row[2], card[2][4][4];
	std::vector<int> magic;
	scanf("%d", &T);
	for(int caseNum = 1; caseNum <= T; caseNum++)
	{
		for(int i = 0; i < 2; i++)
		{
			scanf("%d", &row[i]);
			row[i]--;
			for(int j = 0; j < 4; j++)
				for(int k = 0; k < 4; k++)
					scanf("%d", &card[i][j][k]);
		}
		magic.clear();
		for(int i = 0; i < 4; i++)
		{
			int tmp = card[0][row[0]][i];
			for(int j = 0; j < 4; j++)
				if(card[1][row[1]][j] == tmp)
					magic.push_back(tmp);
		}
		printf("Case #%d: ", caseNum);
		if(magic.size() == 0)
			puts("Volunteer cheated!");
		else if(magic.size() == 1)
			printf("%d\n", magic[0]);
		else
			puts("Bad magician!");
	}
}