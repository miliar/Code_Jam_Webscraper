#include <cstdio>

int main()
{
	int t,r1,r2,c1[4][4],c2[4][4],ans;
	scanf("%i",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&r1);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&c1[j][k]);
		scanf("%d",&r2);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&c2[j][k]);
		bool b=0,bad=0;
		r1--;
		r2--;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				if(c1[r1][j]==c2[r2][k])
					if (not(b))
					{ 
						ans=c1[r1][j];
						b=1;
					}
					else if (b) 
					{
						printf("Case #%d: Bad Magician!\n",i);
						bad=1;
						j=4;
						k=4;
					}

		if (not(b)) printf("Case #%d: Volunteer cheated!\n",i);
		else if ((b)&&not(bad)) printf("Case #%d: %d\n",i,ans); 

	}
	return 0;

}
