#include <stdio.h>

struct Test 
{
	int row[2];
	int number[2][4][4];
};

int main()
{
	int n;
	scanf("%d",&n);
	Test test[100];
	int result[100]={0};
	int j=0,i=0,m=0,o=0;
	for(j=0;j<n;j++)
	{
		while(i<2)
		{
			scanf("%d",&test[j].row[i]);
			for(m=0;m<4;m++)
				for(o=0;o<4;o++)
					scanf("%d",&test[j].number[i][m][o]);
			i++;
		}
		i=0;
		int row1 = test[j].row[0];
		int row2 = test[j].row[1];
		for(m=0;m<4;m++)
		{
			int one = test[j].number[0][row1-1][m];
			for(o=0;o<4;o++)
			{
				int two = test[j].number[1][row2-1][o];
				if(one == two)
				{
					if(!result[j])
						result[j] = one;
					else result[j] = -1;
				}

			}
		}

	}
	for(j=0;j<n;j++)
	{
		if (result[j] == 0)
		{
			printf("Case #%d: Volunteer cheated!\n",j+1);
		}else if (result[j] == -1)
		{
			printf("Case #%d: Bad magician!\n",j+1);
		}else
			printf("Case #%d: %d\n",j+1,result[j]);
	}

	getchar();
	getchar();
	return 0;
}
