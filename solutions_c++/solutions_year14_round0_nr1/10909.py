#include <stdio.h>

int main()
{
	int m1[5][5];
	int m2[5][5];
	int casos, f,c;
	scanf("%d",&casos);
	int cs=1;
	while(casos--)
	{
		printf("Case #%d: ",cs++);
		scanf("%d",&f);

		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&m1[i][j]);
		scanf("%d",&c);
		f--;
		c--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&m2[i][j]);
		int coin=0;
		int ans=0;
		for(int i=0; i<4;i++)
			for(int j=0;j<4;j++)
				if(m1[f][i]==m2[c][j])
				{
					coin++;
					ans=m1[f][i];
				}
		if(!coin)
			printf("Volunteer cheated!\n");
		else
			if(coin==1)
				printf("%d\n",ans);
			else
				printf("Bad magician!\n");
	}
	return 0;
}