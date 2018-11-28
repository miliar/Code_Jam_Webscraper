#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <string.h>

using namespace std;

int mat[5][5];
int num[20];

int main (void)
{
	freopen("D:\\A-small-attempt0.in", "r", stdin);
	freopen("D:\\out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int ca = 0;
	while(t--)
	{
		int row;
		memset(num, 0, sizeof(num));
		scanf("%d", &row);
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				scanf("%d", &mat[i][j]);
				if(i == row - 1)
				{
					num[mat[i][j]]++;
				}
			}
		}
		scanf("%d", &row);
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				scanf("%d", &mat[i][j]);
				if(i == row - 1)
				{
					num[mat[i][j]]++;
				}
			}
		}
		int flag = 0;
		int ans = -1;
		for(int i = 1; i <= 16; ++i)
		{
			if(num[i] >= 2)
			{
				flag++;
				ans = i;
			}
		}
		printf("Case #%d: ", ++ca);
		if(!flag)
			printf("Volunteer cheated!");
		else if(flag == 1)
			printf("%d", ans);
		else
			printf("Bad magician!");
		printf("\n");
	}
	return 0;
}