// Google Code Jam 2014
// Author: Avaneesh Rastogi
// Date: 12-04-2014

#include<cstdio>
#include<algorithm>
#include<cstdlib>
using namespace std;
#define debug printf("DEBUG: On Line #: %d\n", __LINE__);

int main()
{
	int t, caseno = 1, i, j, k;
	scanf("%d", &t);
	double naomi[1001], ken[1001];
	while (t--)
	{
		int N, war=0, dwar=0;
		scanf("%d", &N);
		for (i=0;i<N;i++)
			scanf("%lf", &naomi[i]);
		for (i=0;i<N;i++)
			scanf("%lf", &ken[i]);
		
		sort(naomi, naomi+N);
		sort(ken, ken+N);
		
		i = 0; 
		j = 0;
		while(i<N)
		{
			while(j<N && ken[j]<naomi[i])
				j++;
			if (j==N)
				break;
			war++;
			i++;
			j++; 
		}
		
		j = N-1;
		for (i=N-1;i>=0;i--)
		{
			while(j>=0 && ken[j]>naomi[i])
				j--;
			if (j==-1)
				break;
			dwar++;
			j--; 
			
		}
		
		printf("Case #%d: %d %d\n",caseno++, dwar, N-war);
	}	
	
	return 0;
}
