#include <iostream>
#include <stdio.h>
#include <set>
#include <string.h>
#include <algorithm>
using namespace std;
int n;
double a[1009],b[1009];
int cal(double a[],double b[])
{
	int u=0,d=0,ret=0;
	while(u<n&&d<n)
	{
		if(a[u]>b[d])
		{
			ret++;
			u++;
			d++;
		}else u++;
	}
	return ret;
}
int main()
{
	int ca;
	cin>>ca;
	//cout<<c<<endl;
	int cc=1;
	while(ca--)
	{
		printf("Case #%d: ",cc++);
		cin>>n;
		for(int i=0;i<n;i++) scanf("%lf",a+i);
		for(int i=0;i<n;i++) scanf("%lf",b+i);
		sort(a,a+n);
		sort(b,b+n);
		int a1=cal(a,b);
		int a2=n-cal(b,a);
		printf("%d %d\n",a1,a2);
	}
	return 0;
}
