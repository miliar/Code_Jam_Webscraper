#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int p=0;p<t;p++)
	{
		int n;
		scanf("%d",&n);
		int abeg=0,aend=n-1,bbeg=0,bend=n-1;
		double  a[20],b[20];
		for(int i=0;i<n;i++)
			scanf("%lf",&a[i]);
		sort(a,a+n);
		for(int j=0;j<n;j++)
			scanf("%lf",&b[j]);
		sort(b,b+n);
		int ans1=0,ans2=0;
		for(int i=0;i<n;i++)
		{
			if(b[bend]>a[aend])
			{
				bend--;
				aend--;
			}
			else
			{
				ans1++;
				aend--;
				bbeg--;
			}
		}
		abeg=0;
		aend=n-1;
		bbeg=0;
		bend=n-1;
		int boolean[20]={0};
		for(int i=0;i<n;i++)
		{
			int temp=n;
			for(int j=0;j<n;j++)
			{
				if(boolean[j]==0&&a[j]>b[bend])
				{
					temp=j;
					break;
				}
			}
			if(temp==n)
			{
				bend--;
				boolean[abeg]=1;
				abeg++;
			}
			else
			{
				ans2++;
				bend--;
				boolean[temp]=1;
			}
		}
		printf("Case #%d: %d %d\n",p,ans2,ans1);
	}
	return 0;
}
