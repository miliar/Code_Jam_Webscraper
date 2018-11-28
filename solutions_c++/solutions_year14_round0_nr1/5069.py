#include <stdio.h>

int main(void) {
	// your code goes here
	int _T = 0, idx = 0, nAS1 = 0, nAS2 = 0;
	int arrange1[4][4];
	int arrange2[4][4];
	scanf("%d", &_T);
	while(idx < _T)
	{
		scanf("%d", &nAS1);
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				scanf("%d", &(arrange1[i][j]));
			}
		}
		scanf("%d", &nAS2);
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				scanf("%d", &(arrange2[i][j]));
			}
		}
		nAS1--;	nAS2--;
		int num = 0;
		int ret = 0;
		for(int i = 0; i < 4 && num < 2; i++)
		{
			for(int j = 0; j < 4 && num < 2; j++)
			{
				if(arrange1[nAS1][i] == arrange2[nAS2][j])
				{
					num++;
					ret = arrange1[nAS1][i];
				}
			}
		}
		printf("Case #%d: ", ++idx);
		switch(num)
		{
			case 0:
			{
				printf("Volunteer cheated!\n");
				break;
			}
			case 1:
			{
				printf("%d\n", ret);
				break;
			}
			case 2:
			{
				printf("Bad magician!\n");
				break;
			}
			default:
				break;
		}
	}
	return 0;
}
