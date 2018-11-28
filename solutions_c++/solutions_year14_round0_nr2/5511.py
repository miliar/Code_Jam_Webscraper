#include <stdio.h>
#include <string.h>
int main()
{
	int t, test=0;
	double c, f, x, ans, beg, p, sum;
	freopen("B-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",++test);
		scanf("%lf%lf%lf",&c,&f,&x);
		if( c >= x)
		{
			printf("%.7lf\n",x/2.0);
			continue;
		}
		ans = x/2.0;
		beg = 0;
		p = 2;

		while(1)
		{
			beg += c/p;
			p += f;
			sum = beg + x/p;
			if( sum > ans)
				break;
			ans = sum;
		}
		printf("%.7lf\n",ans);

	}
//	while(1);
	return 0;
}