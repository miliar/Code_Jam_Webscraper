#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define INF 1000000000

main()
{
 	freopen("B-large.in","r",stdin);
	freopen("xxx.out","w",stdout);
	int t;
	double c,f,x;
	int i;
	int tcase=1;
	
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		double ans=x/2.0;
		
		for(i=1;;i++)
		{
			if(ans - x/(2+(i-1)*f) + c/(2+(i-1)*f) + x/(2+i*f) > ans) break;
			else ans = ans - x/(2+(i-1)*f) + c/(2+(i-1)*f) + x/(2+i*f);
		}
		printf("Case #%d: ",tcase++);
		printf("%.7lf\n",ans);
	}
}

