#include <iostream>
#include <cstring>
#include <cstdio>







int main()
{	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, j, n, s, k, x1, x2, a1[5], a2[5], t;

	scanf("%d", &n);
	for (k=1; k<=n; ++k)
	{
		
		scanf("%d", &x1);
		for (i=1; i<=4; ++i)
		{
			if (i==x1)
				scanf("%d%d%d%d", &a1[1], &a1[2], &a1[3], &a1[4]);
			else scanf("%d%d%d%d", &t, &t, &t, &t);
		}

		scanf("%d", &x2);
		for (i=1; i<=4; ++i)
		{
			if (i==x2)
				scanf("%d%d%d%d", &a2[1], &a2[2], &a2[3], &a2[4]);
			else scanf("%d%d%d%d", &t, &t, &t, &t);
		}

		s=0;
		for (i=1;i<=4;++i)
			for (j=1;j<=4;++j)
				if (a1[i]==a2[j])
				{
					++s;
					t=a1[i];
				}

		if (s==0)
			printf("Case #%d: Volunteer cheated!\n", k);
		else if (s==1)
			printf("Case #%d: %d\n", k, t);
		else printf("Case #%d: Bad magician!\n", k);



	}
	
	return 0;
}