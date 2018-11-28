#include<cstdio>
#include<cstdlib>
int main()
{
	int square[4][4];
	int cases;
	int row_1, row_2;
	int susp[4];
	int ans;
	int count;
	scanf("%d", &cases);
	for(int a = 1; a <= cases; a++)
	{
		count = 0;
		ans = 0;
		scanf("%d", &row_1);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &square[i][j]);
		for(int i = 0; i < 4; i++)
			susp[i] = square[row_1-1][i];
		scanf("%d", &row_2);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &square[i][j]);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				if(susp[i] == square[row_2-1][j])
				{
					ans = susp[i];
					count++;
				}
		if(count == 0)
			printf("Case #%d: Volunteer cheated!\n", a);
		else if(count > 1)
			printf("Case #%d: Bad magician!\n", a);
		else
			printf("Case #%d: %d\n", a, ans);
	}
	return 0;
}
