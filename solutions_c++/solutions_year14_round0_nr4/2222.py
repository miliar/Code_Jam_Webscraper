#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int x,i,j,k,t,n,m;
	long double a[1001],b[1001],wa[1001],wb[1001];
	scanf("%d",&t);
	for(x=1;x<=t;++x)
	{
	scanf("%d",&n);
	for(i=0;i<n;++i)
		scanf("%Lf",&a[i]);
	for(i=0;i<n;++i)
		scanf("%Lf",&b[i]);
	int tmp=0,war=0,dpos,wtmp=0,dwar=0;
	//sorting
	sort(a,a+n);
	sort(b,b+n);
	//copying elements
	for(i=0;i<n;++i)
	{
		wa[i]=a[i];
		wb[i]=b[i];
	}/*
	printf("\n");
	for(i=0;i<n;++i)
	printf("%Lf ",a[i]);
	printf("\n");
	for(i=0;i<n;++i)
	printf("%Lf ",wa[i]);
	printf("\n");
	for(i=0;i<n;++i)
	printf("%Lf ",b[i]);
	printf("\n");
	for(i=0;i<n;++i)
	printf("%Lf ",wb[i]);*/
	//calculating optimal dwar score
	for(i=0;i<n;++i)
	for(j=0;j<n;++j)
	{
		if(wa[i]>wb[j] && wb[j]!=-1)
		{
			++wtmp;
			wb[j]=-1;
			break;
		}
	}
	dwar=wtmp;//optimal dwar score
	//calculating optimal war score
	for(i=n-1;i>=0;--i)
	for(j=0;j<n;++j)
	{
		if(b[j]>a[i] && b[j]!=-1)
		{
			++tmp;
			b[j]=-1;
			break;
		}
	}
	war=n-tmp;//optimal war score
	printf("Case #%d: %d %d\n",x,dwar,war);
	}
	return 0;
}