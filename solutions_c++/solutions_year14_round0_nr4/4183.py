#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<set>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
#include<vector>
#include<iostream>
using namespace std;


int main()
{
	int tc,i;
	scanf("%d",&tc);
	for(i=1;i<=tc;i++)
	{
		int n,j,k,ans1,ans2;
		double a[1001],b[1001];
		scanf("%d",&n);
		
		for(j=0;j<n;j++)
		scanf("%lf",&a[j]);
		
		for(j=0;j<n;j++)
		scanf("%lf",&b[j]);
		
		sort(a,a+n);
		sort(b,b+n);
		
		ans1=0;
		ans2=0;
		
		k=0;
		for(j=0;j<n;j++)
		{
			for(;k<n;)
			{
				if(a[k]>b[j])
				{
					k++;
					ans1++;
					break;
				}
				k++;
			}
		}
		
		k=0;
		for(j=0;j<n;j++)
		{
			for(;k<n;)
			{
				if(a[j]<b[k])		
				{
					k++;
					ans2++;
					break;
				}
				k++;
			}
		}
		ans2=n-ans2;
		printf("Case #%d: %d %d\n",i,ans1,ans2);
	}
	return 0;
}

