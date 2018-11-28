#include<stdio.h>

int num[100];

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int runtime;
	scanf("%d",&runtime);
	for (int run = 1; run <= runtime; run++)
	{
		int ans = 0, tmp = 0;
		for (int i = 1; i <=16; i++) num[i] = 0;
		for (int count = 1; count <= 2; count++)
		{
			scanf("%d",&ans);
			for (int i = 1; i <= 4; i++)
				for (int j = 1; j <=4; j++)
				{
					scanf("%d",&tmp);
					if (i == ans) num[tmp]++;
				}
		}
		int numans = 0;
		for (int i = 1; i <= 16; i++)
			if (num[i] == 2)
			{
				ans = i;
				numans++;
			}
		printf("Case #%d: ",run);
		if (numans == 0) printf("Volunteer cheated!\n");
		else if (numans == 1) printf("%d\n",ans);
		else if (numans >= 2) printf("Bad magician!\n");
	}
}
