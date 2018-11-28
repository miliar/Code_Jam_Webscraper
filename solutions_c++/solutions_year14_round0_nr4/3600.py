#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int t, n, i, j, na, k, ans1, ans2;
	scanf("%d", &t);
	for(i=1; i<=t; i++)
	{
		scanf("%d", &n);
		double naomi[1002], ken[1002];
		for(j=0; j<n; j++) scanf("%lf", &naomi[j]);
		sort(naomi, naomi+n);
		for(j=0; j<n; j++) scanf("%lf", &ken[j]);
		sort(ken, ken+n);
		printf("Case #%d: ", i);

		na=0;
		k=0;
		ans1=0;
		while(na<n)
		{
			if(naomi[na]>ken[k])
			{
				ans1++;
				k++;
			}
			na++;
		}
		printf("%d ", ans1);

		na=n-1;
		k=n-1;
		ans2=0;
		while(na>=0)
		{
			if(naomi[na]>ken[k]) ans2++;
			else k--;
			na--;
			
		}
		printf("%d\n", ans2);
	}

	return 0;
}
