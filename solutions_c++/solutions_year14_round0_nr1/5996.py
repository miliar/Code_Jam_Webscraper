#include <stdio.h>

int main()
{
	int t;
	scanf("%d", &t);

	for(int nc=1; nc<=t; nc++)
	{
		int fa, sa;
		int matriz1[4][4];
		int matriz2[4][4];
		int resp[4];

		for(int i=0; i<4; i++)
			resp[i] = 0;

		scanf("%d", &fa);
		fa=fa-1;;

		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d", &matriz1[i][j]);


		//for(int i=0; i<4; i++)
		//{
		//	for(int j=0; j<4; j++)
		//		printf("%d ", matriz1[i][j]);
		//	printf("\n");
		//}

		scanf("%d", &sa);
		sa = sa-1;

		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf("%d", &matriz2[i][j]);

		
		//for(int i=0; i<4; i++)
		//{
		//	for(int j=0; j<4; j++)
		//		printf("%d ", matriz2[i][j]);
		//	printf("\n");
		//
		//}
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				if(matriz1[fa][i]==matriz2[sa][j])
					resp[i] = matriz1[fa][i];
			}
		}

		int count = 0;
		int a=5;
		for(int i=0; i<4; i++)
		{
			if(resp[i]!=0)
			{
				count++;
				a = i;
			}
			if(count>=2)
			{
				count = 5;
				i = 5;
			}
		}
		if(count==1)
			printf("Case #%d: %d\n", nc, resp[a]);
		else if(count==5)
			printf("Case #%d: Bad magician!\n", nc);
		else
			printf("Case #%d: Volunteer cheated!\n", nc);


	}
}
