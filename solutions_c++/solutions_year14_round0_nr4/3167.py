#include<stdio.h>
#include<stdlib.h>
int compare(const void *a,const void *b)
{
	double x = *(const double *)a - *(const double *)b ;
	if(x==0)
		return 0;
	if(x>0)
		return 1;
	return -1;
}
int main()
{
	int t,i,j,k,n,ans1,ans2;
	double a[1001],b[1001];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for(j=0;j<n;j++)
			scanf("%lf",&a[j]);
		for(j=0;j<n;j++)
			scanf("%lf",&b[j]);
		qsort(a,n,sizeof(double),compare);
		qsort(b,n,sizeof(double),compare);
		ans1=ans2=0;
		for(j=0,k=0;j<n&&k<n;k++)
		{
			if(a[j]<b[k])
				j++;
		}
		ans1=n-j;
		for(j=0,k=0;j<n&&k<n;j++)
		{
			if(a[j]>b[k])
			{
				k++;
				ans2++;
			}
		}
		printf("Case #%d: %d %d\n",i,ans2,ans1);
	}
}
