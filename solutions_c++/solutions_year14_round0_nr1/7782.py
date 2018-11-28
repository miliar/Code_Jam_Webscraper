#include<stdio.h>
bool chk[17];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, i, l, n, t, m, ans, f, j;
	scanf("%d", &T);
	for(l=1; l<=T; l++)
	{
		for(i=1; i<=16; i++) chk[i] = false;
		ans = -1;
		f = 0;

		scanf("%d", &m);
		for(i=1; i<=4; i++)for(j=0; j<4; j++)
		{
			if(i==m)
			{
				scanf("%d", &t);
				chk[t] = true;
			}
			else scanf("%*d");
		}

		scanf("%d", &m);
		for(i=1; i<=4; i++)for(j=0; j<4; j++)
		{
			if(i==m)
			{
				scanf("%d", &t);
				if(chk[t])
				{
					if(ans == -1)
					{
						ans = t;
					}
					else f=1;
				}
			}
			else scanf("%*d");
		}

		if(ans == -1) f = -1;

		printf("Case #%d: ", l);
		if(f==0)
		{
			printf("%d\n", ans);
		}
		else if(f==1)
			printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	return 0;
}