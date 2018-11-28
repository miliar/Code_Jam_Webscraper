#include<stdio.h>

void solve(int caseno)
{
	int cards[17] = {0,};
	int cardset[4][4] = {0,};
	int rowno = 0;
	int i, j;
	scanf("%d", &rowno);
	for(i = 0; i < 4; i++)
		for(j = 0; j < 4; j++)
			scanf("%d", &cardset[i][j]);
	for(j = 0; j < 4; j++)
		cards[cardset[rowno-1][j]]++;
	scanf("%d", &rowno);
	for(i = 0; i < 4; i++)
		for(j = 0; j < 4; j++)
			scanf("%d", &cardset[i][j]);
	for(j = 0; j < 4; j++)
		cards[cardset[rowno-1][j]]++;
	j = 0;
	for(i = 1; i<17; i++)
	{
		if(cards[i] > 1)
		{
			rowno = i;
			j++;
		}
	}
	if(j == 0)
		printf("Case #%d: Volunteer cheated!\n", caseno);
	else if(j == 1)
		printf("Case #%d: %d\n", caseno, rowno);
	else
		printf("Case #%d: Bad magician!\n", caseno);
}

int main()
{
	int t = 0;
	scanf("%d", &t);
	for(int i = 0; i<t; i++)
		solve(i+1);
	return 0;
}