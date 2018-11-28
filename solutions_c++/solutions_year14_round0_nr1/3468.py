#include <iostream>
#include <cstdio>

using namespace std;

int h[17];

int main()
{
	int tc, t, i, j, r1, r2, a[5][5], b[5][5], f1, f2, card;

	scanf("%d",&tc);

	for(t=1; t<=tc; t++)
	{
		scanf("%d",&r1);
		for(i=1; i<=4; i++)
		{
			for(j=1; j<=4; j++)
			{
				scanf("%d",&a[i][j]);
			}
		}

		scanf("%d",&r2);
		for(i=1; i<=4; i++)
		{
			for(j=1; j<=4; j++)
			{
				scanf("%d",&b[i][j]);
			}
		}

		f1=f2=0;
		for(i=0; i<=16; i++)
			h[i]=0;
		
		for(i=1; i<=4; i++)
			h[a[r1][i]]++;

		for(i=1; i<=4; i++)
		{
			if(h[b[r2][i]])
			{
				if(!f1) {
					f1=1;
					card = b[r2][i];
				}
				else
				{
					f2=1;
					break;
				}
			}
		}

		if(f1 && !f2)
			printf("Case #%d: %d\n",t,card);
		else if(f2)
			printf("Case #%d: Bad magician!\n",t);
		else if(!f1 && !f2)
			printf("Case #%d: Volunteer cheated!\n",t);

	}

	return 0;
}