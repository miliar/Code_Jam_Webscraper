// Google Code Jam 2014
// Author: Avaneesh Rastogi
// Date: 12-04-2014

#include<cstdio>
#define debug printf("DEBUG: On Line #: %d\n", __LINE__);
int main ()
{
	int t, c = 1;
	scanf("%d", &t);
	while (t--)
	{
		int n, m, N[4][4], M[4][4], i, j, k;
		scanf("%d", &n);
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
				scanf("%d", &N[i][j]);
		scanf("%d", &m);
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
				scanf("%d", &M[i][j]);
		
		int ans = 0, first = 0;
		for (i=0;i<4;i++)
			for (j=0;j<4;j++)
				if (N[n-1][i] == M[m-1][j])
				{
					if (ans == 0) 
						first = N[n-1][i];
					ans++;
				}
					
		if (ans == 0)
			printf("Case #%d: Volunteer cheated!\n", c++);
		else if (ans > 1)
			printf("Case #%d: Bad magician!\n", c++);
		else
			printf("Case #%d: %d\n", c++, first);
	}	
	
	return 0;
}
