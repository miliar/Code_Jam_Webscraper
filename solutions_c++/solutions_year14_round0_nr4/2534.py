#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

double a[1005],b[1005];
int n,ans1,ans2;

int main()
{
	int T,R=0;
	scanf("%d",&T);
	while(T--)
	{
		R++;
		scanf("%d",&n);
		int i,j;
		for(i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		ans1=ans2=0;
		j=0;
		for(i=0;i<n;i++)
		{
			for(;j<n;j++)
				if(a[j]>b[i])
				{
					ans1++;
					j++;
					break;
				}
		}
		j=0;
		for(i=0;i<n;i++)
		{
			for(;j<n;j++)
				if(b[j]>a[i])
				{
					ans2++;
					j++;
					break;
				}
		}
		ans2=n-ans2;
		printf("Case #%d: %d %d\n",R,ans1,ans2);
	}
	return 0;
}
