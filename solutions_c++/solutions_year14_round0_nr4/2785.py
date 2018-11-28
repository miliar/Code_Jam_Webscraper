#include<stdio.h>
#include<algorithm>

double a[2000],b[2000];
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.txt","w",stdout);
	int runtime, n;
	scanf("%d",&runtime);
	for (int run = 1; run <= runtime; run++)
	{
		int ans1 = 0, ans2 = 0;
		scanf("%d",&n);
		for (int i = 0; i < n; i++) scanf("%lf",&a[i]); 
		std::sort(a,a+n);
		for (int i = 0; i < n; i++) scanf("%lf",&b[i]); 
		std::sort(b,b+n);
		
		int h = 0;
		for (int i = 0; i < n; i++)
			if (a[i] > b[h])
			{
				ans1++;
				h++;
			}
		
		h = 0;
		for (int i = 0; i < n; i++)
		{
			while ((a[i] > b[h]) && (h + 1 < n)) h++;
			if ((a[i] < b[h]) && (h < n))
			{
				ans2++;
				h++;
			}
		}
		ans2 = n - ans2;

		printf("Case #%d: %d %d\n",run,ans1,ans2);
	}
}
