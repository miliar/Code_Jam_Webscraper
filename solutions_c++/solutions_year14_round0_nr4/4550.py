#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("outsmall0.txt", "w", stdout);
	unsigned short t,t1,ans1,ans2,n,i,j;
	float a[1000],b[1000];				//a is niomi b is ken
	scanf("%hu",&t1);
	for(t=1;t<=t1;t++)
	{
		scanf("%hu",&n);
		ans2=n;
		ans1=0;
		for(i=0;i<n;i++)
			scanf("%f",&a[i]);
		for(i=0;i<n;i++)
			scanf("%f",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		j=0;
		for(i=0;i<n;i++)
			while(j<n)
			{
                if(b[j]>a[i])
				{
					ans2--;
					j++;
					break;
				}
				j++;
			}
        j=0;
		for(i=0;i<n;i++)
			while(j<n)
			{
                if(a[j]>b[i])
				{
					ans1++;
					j++;
					break;
				}
				j++;
			}
		printf("Case #%hu: %hu %hu\n",t,ans1,ans2);
	}
	return 0;
}
