#include <stdio.h>

#define MAX 110

int main()
{
	int t;

	scanf("%d",&t);
	for(int ccnt=1; ccnt<=t; ++ccnt)
	{
		int rmax[MAX];
		int cmax[MAX];
		int tab[MAX][MAX];

		int n,m;

		scanf("%d %d",&n,&m);
		for(int i=0; i<n; ++i)
			rmax[i] = -1;
		for(int j=0; j<m; ++j)
			cmax[j] = -1;

		for(int i=0; i<n; ++i)
			for(int j=0; j<m; ++j)
			{
				scanf("%d",&tab[i][j]);

				if(tab[i][j] > rmax[i])
					rmax[i] = tab[i][j];

				if(tab[i][j] > cmax[j])
					cmax[j] = tab[i][j];
			}

		bool fail = false;

		for(int i=0; i<n; ++i)
			for(int j=0; j<m; ++j)
				if(tab[i][j] < rmax[i] && tab[i][j] < cmax[j])
					fail = true;

		printf("Case #%d: ",ccnt);
		if(fail)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}


