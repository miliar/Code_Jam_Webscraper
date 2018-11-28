#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	int k=1;
	while(t--)
	{
	int n;
	scanf("%d",&n);
	long double a[n+9];
	long double b[n+9];
	int i;
	for(i=0;i<n;i++)
	scanf("%Lf",&a[i]);
	sort(a,a+n);
	for(i=0;i<n;i++)
	scanf("%Lf",&b[i]);
	sort(b,b+n);
	int j=0;
	i=0;
	int ans1=0;
	int ans2=0;
	while(i<n && j<n)
	{
		if(a[i]>b[j])
		{
			i++;
			j++;
			ans1++;
		}
		else
		{
			i++;
		}
	}
	i=0;
	j=0;
	while(i<n && j<n)
	{
		if(a[i]<b[j])
		{
			ans2++;
			i++;
			j++;
		}
		else
		{
			j++;
		}
	}
	printf("Case #%d: %d %d\n",k++,ans1,n-ans2);
	}
	return 0;
}
