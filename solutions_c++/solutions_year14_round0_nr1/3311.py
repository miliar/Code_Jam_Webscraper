//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int t;
int rowA, rowB;
int tabA[5][5];
int tabB[5][5];

int wyncnt, wyn;

int main()
{
	scanf("%d", &t);
	for(int ti = 1;ti <= t;ti++)
	{
		wyncnt = wyn = 0;

		scanf("%d", &rowA);
		for(int i = 1;i <= 4;i++)
			for(int j = 1;j <= 4;j++)
				scanf("%d", &tabA[i][j]);
		scanf("%d", &rowB);
		for(int i = 1;i <= 4;i++)
			for(int j = 1;j <= 4;j++)
				scanf("%d", &tabB[i][j]);
		for(int num = 1;num <= 16;num++)
		{
			int tak = 0;
			for(int i = 1;i <= 4;i++)
				if(tabA[rowA][i] == num)
				{
					tak++;
					break;
				}
			for(int i = 1;i <= 4;i++)
				if(tabB[rowB][i] == num)
				{
					tak++;
					break;
				}

			if(tak == 2)
			{
				wyncnt++;
				wyn = num;
			}
		}

		printf("Case #%d: ", ti);
		if(wyncnt == 0) printf("Volunteer cheated!");
		else if(wyncnt >= 2) printf("Bad magician!");
		else printf("%d", wyn);
		printf("\n");
	}

	return 0;
}
