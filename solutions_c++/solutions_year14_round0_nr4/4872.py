#include <iostream>
#include<algorithm>
using namespace std;
int main()
{	int t,n,i,j,p,s,o,flag;
	double a[1010],b[1010];
	scanf("%d",&t);
	for(o=1;o<=t;o++)
	{	scanf("%d",&n);
		for(j=0;j<n;j++)
			scanf("%lf",&a[j]);
		for(j=0;j<n;j++)
			scanf("%lf",&b[j]);
		sort(a,a+n);
		sort(b,b+n);
		flag=0;
		for(i=0,j=0;i<n && j<n;)
		{	if(a[i]<b[j])
			{	i++;
				j++;
				flag++;
			}
			else
			{	j++;
			}
		}
		p=n-flag;
		flag=0;
		for(i=0,j=0;i<n && j<n;)
		{	if(b[j]<a[i])
			{	i++;
				j++;
				flag++;
			}
			else
			{	i++;
			}
		}
		s=flag;
		printf("Case #%d: %d %d\n",o,s,p);
	}
	return 0;
}