#include <stdio.h>
int T;
int a[5][5],b[5][5];

int main(int argc, char *argv[])
{
	scanf("%d",&T);
	int cases = 1;
	while (cases<=T)
	{
		
		int m,n;
		scanf("%d",&m);
		for (int i=1; i<5; i++)
		{
			for (int j=1; j<5; j++)
			{
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&n);
		for (int i=1; i<5; i++)
		{
			for (int j=1; j<5; j++)
			{
				scanf("%d",&b[i][j]);
			}
		}
		int count=0,num=0;
		for (int i=1; i<5; i++)
		{
			for (int j=1; j<5; j++)
			{
				if (a[m][i]==b[n][j])
				{
					count++;
					num = a[m][i];
				}
			}
		}
		if (count==0) printf("Case #%d: Volunteer cheated!\n",cases);
		else if (count==1) printf("Case #%d: %d\n",cases,num);
		else  printf("Case #%d: Bad magician!\n",cases);
		cases++;
	}
	
	return 0;
}
