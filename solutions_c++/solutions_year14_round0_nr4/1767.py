#include <stdio.h>
#include <stdlib.h>

double naomi[1005];
double ken[1005];

int cmp(const void *p1, const void *p2)
{
	return *((double *)p1) > *((double *)p2) ? 1 : -1;
}

int main()
{
	//freopen("D-large.in", "r", stdin);
	//freopen("D-l.out", "w", stdout);

	int t, cas;
	int n, i, j;
	int s1, s2;
	
	scanf("%d", &t);
	for(cas=1; cas<=t; cas++)
	{
		scanf("%d", &n);
		for(i=0; i<n; i++)
			scanf("%lf", naomi+i);
		for(i=0; i<n; i++)
			scanf("%lf", ken+i);
		qsort(naomi, n, sizeof(double), cmp);
		qsort(ken, n, sizeof(double), cmp);

		s1=0;
		for(i=0, j=0; i<n; i++)
			if(naomi[i]>ken[j])
			{
				s1++;
				j++;
			}

		for(i=0, j=0; j<n; j++)
			if(naomi[i]<ken[j]) i++;
		s2=n-i;
			
		printf("Case #%d: %d %d\n", cas, s1, s2);
	}
}