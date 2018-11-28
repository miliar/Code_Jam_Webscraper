#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,k,n,i,p;
	scanf("%d",&t);
	for(p=1;p<=t;p++)
	{
		scanf("%d",&n);
		int max=0,min=0,j;
		double a[n];
		double b[n];
		double c[n];
		for(i=0;i<n;i++)
		{
			scanf("%lf",&a[i]);
		}
		sort(a,a+n);
		for(i=0;i<n;i++)
		{
			scanf("%lf",&b[i]);
			c[i]=b[i];
		}
		sort(b,b+n);
		/*for(i=0;i<n;i++)
		{
			printf("%lf ",a[i]);
		}
		printf("\n");
		for(i=0;i<n;i++)
		{
			printf("%lf ",b[i]);
		}
		printf("\n");*/
		int k=n;
		for(i=(n-1);i>=0;i--)
		{	
			for(j=(k-1);j>=0;j--)
			{
				if(a[i] >= b[j])
				{
					max++;
					b[j]=10000;
					//printf("%d %d %d\n",max,i,j);
					break;
				}	
			}
			
		}
		k=n;
		//printf("%d\n",max);	
		for(i=(n-1);i>=0;i--)
		{	
			for(j=(k-1);j>=0;j--)
			{
				if(a[i] < c[j])
				{
					min++;
					c[j]=0;
					//printf("%d %d %d\n",min,i,j);
					break;
				}	
			}
		}
		printf("Case #%d: %d %d\n",p,max,(n-min));	
		}
	return 0;
}
