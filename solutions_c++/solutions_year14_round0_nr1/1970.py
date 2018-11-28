#include <stdio.h>

int main()
{
	/*freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);*/

	int t, cas;
	int n1, n2, i, j, s, m;
	int c1[5][5], c2[5][5];

	scanf("%d", &t);
	for(cas=1; cas<=t; cas++)
	{
		scanf("%d", &n1);
		for(i=1; i<=4; i++)
			for(j=1; j<=4; j++)
				scanf("%d", &c1[i][j]);
		scanf("%d", &n2);
		for(i=1; i<=4; i++)
			for(j=1; j<=4; j++)
				scanf("%d", &c2[i][j]);

		printf("Case #%d: ", cas);

		s=0;
		for(i=1; i<=4; i++)
			for(j=1; j<=4; j++)
			{
				if(c1[n1][i]==c2[n2][j])
				{
					m=c1[n1][i];
					s++;
				}
			}
		if(s>1) printf("Bad magician!\n");
		else if(s==0) printf("Volunteer cheated!\n");
		else printf("%d\n", m);
	}

	return 0;
}