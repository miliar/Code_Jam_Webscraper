#include<stdio.h>
#include<iostream>

using namespace std;
	
double c,f,x;
double check(int mid)
{
	int i;
	double ans=0;
	for(i=0;i<mid;i++)
	{
		ans=ans+c/(2+i*f);
	}
	ans = ans + x/(2+i*f);
	return ans;
}
int main()
{
	int t,j;
	cin >> t;
	for(j=1;j<=t;j++)
	{
		cin >> c >> f >> x;
		int low=0;
		int high=(int)x;
		int mid;
		while(low<high)
		{
			mid=(low+high)/2;
			if(check(mid)>check(mid+1))	low=mid+1;
			else	high=mid;
		}
		printf("Case #%d: %.7lf\n",j,check(low));
	}
	return 0;
}
